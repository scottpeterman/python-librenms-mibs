# SNMP MIB module (IPS-3106-SE-PB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cts\IPS-3106-SE-PB-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:33:40 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysLocation,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysLocation")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6





class VLANPortMember(DisplayString):
    """Custom type VLANPortMember based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 27),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Cts_ObjectIdentity = ObjectIdentity
cts = _Cts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304)
)
_Swh_ObjectIdentity = ObjectIdentity
swh = _Swh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100)
)
_Ips3106se_ObjectIdentity = ObjectIdentity
ips3106se = _Ips3106se_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064)
)
_SwhSystemInformation_ObjectIdentity = ObjectIdentity
swhSystemInformation = _SwhSystemInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1)
)
_SwhCompanyInfo_ObjectIdentity = ObjectIdentity
swhCompanyInfo = _SwhCompanyInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 1)
)


class _SwhCompanyName_Type(DisplayString):
    """Custom type swhCompanyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhCompanyName_Type.__name__ = "DisplayString"
_SwhCompanyName_Object = MibScalar
swhCompanyName = _SwhCompanyName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 1, 1),
    _SwhCompanyName_Type()
)
swhCompanyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhCompanyName.setStatus("mandatory")


class _SwhCLIHostname_Type(DisplayString):
    """Custom type swhCLIHostname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhCLIHostname_Type.__name__ = "DisplayString"
_SwhCLIHostname_Object = MibScalar
swhCLIHostname = _SwhCLIHostname_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 1, 6),
    _SwhCLIHostname_Type()
)
swhCLIHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhCLIHostname.setStatus("mandatory")


class _SwhDHCPVendorID_Type(DisplayString):
    """Custom type swhDHCPVendorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhDHCPVendorID_Type.__name__ = "DisplayString"
_SwhDHCPVendorID_Object = MibScalar
swhDHCPVendorID = _SwhDHCPVendorID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 1, 7),
    _SwhDHCPVendorID_Type()
)
swhDHCPVendorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPVendorID.setStatus("mandatory")
_SwhHardwareInfo_ObjectIdentity = ObjectIdentity
swhHardwareInfo = _SwhHardwareInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2)
)


class _SwhModelName_Type(DisplayString):
    """Custom type swhModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhModelName_Type.__name__ = "DisplayString"
_SwhModelName_Object = MibScalar
swhModelName = _SwhModelName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 1),
    _SwhModelName_Type()
)
swhModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhModelName.setStatus("mandatory")


class _SwhMBVersion_Type(DisplayString):
    """Custom type swhMBVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhMBVersion_Type.__name__ = "DisplayString"
_SwhMBVersion_Object = MibScalar
swhMBVersion = _SwhMBVersion_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 9),
    _SwhMBVersion_Type()
)
swhMBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMBVersion.setStatus("mandatory")


class _SwhSerialNumber_Type(DisplayString):
    """Custom type swhSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhSerialNumber_Type.__name__ = "DisplayString"
_SwhSerialNumber_Object = MibScalar
swhSerialNumber = _SwhSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 14),
    _SwhSerialNumber_Type()
)
swhSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSerialNumber.setStatus("mandatory")


class _SwhDateCode_Type(DisplayString):
    """Custom type swhDateCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhDateCode_Type.__name__ = "DisplayString"
_SwhDateCode_Object = MibScalar
swhDateCode = _SwhDateCode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 15),
    _SwhDateCode_Type()
)
swhDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDateCode.setStatus("mandatory")


class _SwhCPUTemperature_Type(Integer32):
    """Custom type swhCPUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SwhCPUTemperature_Type.__name__ = "Integer32"
_SwhCPUTemperature_Object = MibScalar
swhCPUTemperature = _SwhCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 20),
    _SwhCPUTemperature_Type()
)
swhCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCPUTemperature.setStatus("mandatory")


class _SwhPowerSupply1_Type(Integer32):
    """Custom type swhPowerSupply1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("installed", 1),
          ("not-installed", 2))
    )


_SwhPowerSupply1_Type.__name__ = "Integer32"
_SwhPowerSupply1_Object = MibScalar
swhPowerSupply1 = _SwhPowerSupply1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 24),
    _SwhPowerSupply1_Type()
)
swhPowerSupply1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPowerSupply1.setStatus("mandatory")


class _SwhPowerSupply2_Type(Integer32):
    """Custom type swhPowerSupply2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("installed", 1),
          ("not-installed", 2))
    )


_SwhPowerSupply2_Type.__name__ = "Integer32"
_SwhPowerSupply2_Object = MibScalar
swhPowerSupply2 = _SwhPowerSupply2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 28),
    _SwhPowerSupply2_Type()
)
swhPowerSupply2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPowerSupply2.setStatus("mandatory")
_SwhBootUpImage_Type = DisplayString
_SwhBootUpImage_Object = MibScalar
swhBootUpImage = _SwhBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 40),
    _SwhBootUpImage_Type()
)
swhBootUpImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhBootUpImage.setStatus("mandatory")
_SwhNextBootUpImage_Type = DisplayString
_SwhNextBootUpImage_Object = MibScalar
swhNextBootUpImage = _SwhNextBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 41),
    _SwhNextBootUpImage_Type()
)
swhNextBootUpImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhNextBootUpImage.setStatus("mandatory")


class _SwhImage1FirmwareVersion_Type(DisplayString):
    """Custom type swhImage1FirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhImage1FirmwareVersion_Type.__name__ = "DisplayString"
_SwhImage1FirmwareVersion_Object = MibScalar
swhImage1FirmwareVersion = _SwhImage1FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 45),
    _SwhImage1FirmwareVersion_Type()
)
swhImage1FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhImage1FirmwareVersion.setStatus("mandatory")


class _SwhImage2FirmwareVersion_Type(DisplayString):
    """Custom type swhImage2FirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhImage2FirmwareVersion_Type.__name__ = "DisplayString"
_SwhImage2FirmwareVersion_Object = MibScalar
swhImage2FirmwareVersion = _SwhImage2FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 1, 2, 46),
    _SwhImage2FirmwareVersion_Type()
)
swhImage2FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhImage2FirmwareVersion.setStatus("mandatory")
_SwhUserAuthentication_ObjectIdentity = ObjectIdentity
swhUserAuthentication = _SwhUserAuthentication_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2)
)
_SwhUserTable_Object = MibTable
swhUserTable = _SwhUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 1)
)
if mibBuilder.loadTexts:
    swhUserTable.setStatus("mandatory")
_SwhUserEntry_Object = MibTableRow
swhUserEntry = _SwhUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 1, 1)
)
swhUserEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhUserIndex"),
)
if mibBuilder.loadTexts:
    swhUserEntry.setStatus("mandatory")


class _SwhUserIndex_Type(Integer32):
    """Custom type swhUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhUserIndex_Type.__name__ = "Integer32"
_SwhUserIndex_Object = MibTableColumn
swhUserIndex = _SwhUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 1, 1, 1),
    _SwhUserIndex_Type()
)
swhUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhUserIndex.setStatus("mandatory")


class _SwhUserEnable_Type(Integer32):
    """Custom type swhUserEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhUserEnable_Type.__name__ = "Integer32"
_SwhUserEnable_Object = MibTableColumn
swhUserEnable = _SwhUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 1, 1, 3),
    _SwhUserEnable_Type()
)
swhUserEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhUserEnable.setStatus("mandatory")


class _SwhUserName_Type(DisplayString):
    """Custom type swhUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhUserName_Type.__name__ = "DisplayString"
_SwhUserName_Object = MibTableColumn
swhUserName = _SwhUserName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 1, 1, 4),
    _SwhUserName_Type()
)
swhUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhUserName.setStatus("mandatory")


class _SwhUserPassword_Type(DisplayString):
    """Custom type swhUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhUserPassword_Type.__name__ = "DisplayString"
_SwhUserPassword_Object = MibTableColumn
swhUserPassword = _SwhUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 1, 1, 5),
    _SwhUserPassword_Type()
)
swhUserPassword.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhUserPassword.setStatus("mandatory")


class _SwhUserDescription_Type(DisplayString):
    """Custom type swhUserDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhUserDescription_Type.__name__ = "DisplayString"
_SwhUserDescription_Object = MibTableColumn
swhUserDescription = _SwhUserDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 1, 1, 6),
    _SwhUserDescription_Type()
)
swhUserDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhUserDescription.setStatus("mandatory")


class _SwhUserConsoleLevel_Type(Integer32):
    """Custom type swhUserConsoleLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2),
          ("administrator", 3))
    )


_SwhUserConsoleLevel_Type.__name__ = "Integer32"
_SwhUserConsoleLevel_Object = MibTableColumn
swhUserConsoleLevel = _SwhUserConsoleLevel_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 1, 1, 10),
    _SwhUserConsoleLevel_Type()
)
swhUserConsoleLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhUserConsoleLevel.setStatus("mandatory")
_SwhRADIUSConfiguration_ObjectIdentity = ObjectIdentity
swhRADIUSConfiguration = _SwhRADIUSConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2)
)


class _SwhRADIUSEn_Type(Integer32):
    """Custom type swhRADIUSEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhRADIUSEn_Type.__name__ = "Integer32"
_SwhRADIUSEn_Object = MibScalar
swhRADIUSEn = _SwhRADIUSEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2, 1),
    _SwhRADIUSEn_Type()
)
swhRADIUSEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRADIUSEn.setStatus("mandatory")
_SwhRADIUSSecretKey_Type = DisplayString
_SwhRADIUSSecretKey_Object = MibScalar
swhRADIUSSecretKey = _SwhRADIUSSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2, 2),
    _SwhRADIUSSecretKey_Type()
)
swhRADIUSSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRADIUSSecretKey.setStatus("mandatory")


class _SwhRADIUSPort_Type(Integer32):
    """Custom type swhRADIUSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SwhRADIUSPort_Type.__name__ = "Integer32"
_SwhRADIUSPort_Object = MibScalar
swhRADIUSPort = _SwhRADIUSPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2, 3),
    _SwhRADIUSPort_Type()
)
swhRADIUSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRADIUSPort.setStatus("mandatory")


class _SwhRADIUSRetry_Type(Integer32):
    """Custom type swhRADIUSRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SwhRADIUSRetry_Type.__name__ = "Integer32"
_SwhRADIUSRetry_Object = MibScalar
swhRADIUSRetry = _SwhRADIUSRetry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2, 5),
    _SwhRADIUSRetry_Type()
)
swhRADIUSRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRADIUSRetry.setStatus("mandatory")
_SwhRADIUSIPAddr_Type = IpAddress
_SwhRADIUSIPAddr_Object = MibScalar
swhRADIUSIPAddr = _SwhRADIUSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2, 6),
    _SwhRADIUSIPAddr_Type()
)
swhRADIUSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRADIUSIPAddr.setStatus("mandatory")
_SwhRADIUSIPAddr2_Type = IpAddress
_SwhRADIUSIPAddr2_Object = MibScalar
swhRADIUSIPAddr2 = _SwhRADIUSIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2, 7),
    _SwhRADIUSIPAddr2_Type()
)
swhRADIUSIPAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRADIUSIPAddr2.setStatus("mandatory")


class _SwhRADIUSIPv6Addr_Type(DisplayString):
    """Custom type swhRADIUSIPv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhRADIUSIPv6Addr_Type.__name__ = "DisplayString"
_SwhRADIUSIPv6Addr_Object = MibScalar
swhRADIUSIPv6Addr = _SwhRADIUSIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2, 8),
    _SwhRADIUSIPv6Addr_Type()
)
swhRADIUSIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRADIUSIPv6Addr.setStatus("mandatory")


class _SwhRADIUSIPv6Addr2_Type(DisplayString):
    """Custom type swhRADIUSIPv6Addr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhRADIUSIPv6Addr2_Type.__name__ = "DisplayString"
_SwhRADIUSIPv6Addr2_Object = MibScalar
swhRADIUSIPv6Addr2 = _SwhRADIUSIPv6Addr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 2, 9),
    _SwhRADIUSIPv6Addr2_Type()
)
swhRADIUSIPv6Addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRADIUSIPv6Addr2.setStatus("mandatory")
_SwhTACACSConfiguration_ObjectIdentity = ObjectIdentity
swhTACACSConfiguration = _SwhTACACSConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3)
)


class _SwhTACACSEn_Type(Integer32):
    """Custom type swhTACACSEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTACACSEn_Type.__name__ = "Integer32"
_SwhTACACSEn_Object = MibScalar
swhTACACSEn = _SwhTACACSEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3, 1),
    _SwhTACACSEn_Type()
)
swhTACACSEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTACACSEn.setStatus("mandatory")
_SwhTACACSSecretKey_Type = DisplayString
_SwhTACACSSecretKey_Object = MibScalar
swhTACACSSecretKey = _SwhTACACSSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3, 2),
    _SwhTACACSSecretKey_Type()
)
swhTACACSSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTACACSSecretKey.setStatus("mandatory")


class _SwhTACACSPort_Type(Integer32):
    """Custom type swhTACACSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1025, 65535),
    )


_SwhTACACSPort_Type.__name__ = "Integer32"
_SwhTACACSPort_Object = MibScalar
swhTACACSPort = _SwhTACACSPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3, 3),
    _SwhTACACSPort_Type()
)
swhTACACSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTACACSPort.setStatus("mandatory")


class _SwhTACACSRetry_Type(Integer32):
    """Custom type swhTACACSRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_SwhTACACSRetry_Type.__name__ = "Integer32"
_SwhTACACSRetry_Object = MibScalar
swhTACACSRetry = _SwhTACACSRetry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3, 5),
    _SwhTACACSRetry_Type()
)
swhTACACSRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTACACSRetry.setStatus("mandatory")
_SwhTACACSIPAddr_Type = IpAddress
_SwhTACACSIPAddr_Object = MibScalar
swhTACACSIPAddr = _SwhTACACSIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3, 6),
    _SwhTACACSIPAddr_Type()
)
swhTACACSIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTACACSIPAddr.setStatus("mandatory")
_SwhTACACSIPAddr2_Type = IpAddress
_SwhTACACSIPAddr2_Object = MibScalar
swhTACACSIPAddr2 = _SwhTACACSIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3, 7),
    _SwhTACACSIPAddr2_Type()
)
swhTACACSIPAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTACACSIPAddr2.setStatus("mandatory")


class _SwhTACACSIPv6Addr_Type(DisplayString):
    """Custom type swhTACACSIPv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhTACACSIPv6Addr_Type.__name__ = "DisplayString"
_SwhTACACSIPv6Addr_Object = MibScalar
swhTACACSIPv6Addr = _SwhTACACSIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3, 8),
    _SwhTACACSIPv6Addr_Type()
)
swhTACACSIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTACACSIPv6Addr.setStatus("mandatory")


class _SwhTACACSIPv6Addr2_Type(DisplayString):
    """Custom type swhTACACSIPv6Addr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhTACACSIPv6Addr2_Type.__name__ = "DisplayString"
_SwhTACACSIPv6Addr2_Object = MibScalar
swhTACACSIPv6Addr2 = _SwhTACACSIPv6Addr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 3, 9),
    _SwhTACACSIPv6Addr2_Type()
)
swhTACACSIPv6Addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTACACSIPv6Addr2.setStatus("mandatory")


class _SwhUserPasswordEncryption_Type(Integer32):
    """Custom type swhUserPasswordEncryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("md5", 1))
    )


_SwhUserPasswordEncryption_Type.__name__ = "Integer32"
_SwhUserPasswordEncryption_Object = MibScalar
swhUserPasswordEncryption = _SwhUserPasswordEncryption_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 2, 4),
    _SwhUserPasswordEncryption_Type()
)
swhUserPasswordEncryption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhUserPasswordEncryption.setStatus("mandatory")
_SwhNetworkManagement_ObjectIdentity = ObjectIdentity
swhNetworkManagement = _SwhNetworkManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3)
)
_SwhNetworkConfiguration_ObjectIdentity = ObjectIdentity
swhNetworkConfiguration = _SwhNetworkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1)
)
_SwhNetMacAddr_Type = MacAddress
_SwhNetMacAddr_Object = MibScalar
swhNetMacAddr = _SwhNetMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 1),
    _SwhNetMacAddr_Type()
)
swhNetMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhNetMacAddr.setStatus("mandatory")


class _SwhNetType_Type(Integer32):
    """Custom type swhNetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp", 0),
          ("manual", 1))
    )


_SwhNetType_Type.__name__ = "Integer32"
_SwhNetType_Object = MibScalar
swhNetType = _SwhNetType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 2),
    _SwhNetType_Type()
)
swhNetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetType.setStatus("mandatory")
_SwhNetIPAddr_Type = IpAddress
_SwhNetIPAddr_Object = MibScalar
swhNetIPAddr = _SwhNetIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 3),
    _SwhNetIPAddr_Type()
)
swhNetIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPAddr.setStatus("mandatory")
_SwhNetIPMask_Type = IpAddress
_SwhNetIPMask_Object = MibScalar
swhNetIPMask = _SwhNetIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 4),
    _SwhNetIPMask_Type()
)
swhNetIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPMask.setStatus("mandatory")
_SwhNetGateway_Type = IpAddress
_SwhNetGateway_Object = MibScalar
swhNetGateway = _SwhNetGateway_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 5),
    _SwhNetGateway_Type()
)
swhNetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetGateway.setStatus("mandatory")


class _SwhNetIPv4En_Type(Integer32):
    """Custom type swhNetIPv4En based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhNetIPv4En_Type.__name__ = "Integer32"
_SwhNetIPv4En_Object = MibScalar
swhNetIPv4En = _SwhNetIPv4En_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 8),
    _SwhNetIPv4En_Type()
)
swhNetIPv4En.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPv4En.setStatus("mandatory")
_SwhNetCurrentIPAddr_Type = IpAddress
_SwhNetCurrentIPAddr_Object = MibScalar
swhNetCurrentIPAddr = _SwhNetCurrentIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 10),
    _SwhNetCurrentIPAddr_Type()
)
swhNetCurrentIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhNetCurrentIPAddr.setStatus("mandatory")
_SwhNetCurrentIPMask_Type = IpAddress
_SwhNetCurrentIPMask_Object = MibScalar
swhNetCurrentIPMask = _SwhNetCurrentIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 11),
    _SwhNetCurrentIPMask_Type()
)
swhNetCurrentIPMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhNetCurrentIPMask.setStatus("mandatory")
_SwhNetCurrentGateway_Type = IpAddress
_SwhNetCurrentGateway_Object = MibScalar
swhNetCurrentGateway = _SwhNetCurrentGateway_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 12),
    _SwhNetCurrentGateway_Type()
)
swhNetCurrentGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhNetCurrentGateway.setStatus("mandatory")


class _SwhNetIPSourceBinding_Type(Integer32):
    """Custom type swhNetIPSourceBinding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhNetIPSourceBinding_Type.__name__ = "Integer32"
_SwhNetIPSourceBinding_Object = MibScalar
swhNetIPSourceBinding = _SwhNetIPSourceBinding_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 20),
    _SwhNetIPSourceBinding_Type()
)
swhNetIPSourceBinding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPSourceBinding.setStatus("mandatory")
_SwhNetIPSourceBindingTable_Object = MibTable
swhNetIPSourceBindingTable = _SwhNetIPSourceBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 21)
)
if mibBuilder.loadTexts:
    swhNetIPSourceBindingTable.setStatus("mandatory")
_SwhNetIPSourceBindingEntry_Object = MibTableRow
swhNetIPSourceBindingEntry = _SwhNetIPSourceBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 21, 1)
)
swhNetIPSourceBindingEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhNetIPSourceBindingIndex"),
)
if mibBuilder.loadTexts:
    swhNetIPSourceBindingEntry.setStatus("mandatory")


class _SwhNetIPSourceBindingIndex_Type(Integer32):
    """Custom type swhNetIPSourceBindingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhNetIPSourceBindingIndex_Type.__name__ = "Integer32"
_SwhNetIPSourceBindingIndex_Object = MibTableColumn
swhNetIPSourceBindingIndex = _SwhNetIPSourceBindingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 21, 1, 1),
    _SwhNetIPSourceBindingIndex_Type()
)
swhNetIPSourceBindingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhNetIPSourceBindingIndex.setStatus("mandatory")


class _SwhNetIPSourceBindingState_Type(Integer32):
    """Custom type swhNetIPSourceBindingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhNetIPSourceBindingState_Type.__name__ = "Integer32"
_SwhNetIPSourceBindingState_Object = MibTableColumn
swhNetIPSourceBindingState = _SwhNetIPSourceBindingState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 21, 1, 3),
    _SwhNetIPSourceBindingState_Type()
)
swhNetIPSourceBindingState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPSourceBindingState.setStatus("mandatory")
_SwhNetIPSourceBindingIPAddress_Type = DisplayString
_SwhNetIPSourceBindingIPAddress_Object = MibTableColumn
swhNetIPSourceBindingIPAddress = _SwhNetIPSourceBindingIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 21, 1, 4),
    _SwhNetIPSourceBindingIPAddress_Type()
)
swhNetIPSourceBindingIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPSourceBindingIPAddress.setStatus("mandatory")
_SwhNetIPSourceBindingIPv6Address_Type = DisplayString
_SwhNetIPSourceBindingIPv6Address_Object = MibTableColumn
swhNetIPSourceBindingIPv6Address = _SwhNetIPSourceBindingIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 21, 1, 5),
    _SwhNetIPSourceBindingIPv6Address_Type()
)
swhNetIPSourceBindingIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPSourceBindingIPv6Address.setStatus("mandatory")


class _SwhNetIPSourceBindingDelete_Type(Integer32):
    """Custom type swhNetIPSourceBindingDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhNetIPSourceBindingDelete_Type.__name__ = "Integer32"
_SwhNetIPSourceBindingDelete_Object = MibTableColumn
swhNetIPSourceBindingDelete = _SwhNetIPSourceBindingDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 21, 1, 10),
    _SwhNetIPSourceBindingDelete_Type()
)
swhNetIPSourceBindingDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPSourceBindingDelete.setStatus("mandatory")


class _SwhNetIPv6En_Type(Integer32):
    """Custom type swhNetIPv6En based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhNetIPv6En_Type.__name__ = "Integer32"
_SwhNetIPv6En_Object = MibScalar
swhNetIPv6En = _SwhNetIPv6En_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 32),
    _SwhNetIPv6En_Type()
)
swhNetIPv6En.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPv6En.setStatus("mandatory")


class _SwhNetIPv6AutoConfig_Type(Integer32):
    """Custom type swhNetIPv6AutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhNetIPv6AutoConfig_Type.__name__ = "Integer32"
_SwhNetIPv6AutoConfig_Object = MibScalar
swhNetIPv6AutoConfig = _SwhNetIPv6AutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 33),
    _SwhNetIPv6AutoConfig_Type()
)
swhNetIPv6AutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPv6AutoConfig.setStatus("mandatory")


class _SwhNetIPv6LinkLocalAddr_Type(DisplayString):
    """Custom type swhNetIPv6LinkLocalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhNetIPv6LinkLocalAddr_Type.__name__ = "DisplayString"
_SwhNetIPv6LinkLocalAddr_Object = MibScalar
swhNetIPv6LinkLocalAddr = _SwhNetIPv6LinkLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 34),
    _SwhNetIPv6LinkLocalAddr_Type()
)
swhNetIPv6LinkLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPv6LinkLocalAddr.setStatus("mandatory")


class _SwhNetIPv6GlobalAddr_Type(DisplayString):
    """Custom type swhNetIPv6GlobalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhNetIPv6GlobalAddr_Type.__name__ = "DisplayString"
_SwhNetIPv6GlobalAddr_Object = MibScalar
swhNetIPv6GlobalAddr = _SwhNetIPv6GlobalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 35),
    _SwhNetIPv6GlobalAddr_Type()
)
swhNetIPv6GlobalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPv6GlobalAddr.setStatus("mandatory")


class _SwhNetIPv6Gateway_Type(DisplayString):
    """Custom type swhNetIPv6Gateway based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhNetIPv6Gateway_Type.__name__ = "DisplayString"
_SwhNetIPv6Gateway_Object = MibScalar
swhNetIPv6Gateway = _SwhNetIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 36),
    _SwhNetIPv6Gateway_Type()
)
swhNetIPv6Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetIPv6Gateway.setStatus("mandatory")


class _SwhNetDHCPv6_Type(Integer32):
    """Custom type swhNetDHCPv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("auto", 1),
          ("force", 2))
    )


_SwhNetDHCPv6_Type.__name__ = "Integer32"
_SwhNetDHCPv6_Object = MibScalar
swhNetDHCPv6 = _SwhNetDHCPv6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 37),
    _SwhNetDHCPv6_Type()
)
swhNetDHCPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetDHCPv6.setStatus("mandatory")


class _SwhNetRapidCommit_Type(Integer32):
    """Custom type swhNetRapidCommit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhNetRapidCommit_Type.__name__ = "Integer32"
_SwhNetRapidCommit_Object = MibScalar
swhNetRapidCommit = _SwhNetRapidCommit_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 38),
    _SwhNetRapidCommit_Type()
)
swhNetRapidCommit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNetRapidCommit.setStatus("mandatory")


class _SwhNetCurrentIPv6LinklocalAddr_Type(DisplayString):
    """Custom type swhNetCurrentIPv6LinklocalAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhNetCurrentIPv6LinklocalAddr_Type.__name__ = "DisplayString"
_SwhNetCurrentIPv6LinklocalAddr_Object = MibScalar
swhNetCurrentIPv6LinklocalAddr = _SwhNetCurrentIPv6LinklocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 39),
    _SwhNetCurrentIPv6LinklocalAddr_Type()
)
swhNetCurrentIPv6LinklocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhNetCurrentIPv6LinklocalAddr.setStatus("mandatory")


class _SwhNetCurrentIPv6GatewayAddr_Type(DisplayString):
    """Custom type swhNetCurrentIPv6GatewayAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhNetCurrentIPv6GatewayAddr_Type.__name__ = "DisplayString"
_SwhNetCurrentIPv6GatewayAddr_Object = MibScalar
swhNetCurrentIPv6GatewayAddr = _SwhNetCurrentIPv6GatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 40),
    _SwhNetCurrentIPv6GatewayAddr_Type()
)
swhNetCurrentIPv6GatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhNetCurrentIPv6GatewayAddr.setStatus("mandatory")


class _SwhNetCurrentDHCPv6DUID_Type(DisplayString):
    """Custom type swhNetCurrentDHCPv6DUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhNetCurrentDHCPv6DUID_Type.__name__ = "DisplayString"
_SwhNetCurrentDHCPv6DUID_Object = MibScalar
swhNetCurrentDHCPv6DUID = _SwhNetCurrentDHCPv6DUID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 1, 41),
    _SwhNetCurrentDHCPv6DUID_Type()
)
swhNetCurrentDHCPv6DUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhNetCurrentDHCPv6DUID.setStatus("mandatory")
_SwhSystemServiceConfiguration_ObjectIdentity = ObjectIdentity
swhSystemServiceConfiguration = _SwhSystemServiceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 2)
)


class _SwhServiceTelnetThreadEn_Type(Integer32):
    """Custom type swhServiceTelnetThreadEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhServiceTelnetThreadEn_Type.__name__ = "Integer32"
_SwhServiceTelnetThreadEn_Object = MibScalar
swhServiceTelnetThreadEn = _SwhServiceTelnetThreadEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 2, 1),
    _SwhServiceTelnetThreadEn_Type()
)
swhServiceTelnetThreadEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhServiceTelnetThreadEn.setStatus("mandatory")


class _SwhServiceSNMPThreadEn_Type(Integer32):
    """Custom type swhServiceSNMPThreadEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhServiceSNMPThreadEn_Type.__name__ = "Integer32"
_SwhServiceSNMPThreadEn_Object = MibScalar
swhServiceSNMPThreadEn = _SwhServiceSNMPThreadEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 2, 3),
    _SwhServiceSNMPThreadEn_Type()
)
swhServiceSNMPThreadEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhServiceSNMPThreadEn.setStatus("mandatory")


class _SwhServiceWebThreadEn_Type(Integer32):
    """Custom type swhServiceWebThreadEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhServiceWebThreadEn_Type.__name__ = "Integer32"
_SwhServiceWebThreadEn_Object = MibScalar
swhServiceWebThreadEn = _SwhServiceWebThreadEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 2, 4),
    _SwhServiceWebThreadEn_Type()
)
swhServiceWebThreadEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhServiceWebThreadEn.setStatus("mandatory")


class _SwhServiceSSHThreadEn_Type(Integer32):
    """Custom type swhServiceSSHThreadEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhServiceSSHThreadEn_Type.__name__ = "Integer32"
_SwhServiceSSHThreadEn_Object = MibScalar
swhServiceSSHThreadEn = _SwhServiceSSHThreadEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 2, 10),
    _SwhServiceSSHThreadEn_Type()
)
swhServiceSSHThreadEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhServiceSSHThreadEn.setStatus("mandatory")


class _SwhServiceConsolePortThreadEn_Type(Integer32):
    """Custom type swhServiceConsolePortThreadEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhServiceConsolePortThreadEn_Type.__name__ = "Integer32"
_SwhServiceConsolePortThreadEn_Object = MibScalar
swhServiceConsolePortThreadEn = _SwhServiceConsolePortThreadEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 2, 12),
    _SwhServiceConsolePortThreadEn_Type()
)
swhServiceConsolePortThreadEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhServiceConsolePortThreadEn.setStatus("mandatory")
_SwhRS232TelnetConsoleConfiguration_ObjectIdentity = ObjectIdentity
swhRS232TelnetConsoleConfiguration = _SwhRS232TelnetConsoleConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3)
)
_SwhRS232BaudRate_Type = Integer32
_SwhRS232BaudRate_Object = MibScalar
swhRS232BaudRate = _SwhRS232BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 2),
    _SwhRS232BaudRate_Type()
)
swhRS232BaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRS232BaudRate.setStatus("mandatory")


class _SwhRS232StopBits_Type(Integer32):
    """Custom type swhRS232StopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("x1", 1),
          ("x1-5", 2),
          ("x2", 3))
    )


_SwhRS232StopBits_Type.__name__ = "Integer32"
_SwhRS232StopBits_Object = MibScalar
swhRS232StopBits = _SwhRS232StopBits_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 3),
    _SwhRS232StopBits_Type()
)
swhRS232StopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRS232StopBits.setStatus("mandatory")


class _SwhRS232ParityCheck_Type(Integer32):
    """Custom type swhRS232ParityCheck based on Integer32"""
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
        *(("none", 0),
          ("even", 1),
          ("odd", 2),
          ("mark", 3),
          ("space", 4))
    )


_SwhRS232ParityCheck_Type.__name__ = "Integer32"
_SwhRS232ParityCheck_Object = MibScalar
swhRS232ParityCheck = _SwhRS232ParityCheck_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 4),
    _SwhRS232ParityCheck_Type()
)
swhRS232ParityCheck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRS232ParityCheck.setStatus("mandatory")
_SwhRS232WordLength_Type = Integer32
_SwhRS232WordLength_Object = MibScalar
swhRS232WordLength = _SwhRS232WordLength_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 5),
    _SwhRS232WordLength_Type()
)
swhRS232WordLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRS232WordLength.setStatus("mandatory")


class _SwhRS232FlowControl_Type(Integer32):
    """Custom type swhRS232FlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("hardware", 1))
    )


_SwhRS232FlowControl_Type.__name__ = "Integer32"
_SwhRS232FlowControl_Object = MibScalar
swhRS232FlowControl = _SwhRS232FlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 6),
    _SwhRS232FlowControl_Type()
)
swhRS232FlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRS232FlowControl.setStatus("mandatory")
_SwhTelnetPort_Type = Integer32
_SwhTelnetPort_Object = MibScalar
swhTelnetPort = _SwhTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 8),
    _SwhTelnetPort_Type()
)
swhTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTelnetPort.setStatus("mandatory")


class _SwhTimeOutTime_Type(Integer32):
    """Custom type swhTimeOutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SwhTimeOutTime_Type.__name__ = "Integer32"
_SwhTimeOutTime_Object = MibScalar
swhTimeOutTime = _SwhTimeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 11),
    _SwhTimeOutTime_Type()
)
swhTimeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeOutTime.setStatus("mandatory")


class _SwhTimeOutTimeUnit_Type(Integer32):
    """Custom type swhTimeOutTimeUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("seconds", 0),
          ("minutes", 1))
    )


_SwhTimeOutTimeUnit_Type.__name__ = "Integer32"
_SwhTimeOutTimeUnit_Object = MibScalar
swhTimeOutTimeUnit = _SwhTimeOutTimeUnit_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 12),
    _SwhTimeOutTimeUnit_Type()
)
swhTimeOutTimeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeOutTimeUnit.setStatus("mandatory")


class _SwhWebTimeOutTime_Type(Integer32):
    """Custom type swhWebTimeOutTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SwhWebTimeOutTime_Type.__name__ = "Integer32"
_SwhWebTimeOutTime_Object = MibScalar
swhWebTimeOutTime = _SwhWebTimeOutTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 13),
    _SwhWebTimeOutTime_Type()
)
swhWebTimeOutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhWebTimeOutTime.setStatus("mandatory")


class _SwhConsolePortFailRetry_Type(Integer32):
    """Custom type swhConsolePortFailRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SwhConsolePortFailRetry_Type.__name__ = "Integer32"
_SwhConsolePortFailRetry_Object = MibScalar
swhConsolePortFailRetry = _SwhConsolePortFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 14),
    _SwhConsolePortFailRetry_Type()
)
swhConsolePortFailRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhConsolePortFailRetry.setStatus("mandatory")


class _SwhConsolePortFailBlockTime_Type(Integer32):
    """Custom type swhConsolePortFailBlockTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SwhConsolePortFailBlockTime_Type.__name__ = "Integer32"
_SwhConsolePortFailBlockTime_Object = MibScalar
swhConsolePortFailBlockTime = _SwhConsolePortFailBlockTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 3, 15),
    _SwhConsolePortFailBlockTime_Type()
)
swhConsolePortFailBlockTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhConsolePortFailBlockTime.setStatus("mandatory")
_SwhDeviceCommunity_ObjectIdentity = ObjectIdentity
swhDeviceCommunity = _SwhDeviceCommunity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4)
)
_SwhAgentTable_Object = MibTable
swhAgentTable = _SwhAgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1)
)
if mibBuilder.loadTexts:
    swhAgentTable.setStatus("mandatory")
_SwhAgentEntry_Object = MibTableRow
swhAgentEntry = _SwhAgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1, 1)
)
swhAgentEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhAgentIndex"),
)
if mibBuilder.loadTexts:
    swhAgentEntry.setStatus("mandatory")


class _SwhAgentIndex_Type(Integer32):
    """Custom type swhAgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhAgentIndex_Type.__name__ = "Integer32"
_SwhAgentIndex_Object = MibTableColumn
swhAgentIndex = _SwhAgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1, 1, 1),
    _SwhAgentIndex_Type()
)
swhAgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhAgentIndex.setStatus("mandatory")


class _SwhAgentValid_Type(Integer32):
    """Custom type swhAgentValid based on Integer32"""
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


_SwhAgentValid_Type.__name__ = "Integer32"
_SwhAgentValid_Object = MibTableColumn
swhAgentValid = _SwhAgentValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1, 1, 2),
    _SwhAgentValid_Type()
)
swhAgentValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhAgentValid.setStatus("mandatory")


class _SwhAgentEnable_Type(Integer32):
    """Custom type swhAgentEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhAgentEnable_Type.__name__ = "Integer32"
_SwhAgentEnable_Object = MibTableColumn
swhAgentEnable = _SwhAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1, 1, 3),
    _SwhAgentEnable_Type()
)
swhAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAgentEnable.setStatus("mandatory")


class _SwhAgentCommunity_Type(DisplayString):
    """Custom type swhAgentCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhAgentCommunity_Type.__name__ = "DisplayString"
_SwhAgentCommunity_Object = MibTableColumn
swhAgentCommunity = _SwhAgentCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1, 1, 4),
    _SwhAgentCommunity_Type()
)
swhAgentCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAgentCommunity.setStatus("mandatory")


class _SwhAgentDescription_Type(DisplayString):
    """Custom type swhAgentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhAgentDescription_Type.__name__ = "DisplayString"
_SwhAgentDescription_Object = MibTableColumn
swhAgentDescription = _SwhAgentDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1, 1, 6),
    _SwhAgentDescription_Type()
)
swhAgentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAgentDescription.setStatus("mandatory")


class _SwhAgentSNMPLevel_Type(Integer32):
    """Custom type swhAgentSNMPLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2),
          ("administrator", 3))
    )


_SwhAgentSNMPLevel_Type.__name__ = "Integer32"
_SwhAgentSNMPLevel_Object = MibTableColumn
swhAgentSNMPLevel = _SwhAgentSNMPLevel_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1, 1, 9),
    _SwhAgentSNMPLevel_Type()
)
swhAgentSNMPLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAgentSNMPLevel.setStatus("mandatory")


class _SwhAgentDelete_Type(Integer32):
    """Custom type swhAgentDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhAgentDelete_Type.__name__ = "Integer32"
_SwhAgentDelete_Object = MibTableColumn
swhAgentDelete = _SwhAgentDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 1, 1, 10),
    _SwhAgentDelete_Type()
)
swhAgentDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAgentDelete.setStatus("mandatory")
_SwhSNMPv3AgentTable_Object = MibTable
swhSNMPv3AgentTable = _SwhSNMPv3AgentTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5)
)
if mibBuilder.loadTexts:
    swhSNMPv3AgentTable.setStatus("mandatory")
_SwhSNMPv3AgentEntry_Object = MibTableRow
swhSNMPv3AgentEntry = _SwhSNMPv3AgentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5, 1)
)
swhSNMPv3AgentEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhSNMPv3AgentIndex"),
)
if mibBuilder.loadTexts:
    swhSNMPv3AgentEntry.setStatus("mandatory")


class _SwhSNMPv3AgentIndex_Type(Integer32):
    """Custom type swhSNMPv3AgentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhSNMPv3AgentIndex_Type.__name__ = "Integer32"
_SwhSNMPv3AgentIndex_Object = MibTableColumn
swhSNMPv3AgentIndex = _SwhSNMPv3AgentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5, 1, 1),
    _SwhSNMPv3AgentIndex_Type()
)
swhSNMPv3AgentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhSNMPv3AgentIndex.setStatus("mandatory")


class _SwhSNMPv3AgentValid_Type(Integer32):
    """Custom type swhSNMPv3AgentValid based on Integer32"""
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


_SwhSNMPv3AgentValid_Type.__name__ = "Integer32"
_SwhSNMPv3AgentValid_Object = MibTableColumn
swhSNMPv3AgentValid = _SwhSNMPv3AgentValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5, 1, 3),
    _SwhSNMPv3AgentValid_Type()
)
swhSNMPv3AgentValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSNMPv3AgentValid.setStatus("mandatory")


class _SwhSNMPv3AgentUserName_Type(DisplayString):
    """Custom type swhSNMPv3AgentUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhSNMPv3AgentUserName_Type.__name__ = "DisplayString"
_SwhSNMPv3AgentUserName_Object = MibTableColumn
swhSNMPv3AgentUserName = _SwhSNMPv3AgentUserName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5, 1, 7),
    _SwhSNMPv3AgentUserName_Type()
)
swhSNMPv3AgentUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSNMPv3AgentUserName.setStatus("mandatory")


class _SwhSNMPv3AgentAuthentication_Type(Integer32):
    """Custom type swhSNMPv3AgentAuthentication based on Integer32"""
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
          ("md5", 1),
          ("sha", 2))
    )


_SwhSNMPv3AgentAuthentication_Type.__name__ = "Integer32"
_SwhSNMPv3AgentAuthentication_Object = MibTableColumn
swhSNMPv3AgentAuthentication = _SwhSNMPv3AgentAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5, 1, 9),
    _SwhSNMPv3AgentAuthentication_Type()
)
swhSNMPv3AgentAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSNMPv3AgentAuthentication.setStatus("mandatory")


class _SwhSNMPv3AgentAuthPassword_Type(DisplayString):
    """Custom type swhSNMPv3AgentAuthPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhSNMPv3AgentAuthPassword_Type.__name__ = "DisplayString"
_SwhSNMPv3AgentAuthPassword_Object = MibTableColumn
swhSNMPv3AgentAuthPassword = _SwhSNMPv3AgentAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5, 1, 11),
    _SwhSNMPv3AgentAuthPassword_Type()
)
swhSNMPv3AgentAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSNMPv3AgentAuthPassword.setStatus("mandatory")


class _SwhSNMPv3AgentPrivate_Type(Integer32):
    """Custom type swhSNMPv3AgentPrivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("des", 1))
    )


_SwhSNMPv3AgentPrivate_Type.__name__ = "Integer32"
_SwhSNMPv3AgentPrivate_Object = MibTableColumn
swhSNMPv3AgentPrivate = _SwhSNMPv3AgentPrivate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5, 1, 12),
    _SwhSNMPv3AgentPrivate_Type()
)
swhSNMPv3AgentPrivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSNMPv3AgentPrivate.setStatus("mandatory")


class _SwhSNMPv3AgentPrivPassword_Type(DisplayString):
    """Custom type swhSNMPv3AgentPrivPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhSNMPv3AgentPrivPassword_Type.__name__ = "DisplayString"
_SwhSNMPv3AgentPrivPassword_Object = MibTableColumn
swhSNMPv3AgentPrivPassword = _SwhSNMPv3AgentPrivPassword_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 4, 5, 1, 13),
    _SwhSNMPv3AgentPrivPassword_Type()
)
swhSNMPv3AgentPrivPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSNMPv3AgentPrivPassword.setStatus("mandatory")
_SwhTrapDestination_ObjectIdentity = ObjectIdentity
swhTrapDestination = _SwhTrapDestination_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 5)
)
_SwhTrapDestTable_Object = MibTable
swhTrapDestTable = _SwhTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 5, 1)
)
if mibBuilder.loadTexts:
    swhTrapDestTable.setStatus("mandatory")
_SwhTrapDestEntry_Object = MibTableRow
swhTrapDestEntry = _SwhTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 5, 1, 1)
)
swhTrapDestEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhTrapDestIndex"),
)
if mibBuilder.loadTexts:
    swhTrapDestEntry.setStatus("mandatory")


class _SwhTrapDestIndex_Type(Integer32):
    """Custom type swhTrapDestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhTrapDestIndex_Type.__name__ = "Integer32"
_SwhTrapDestIndex_Object = MibTableColumn
swhTrapDestIndex = _SwhTrapDestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 5, 1, 1, 1),
    _SwhTrapDestIndex_Type()
)
swhTrapDestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhTrapDestIndex.setStatus("mandatory")


class _SwhTrapDestEnable_Type(Integer32):
    """Custom type swhTrapDestEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapDestEnable_Type.__name__ = "Integer32"
_SwhTrapDestEnable_Object = MibTableColumn
swhTrapDestEnable = _SwhTrapDestEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 5, 1, 1, 3),
    _SwhTrapDestEnable_Type()
)
swhTrapDestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapDestEnable.setStatus("mandatory")


class _SwhTrapDestCommunity_Type(DisplayString):
    """Custom type swhTrapDestCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhTrapDestCommunity_Type.__name__ = "DisplayString"
_SwhTrapDestCommunity_Object = MibTableColumn
swhTrapDestCommunity = _SwhTrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 5, 1, 1, 4),
    _SwhTrapDestCommunity_Type()
)
swhTrapDestCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapDestCommunity.setStatus("mandatory")
_SwhTrapDestIPAddr_Type = IpAddress
_SwhTrapDestIPAddr_Object = MibTableColumn
swhTrapDestIPAddr = _SwhTrapDestIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 5, 1, 1, 8),
    _SwhTrapDestIPAddr_Type()
)
swhTrapDestIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapDestIPAddr.setStatus("mandatory")


class _SwhTrapDestIPv6Addr_Type(DisplayString):
    """Custom type swhTrapDestIPv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhTrapDestIPv6Addr_Type.__name__ = "DisplayString"
_SwhTrapDestIPv6Addr_Object = MibTableColumn
swhTrapDestIPv6Addr = _SwhTrapDestIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 5, 1, 1, 9),
    _SwhTrapDestIPv6Addr_Type()
)
swhTrapDestIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapDestIPv6Addr.setStatus("mandatory")
_SwhTrapConfiguration_ObjectIdentity = ObjectIdentity
swhTrapConfiguration = _SwhTrapConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6)
)


class _SwhTrapColdStart_Type(Integer32):
    """Custom type swhTrapColdStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapColdStart_Type.__name__ = "Integer32"
_SwhTrapColdStart_Object = MibScalar
swhTrapColdStart = _SwhTrapColdStart_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 1),
    _SwhTrapColdStart_Type()
)
swhTrapColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapColdStart.setStatus("mandatory")


class _SwhTrapWarmStart_Type(Integer32):
    """Custom type swhTrapWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapWarmStart_Type.__name__ = "Integer32"
_SwhTrapWarmStart_Object = MibScalar
swhTrapWarmStart = _SwhTrapWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 2),
    _SwhTrapWarmStart_Type()
)
swhTrapWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapWarmStart.setStatus("mandatory")


class _SwhTrapAuthenticationFailure_Type(Integer32):
    """Custom type swhTrapAuthenticationFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapAuthenticationFailure_Type.__name__ = "Integer32"
_SwhTrapAuthenticationFailure_Object = MibScalar
swhTrapAuthenticationFailure = _SwhTrapAuthenticationFailure_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 3),
    _SwhTrapAuthenticationFailure_Type()
)
swhTrapAuthenticationFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapAuthenticationFailure.setStatus("mandatory")


class _SwhTrapPortLink_Type(Integer32):
    """Custom type swhTrapPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapPortLink_Type.__name__ = "Integer32"
_SwhTrapPortLink_Object = MibScalar
swhTrapPortLink = _SwhTrapPortLink_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 4),
    _SwhTrapPortLink_Type()
)
swhTrapPortLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapPortLink.setStatus("mandatory")


class _SwhTrapPowerFailure_Type(Integer32):
    """Custom type swhTrapPowerFailure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapPowerFailure_Type.__name__ = "Integer32"
_SwhTrapPowerFailure_Object = MibScalar
swhTrapPowerFailure = _SwhTrapPowerFailure_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 5),
    _SwhTrapPowerFailure_Type()
)
swhTrapPowerFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapPowerFailure.setStatus("mandatory")


class _SwhTrapCPULoading_Type(Integer32):
    """Custom type swhTrapCPULoading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapCPULoading_Type.__name__ = "Integer32"
_SwhTrapCPULoading_Object = MibScalar
swhTrapCPULoading = _SwhTrapCPULoading_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 11),
    _SwhTrapCPULoading_Type()
)
swhTrapCPULoading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapCPULoading.setStatus("mandatory")


class _SwhTrapAutoBackup_Type(Integer32):
    """Custom type swhTrapAutoBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapAutoBackup_Type.__name__ = "Integer32"
_SwhTrapAutoBackup_Object = MibScalar
swhTrapAutoBackup = _SwhTrapAutoBackup_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 13),
    _SwhTrapAutoBackup_Type()
)
swhTrapAutoBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapAutoBackup.setStatus("mandatory")


class _SwhTrapMACLimiter_Type(Integer32):
    """Custom type swhTrapMACLimiter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapMACLimiter_Type.__name__ = "Integer32"
_SwhTrapMACLimiter_Object = MibScalar
swhTrapMACLimiter = _SwhTrapMACLimiter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 14),
    _SwhTrapMACLimiter_Type()
)
swhTrapMACLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapMACLimiter.setStatus("mandatory")


class _SwhTrapStormControl_Type(Integer32):
    """Custom type swhTrapStormControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapStormControl_Type.__name__ = "Integer32"
_SwhTrapStormControl_Object = MibScalar
swhTrapStormControl = _SwhTrapStormControl_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 15),
    _SwhTrapStormControl_Type()
)
swhTrapStormControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapStormControl.setStatus("mandatory")


class _SwhTrapDigitalState_Type(Integer32):
    """Custom type swhTrapDigitalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapDigitalState_Type.__name__ = "Integer32"
_SwhTrapDigitalState_Object = MibScalar
swhTrapDigitalState = _SwhTrapDigitalState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 16),
    _SwhTrapDigitalState_Type()
)
swhTrapDigitalState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapDigitalState.setStatus("mandatory")


class _SwhTrapConsolePortLink_Type(Integer32):
    """Custom type swhTrapConsolePortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapConsolePortLink_Type.__name__ = "Integer32"
_SwhTrapConsolePortLink_Object = MibScalar
swhTrapConsolePortLink = _SwhTrapConsolePortLink_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 17),
    _SwhTrapConsolePortLink_Type()
)
swhTrapConsolePortLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapConsolePortLink.setStatus("mandatory")


class _SwhTrapCPUTemperature_Type(Integer32):
    """Custom type swhTrapCPUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapCPUTemperature_Type.__name__ = "Integer32"
_SwhTrapCPUTemperature_Object = MibScalar
swhTrapCPUTemperature = _SwhTrapCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 18),
    _SwhTrapCPUTemperature_Type()
)
swhTrapCPUTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapCPUTemperature.setStatus("mandatory")


class _SwhTrapFastRedundancy_Type(Integer32):
    """Custom type swhTrapFastRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTrapFastRedundancy_Type.__name__ = "Integer32"
_SwhTrapFastRedundancy_Object = MibScalar
swhTrapFastRedundancy = _SwhTrapFastRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 6, 75),
    _SwhTrapFastRedundancy_Type()
)
swhTrapFastRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTrapFastRedundancy.setStatus("mandatory")
_SwhTimeServerConfiguration_ObjectIdentity = ObjectIdentity
swhTimeServerConfiguration = _SwhTimeServerConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7)
)


class _SwhTimeSync_Type(Integer32):
    """Custom type swhTimeSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhTimeSync_Type.__name__ = "Integer32"
_SwhTimeSync_Object = MibScalar
swhTimeSync = _SwhTimeSync_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 1),
    _SwhTimeSync_Type()
)
swhTimeSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeSync.setStatus("mandatory")
_SwhTimeServerIPAddr_Type = IpAddress
_SwhTimeServerIPAddr_Object = MibScalar
swhTimeServerIPAddr = _SwhTimeServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 2),
    _SwhTimeServerIPAddr_Type()
)
swhTimeServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeServerIPAddr.setStatus("mandatory")
_SwhTimeServerIPAddr2_Type = IpAddress
_SwhTimeServerIPAddr2_Object = MibScalar
swhTimeServerIPAddr2 = _SwhTimeServerIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 3),
    _SwhTimeServerIPAddr2_Type()
)
swhTimeServerIPAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeServerIPAddr2.setStatus("mandatory")


class _SwhTimeSyncInterval_Type(Integer32):
    """Custom type swhTimeSyncInterval based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("hour1", 1),
          ("hour2", 2),
          ("hour3", 3),
          ("hour4", 4),
          ("hour6", 5),
          ("hour8", 6),
          ("hour12", 7),
          ("hour24", 8))
    )


_SwhTimeSyncInterval_Type.__name__ = "Integer32"
_SwhTimeSyncInterval_Object = MibScalar
swhTimeSyncInterval = _SwhTimeSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 4),
    _SwhTimeSyncInterval_Type()
)
swhTimeSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeSyncInterval.setStatus("mandatory")
_SwhTimeZoneIndex_Type = Integer32
_SwhTimeZoneIndex_Object = MibScalar
swhTimeZoneIndex = _SwhTimeZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 5),
    _SwhTimeZoneIndex_Type()
)
swhTimeZoneIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeZoneIndex.setStatus("mandatory")
_SwhTimeZone_Type = DisplayString
_SwhTimeZone_Object = MibScalar
swhTimeZone = _SwhTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 6),
    _SwhTimeZone_Type()
)
swhTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhTimeZone.setStatus("mandatory")


class _SwhTimeDST_Type(Integer32):
    """Custom type swhTimeDST based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("recurring", 1),
          ("date", 2))
    )


_SwhTimeDST_Type.__name__ = "Integer32"
_SwhTimeDST_Object = MibScalar
swhTimeDST = _SwhTimeDST_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 7),
    _SwhTimeDST_Type()
)
swhTimeDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeDST.setStatus("mandatory")
_SwhTimeDSTRange_Type = DisplayString
_SwhTimeDSTRange_Object = MibScalar
swhTimeDSTRange = _SwhTimeDSTRange_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 9),
    _SwhTimeDSTRange_Type()
)
swhTimeDSTRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeDSTRange.setStatus("mandatory")
_SwhTimeServerIPv6Addr_Type = DisplayString
_SwhTimeServerIPv6Addr_Object = MibScalar
swhTimeServerIPv6Addr = _SwhTimeServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 20),
    _SwhTimeServerIPv6Addr_Type()
)
swhTimeServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeServerIPv6Addr.setStatus("mandatory")
_SwhTimeServerIPv6Addr2_Type = DisplayString
_SwhTimeServerIPv6Addr2_Object = MibScalar
swhTimeServerIPv6Addr2 = _SwhTimeServerIPv6Addr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 7, 21),
    _SwhTimeServerIPv6Addr2_Type()
)
swhTimeServerIPv6Addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeServerIPv6Addr2.setStatus("mandatory")
_SwhSyslogConfiguration_ObjectIdentity = ObjectIdentity
swhSyslogConfiguration = _SwhSyslogConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8)
)


class _SwhLogServer_Type(Integer32):
    """Custom type swhLogServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLogServer_Type.__name__ = "Integer32"
_SwhLogServer_Object = MibScalar
swhLogServer = _SwhLogServer_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 1),
    _SwhLogServer_Type()
)
swhLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLogServer.setStatus("mandatory")


class _SwhLogSNTPStatus_Type(Integer32):
    """Custom type swhLogSNTPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLogSNTPStatus_Type.__name__ = "Integer32"
_SwhLogSNTPStatus_Object = MibScalar
swhLogSNTPStatus = _SwhLogSNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 3),
    _SwhLogSNTPStatus_Type()
)
swhLogSNTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLogSNTPStatus.setStatus("mandatory")
_SwhLogServerIPAddr1_Type = IpAddress
_SwhLogServerIPAddr1_Object = MibScalar
swhLogServerIPAddr1 = _SwhLogServerIPAddr1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 4),
    _SwhLogServerIPAddr1_Type()
)
swhLogServerIPAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLogServerIPAddr1.setStatus("mandatory")
_SwhLogServerIPAddr2_Type = IpAddress
_SwhLogServerIPAddr2_Object = MibScalar
swhLogServerIPAddr2 = _SwhLogServerIPAddr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 5),
    _SwhLogServerIPAddr2_Type()
)
swhLogServerIPAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLogServerIPAddr2.setStatus("mandatory")
_SwhLogServerIPAddr3_Type = IpAddress
_SwhLogServerIPAddr3_Object = MibScalar
swhLogServerIPAddr3 = _SwhLogServerIPAddr3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 6),
    _SwhLogServerIPAddr3_Type()
)
swhLogServerIPAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLogServerIPAddr3.setStatus("mandatory")


class _SwhLogServerIPv6Addr1_Type(DisplayString):
    """Custom type swhLogServerIPv6Addr1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhLogServerIPv6Addr1_Type.__name__ = "DisplayString"
_SwhLogServerIPv6Addr1_Object = MibScalar
swhLogServerIPv6Addr1 = _SwhLogServerIPv6Addr1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 8),
    _SwhLogServerIPv6Addr1_Type()
)
swhLogServerIPv6Addr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLogServerIPv6Addr1.setStatus("mandatory")


class _SwhLogServerIPv6Addr2_Type(DisplayString):
    """Custom type swhLogServerIPv6Addr2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhLogServerIPv6Addr2_Type.__name__ = "DisplayString"
_SwhLogServerIPv6Addr2_Object = MibScalar
swhLogServerIPv6Addr2 = _SwhLogServerIPv6Addr2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 9),
    _SwhLogServerIPv6Addr2_Type()
)
swhLogServerIPv6Addr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLogServerIPv6Addr2.setStatus("mandatory")


class _SwhLogServerIPv6Addr3_Type(DisplayString):
    """Custom type swhLogServerIPv6Addr3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhLogServerIPv6Addr3_Type.__name__ = "DisplayString"
_SwhLogServerIPv6Addr3_Object = MibScalar
swhLogServerIPv6Addr3 = _SwhLogServerIPv6Addr3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 10),
    _SwhLogServerIPv6Addr3_Type()
)
swhLogServerIPv6Addr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLogServerIPv6Addr3.setStatus("mandatory")
_SwhLoggingType_ObjectIdentity = ObjectIdentity
swhLoggingType = _SwhLoggingType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 11)
)


class _SwhLoggingTypeTerminalHistory_Type(Integer32):
    """Custom type swhLoggingTypeTerminalHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLoggingTypeTerminalHistory_Type.__name__ = "Integer32"
_SwhLoggingTypeTerminalHistory_Object = MibScalar
swhLoggingTypeTerminalHistory = _SwhLoggingTypeTerminalHistory_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 8, 11, 1),
    _SwhLoggingTypeTerminalHistory_Type()
)
swhLoggingTypeTerminalHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoggingTypeTerminalHistory.setStatus("mandatory")
_SwhTimeRange_ObjectIdentity = ObjectIdentity
swhTimeRange = _SwhTimeRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10)
)
_SwhTimeRangeTable_Object = MibTable
swhTimeRangeTable = _SwhTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1)
)
if mibBuilder.loadTexts:
    swhTimeRangeTable.setStatus("mandatory")
_SwhTimeRangeEntry_Object = MibTableRow
swhTimeRangeEntry = _SwhTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1)
)
swhTimeRangeEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhTimeRangeIndex"),
)
if mibBuilder.loadTexts:
    swhTimeRangeEntry.setStatus("mandatory")


class _SwhTimeRangeIndex_Type(Integer32):
    """Custom type swhTimeRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhTimeRangeIndex_Type.__name__ = "Integer32"
_SwhTimeRangeIndex_Object = MibTableColumn
swhTimeRangeIndex = _SwhTimeRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 1),
    _SwhTimeRangeIndex_Type()
)
swhTimeRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhTimeRangeIndex.setStatus("mandatory")
_SwhTimeRangeName_Type = DisplayString
_SwhTimeRangeName_Object = MibTableColumn
swhTimeRangeName = _SwhTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 3),
    _SwhTimeRangeName_Type()
)
swhTimeRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeName.setStatus("mandatory")
_SwhTimeRangeAbsoluteStartHour_Type = DisplayString
_SwhTimeRangeAbsoluteStartHour_Object = MibTableColumn
swhTimeRangeAbsoluteStartHour = _SwhTimeRangeAbsoluteStartHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 4),
    _SwhTimeRangeAbsoluteStartHour_Type()
)
swhTimeRangeAbsoluteStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteStartHour.setStatus("mandatory")
_SwhTimeRangeAbsoluteStartMinute_Type = DisplayString
_SwhTimeRangeAbsoluteStartMinute_Object = MibTableColumn
swhTimeRangeAbsoluteStartMinute = _SwhTimeRangeAbsoluteStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 5),
    _SwhTimeRangeAbsoluteStartMinute_Type()
)
swhTimeRangeAbsoluteStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteStartMinute.setStatus("mandatory")
_SwhTimeRangeAbsoluteStartDate_Type = Integer32
_SwhTimeRangeAbsoluteStartDate_Object = MibTableColumn
swhTimeRangeAbsoluteStartDate = _SwhTimeRangeAbsoluteStartDate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 6),
    _SwhTimeRangeAbsoluteStartDate_Type()
)
swhTimeRangeAbsoluteStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteStartDate.setStatus("mandatory")


class _SwhTimeRangeAbsoluteStartMonth_Type(Integer32):
    """Custom type swhTimeRangeAbsoluteStartMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SwhTimeRangeAbsoluteStartMonth_Type.__name__ = "Integer32"
_SwhTimeRangeAbsoluteStartMonth_Object = MibTableColumn
swhTimeRangeAbsoluteStartMonth = _SwhTimeRangeAbsoluteStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 7),
    _SwhTimeRangeAbsoluteStartMonth_Type()
)
swhTimeRangeAbsoluteStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteStartMonth.setStatus("mandatory")
_SwhTimeRangeAbsoluteStartYear_Type = Integer32
_SwhTimeRangeAbsoluteStartYear_Object = MibTableColumn
swhTimeRangeAbsoluteStartYear = _SwhTimeRangeAbsoluteStartYear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 8),
    _SwhTimeRangeAbsoluteStartYear_Type()
)
swhTimeRangeAbsoluteStartYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteStartYear.setStatus("mandatory")


class _SwhTimeRangeAbsoluteStartReset_Type(Integer32):
    """Custom type swhTimeRangeAbsoluteStartReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_SwhTimeRangeAbsoluteStartReset_Type.__name__ = "Integer32"
_SwhTimeRangeAbsoluteStartReset_Object = MibTableColumn
swhTimeRangeAbsoluteStartReset = _SwhTimeRangeAbsoluteStartReset_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 9),
    _SwhTimeRangeAbsoluteStartReset_Type()
)
swhTimeRangeAbsoluteStartReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteStartReset.setStatus("mandatory")
_SwhTimeRangeAbsoluteEndHour_Type = DisplayString
_SwhTimeRangeAbsoluteEndHour_Object = MibTableColumn
swhTimeRangeAbsoluteEndHour = _SwhTimeRangeAbsoluteEndHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 10),
    _SwhTimeRangeAbsoluteEndHour_Type()
)
swhTimeRangeAbsoluteEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteEndHour.setStatus("mandatory")
_SwhTimeRangeAbsoluteEndMinute_Type = DisplayString
_SwhTimeRangeAbsoluteEndMinute_Object = MibTableColumn
swhTimeRangeAbsoluteEndMinute = _SwhTimeRangeAbsoluteEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 11),
    _SwhTimeRangeAbsoluteEndMinute_Type()
)
swhTimeRangeAbsoluteEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteEndMinute.setStatus("mandatory")
_SwhTimeRangeAbsoluteEndDate_Type = Integer32
_SwhTimeRangeAbsoluteEndDate_Object = MibTableColumn
swhTimeRangeAbsoluteEndDate = _SwhTimeRangeAbsoluteEndDate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 12),
    _SwhTimeRangeAbsoluteEndDate_Type()
)
swhTimeRangeAbsoluteEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteEndDate.setStatus("mandatory")


class _SwhTimeRangeAbsoluteEndMonth_Type(Integer32):
    """Custom type swhTimeRangeAbsoluteEndMonth based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("jan", 1),
          ("feb", 2),
          ("mar", 3),
          ("apr", 4),
          ("may", 5),
          ("jun", 6),
          ("jul", 7),
          ("aug", 8),
          ("sep", 9),
          ("oct", 10),
          ("nov", 11),
          ("dec", 12))
    )


_SwhTimeRangeAbsoluteEndMonth_Type.__name__ = "Integer32"
_SwhTimeRangeAbsoluteEndMonth_Object = MibTableColumn
swhTimeRangeAbsoluteEndMonth = _SwhTimeRangeAbsoluteEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 13),
    _SwhTimeRangeAbsoluteEndMonth_Type()
)
swhTimeRangeAbsoluteEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteEndMonth.setStatus("mandatory")
_SwhTimeRangeAbsoluteEndYear_Type = Integer32
_SwhTimeRangeAbsoluteEndYear_Object = MibTableColumn
swhTimeRangeAbsoluteEndYear = _SwhTimeRangeAbsoluteEndYear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 14),
    _SwhTimeRangeAbsoluteEndYear_Type()
)
swhTimeRangeAbsoluteEndYear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteEndYear.setStatus("mandatory")


class _SwhTimeRangeAbsoluteEndReset_Type(Integer32):
    """Custom type swhTimeRangeAbsoluteEndReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_SwhTimeRangeAbsoluteEndReset_Type.__name__ = "Integer32"
_SwhTimeRangeAbsoluteEndReset_Object = MibTableColumn
swhTimeRangeAbsoluteEndReset = _SwhTimeRangeAbsoluteEndReset_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 15),
    _SwhTimeRangeAbsoluteEndReset_Type()
)
swhTimeRangeAbsoluteEndReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeAbsoluteEndReset.setStatus("mandatory")
_SwhTimeRangePeriodic1StartHour_Type = DisplayString
_SwhTimeRangePeriodic1StartHour_Object = MibTableColumn
swhTimeRangePeriodic1StartHour = _SwhTimeRangePeriodic1StartHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 16),
    _SwhTimeRangePeriodic1StartHour_Type()
)
swhTimeRangePeriodic1StartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic1StartHour.setStatus("mandatory")
_SwhTimeRangePeriodic1StartMinute_Type = DisplayString
_SwhTimeRangePeriodic1StartMinute_Object = MibTableColumn
swhTimeRangePeriodic1StartMinute = _SwhTimeRangePeriodic1StartMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 17),
    _SwhTimeRangePeriodic1StartMinute_Type()
)
swhTimeRangePeriodic1StartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic1StartMinute.setStatus("mandatory")


class _SwhTimeRangePeriodic1StartDay_Type(Integer32):
    """Custom type swhTimeRangePeriodic1StartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sun", 0),
          ("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6))
    )


_SwhTimeRangePeriodic1StartDay_Type.__name__ = "Integer32"
_SwhTimeRangePeriodic1StartDay_Object = MibTableColumn
swhTimeRangePeriodic1StartDay = _SwhTimeRangePeriodic1StartDay_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 18),
    _SwhTimeRangePeriodic1StartDay_Type()
)
swhTimeRangePeriodic1StartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic1StartDay.setStatus("mandatory")
_SwhTimeRangePeriodic1EndHour_Type = DisplayString
_SwhTimeRangePeriodic1EndHour_Object = MibTableColumn
swhTimeRangePeriodic1EndHour = _SwhTimeRangePeriodic1EndHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 19),
    _SwhTimeRangePeriodic1EndHour_Type()
)
swhTimeRangePeriodic1EndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic1EndHour.setStatus("mandatory")
_SwhTimeRangePeriodic1EndMinute_Type = DisplayString
_SwhTimeRangePeriodic1EndMinute_Object = MibTableColumn
swhTimeRangePeriodic1EndMinute = _SwhTimeRangePeriodic1EndMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 20),
    _SwhTimeRangePeriodic1EndMinute_Type()
)
swhTimeRangePeriodic1EndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic1EndMinute.setStatus("mandatory")


class _SwhTimeRangePeriodic1EndDay_Type(Integer32):
    """Custom type swhTimeRangePeriodic1EndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sun", 0),
          ("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6))
    )


_SwhTimeRangePeriodic1EndDay_Type.__name__ = "Integer32"
_SwhTimeRangePeriodic1EndDay_Object = MibTableColumn
swhTimeRangePeriodic1EndDay = _SwhTimeRangePeriodic1EndDay_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 21),
    _SwhTimeRangePeriodic1EndDay_Type()
)
swhTimeRangePeriodic1EndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic1EndDay.setStatus("mandatory")


class _SwhTimeRangePeriodic1Delete_Type(Integer32):
    """Custom type swhTimeRangePeriodic1Delete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhTimeRangePeriodic1Delete_Type.__name__ = "Integer32"
_SwhTimeRangePeriodic1Delete_Object = MibTableColumn
swhTimeRangePeriodic1Delete = _SwhTimeRangePeriodic1Delete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 22),
    _SwhTimeRangePeriodic1Delete_Type()
)
swhTimeRangePeriodic1Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic1Delete.setStatus("mandatory")
_SwhTimeRangePeriodic2StartHour_Type = DisplayString
_SwhTimeRangePeriodic2StartHour_Object = MibTableColumn
swhTimeRangePeriodic2StartHour = _SwhTimeRangePeriodic2StartHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 23),
    _SwhTimeRangePeriodic2StartHour_Type()
)
swhTimeRangePeriodic2StartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic2StartHour.setStatus("mandatory")
_SwhTimeRangePeriodic2StartMinute_Type = DisplayString
_SwhTimeRangePeriodic2StartMinute_Object = MibTableColumn
swhTimeRangePeriodic2StartMinute = _SwhTimeRangePeriodic2StartMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 24),
    _SwhTimeRangePeriodic2StartMinute_Type()
)
swhTimeRangePeriodic2StartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic2StartMinute.setStatus("mandatory")


class _SwhTimeRangePeriodic2StartDay_Type(Integer32):
    """Custom type swhTimeRangePeriodic2StartDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sun", 0),
          ("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6))
    )


_SwhTimeRangePeriodic2StartDay_Type.__name__ = "Integer32"
_SwhTimeRangePeriodic2StartDay_Object = MibTableColumn
swhTimeRangePeriodic2StartDay = _SwhTimeRangePeriodic2StartDay_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 25),
    _SwhTimeRangePeriodic2StartDay_Type()
)
swhTimeRangePeriodic2StartDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic2StartDay.setStatus("mandatory")
_SwhTimeRangePeriodic2EndHour_Type = DisplayString
_SwhTimeRangePeriodic2EndHour_Object = MibTableColumn
swhTimeRangePeriodic2EndHour = _SwhTimeRangePeriodic2EndHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 26),
    _SwhTimeRangePeriodic2EndHour_Type()
)
swhTimeRangePeriodic2EndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic2EndHour.setStatus("mandatory")
_SwhTimeRangePeriodic2EndMinute_Type = DisplayString
_SwhTimeRangePeriodic2EndMinute_Object = MibTableColumn
swhTimeRangePeriodic2EndMinute = _SwhTimeRangePeriodic2EndMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 27),
    _SwhTimeRangePeriodic2EndMinute_Type()
)
swhTimeRangePeriodic2EndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic2EndMinute.setStatus("mandatory")


class _SwhTimeRangePeriodic2EndDay_Type(Integer32):
    """Custom type swhTimeRangePeriodic2EndDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("sun", 0),
          ("mon", 1),
          ("tue", 2),
          ("wed", 3),
          ("thu", 4),
          ("fri", 5),
          ("sat", 6))
    )


_SwhTimeRangePeriodic2EndDay_Type.__name__ = "Integer32"
_SwhTimeRangePeriodic2EndDay_Object = MibTableColumn
swhTimeRangePeriodic2EndDay = _SwhTimeRangePeriodic2EndDay_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 28),
    _SwhTimeRangePeriodic2EndDay_Type()
)
swhTimeRangePeriodic2EndDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic2EndDay.setStatus("mandatory")


class _SwhTimeRangePeriodic2Delete_Type(Integer32):
    """Custom type swhTimeRangePeriodic2Delete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhTimeRangePeriodic2Delete_Type.__name__ = "Integer32"
_SwhTimeRangePeriodic2Delete_Object = MibTableColumn
swhTimeRangePeriodic2Delete = _SwhTimeRangePeriodic2Delete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 29),
    _SwhTimeRangePeriodic2Delete_Type()
)
swhTimeRangePeriodic2Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodic2Delete.setStatus("mandatory")
_SwhTimeRangePeriodicList1StartHour_Type = DisplayString
_SwhTimeRangePeriodicList1StartHour_Object = MibTableColumn
swhTimeRangePeriodicList1StartHour = _SwhTimeRangePeriodicList1StartHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 30),
    _SwhTimeRangePeriodicList1StartHour_Type()
)
swhTimeRangePeriodicList1StartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1StartHour.setStatus("mandatory")
_SwhTimeRangePeriodicList1StartMinute_Type = DisplayString
_SwhTimeRangePeriodicList1StartMinute_Object = MibTableColumn
swhTimeRangePeriodicList1StartMinute = _SwhTimeRangePeriodicList1StartMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 31),
    _SwhTimeRangePeriodicList1StartMinute_Type()
)
swhTimeRangePeriodicList1StartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1StartMinute.setStatus("mandatory")
_SwhTimeRangePeriodicList1EndHour_Type = DisplayString
_SwhTimeRangePeriodicList1EndHour_Object = MibTableColumn
swhTimeRangePeriodicList1EndHour = _SwhTimeRangePeriodicList1EndHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 32),
    _SwhTimeRangePeriodicList1EndHour_Type()
)
swhTimeRangePeriodicList1EndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1EndHour.setStatus("mandatory")
_SwhTimeRangePeriodicList1EndMinute_Type = DisplayString
_SwhTimeRangePeriodicList1EndMinute_Object = MibTableColumn
swhTimeRangePeriodicList1EndMinute = _SwhTimeRangePeriodicList1EndMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 33),
    _SwhTimeRangePeriodicList1EndMinute_Type()
)
swhTimeRangePeriodicList1EndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1EndMinute.setStatus("mandatory")


class _SwhTimeRangePeriodicList1Sun_Type(Integer32):
    """Custom type swhTimeRangePeriodicList1Sun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList1Sun_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList1Sun_Object = MibTableColumn
swhTimeRangePeriodicList1Sun = _SwhTimeRangePeriodicList1Sun_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 34),
    _SwhTimeRangePeriodicList1Sun_Type()
)
swhTimeRangePeriodicList1Sun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1Sun.setStatus("mandatory")


class _SwhTimeRangePeriodicList1Mon_Type(Integer32):
    """Custom type swhTimeRangePeriodicList1Mon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList1Mon_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList1Mon_Object = MibTableColumn
swhTimeRangePeriodicList1Mon = _SwhTimeRangePeriodicList1Mon_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 35),
    _SwhTimeRangePeriodicList1Mon_Type()
)
swhTimeRangePeriodicList1Mon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1Mon.setStatus("mandatory")


class _SwhTimeRangePeriodicList1Tue_Type(Integer32):
    """Custom type swhTimeRangePeriodicList1Tue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList1Tue_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList1Tue_Object = MibTableColumn
swhTimeRangePeriodicList1Tue = _SwhTimeRangePeriodicList1Tue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 36),
    _SwhTimeRangePeriodicList1Tue_Type()
)
swhTimeRangePeriodicList1Tue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1Tue.setStatus("mandatory")


class _SwhTimeRangePeriodicList1Wed_Type(Integer32):
    """Custom type swhTimeRangePeriodicList1Wed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList1Wed_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList1Wed_Object = MibTableColumn
swhTimeRangePeriodicList1Wed = _SwhTimeRangePeriodicList1Wed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 37),
    _SwhTimeRangePeriodicList1Wed_Type()
)
swhTimeRangePeriodicList1Wed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1Wed.setStatus("mandatory")


class _SwhTimeRangePeriodicList1Thr_Type(Integer32):
    """Custom type swhTimeRangePeriodicList1Thr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList1Thr_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList1Thr_Object = MibTableColumn
swhTimeRangePeriodicList1Thr = _SwhTimeRangePeriodicList1Thr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 38),
    _SwhTimeRangePeriodicList1Thr_Type()
)
swhTimeRangePeriodicList1Thr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1Thr.setStatus("mandatory")


class _SwhTimeRangePeriodicList1Fri_Type(Integer32):
    """Custom type swhTimeRangePeriodicList1Fri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList1Fri_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList1Fri_Object = MibTableColumn
swhTimeRangePeriodicList1Fri = _SwhTimeRangePeriodicList1Fri_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 39),
    _SwhTimeRangePeriodicList1Fri_Type()
)
swhTimeRangePeriodicList1Fri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1Fri.setStatus("mandatory")


class _SwhTimeRangePeriodicList1Sat_Type(Integer32):
    """Custom type swhTimeRangePeriodicList1Sat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList1Sat_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList1Sat_Object = MibTableColumn
swhTimeRangePeriodicList1Sat = _SwhTimeRangePeriodicList1Sat_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 40),
    _SwhTimeRangePeriodicList1Sat_Type()
)
swhTimeRangePeriodicList1Sat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1Sat.setStatus("mandatory")


class _SwhTimeRangePeriodicList1Delete_Type(Integer32):
    """Custom type swhTimeRangePeriodicList1Delete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhTimeRangePeriodicList1Delete_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList1Delete_Object = MibTableColumn
swhTimeRangePeriodicList1Delete = _SwhTimeRangePeriodicList1Delete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 41),
    _SwhTimeRangePeriodicList1Delete_Type()
)
swhTimeRangePeriodicList1Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList1Delete.setStatus("mandatory")
_SwhTimeRangePeriodicList2StartHour_Type = DisplayString
_SwhTimeRangePeriodicList2StartHour_Object = MibTableColumn
swhTimeRangePeriodicList2StartHour = _SwhTimeRangePeriodicList2StartHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 42),
    _SwhTimeRangePeriodicList2StartHour_Type()
)
swhTimeRangePeriodicList2StartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2StartHour.setStatus("mandatory")
_SwhTimeRangePeriodicList2StartMinute_Type = DisplayString
_SwhTimeRangePeriodicList2StartMinute_Object = MibTableColumn
swhTimeRangePeriodicList2StartMinute = _SwhTimeRangePeriodicList2StartMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 43),
    _SwhTimeRangePeriodicList2StartMinute_Type()
)
swhTimeRangePeriodicList2StartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2StartMinute.setStatus("mandatory")
_SwhTimeRangePeriodicList2EndHour_Type = DisplayString
_SwhTimeRangePeriodicList2EndHour_Object = MibTableColumn
swhTimeRangePeriodicList2EndHour = _SwhTimeRangePeriodicList2EndHour_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 44),
    _SwhTimeRangePeriodicList2EndHour_Type()
)
swhTimeRangePeriodicList2EndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2EndHour.setStatus("mandatory")
_SwhTimeRangePeriodicList2EndMinute_Type = DisplayString
_SwhTimeRangePeriodicList2EndMinute_Object = MibTableColumn
swhTimeRangePeriodicList2EndMinute = _SwhTimeRangePeriodicList2EndMinute_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 45),
    _SwhTimeRangePeriodicList2EndMinute_Type()
)
swhTimeRangePeriodicList2EndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2EndMinute.setStatus("mandatory")


class _SwhTimeRangePeriodicList2Sun_Type(Integer32):
    """Custom type swhTimeRangePeriodicList2Sun based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList2Sun_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList2Sun_Object = MibTableColumn
swhTimeRangePeriodicList2Sun = _SwhTimeRangePeriodicList2Sun_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 46),
    _SwhTimeRangePeriodicList2Sun_Type()
)
swhTimeRangePeriodicList2Sun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2Sun.setStatus("mandatory")


class _SwhTimeRangePeriodicList2Mon_Type(Integer32):
    """Custom type swhTimeRangePeriodicList2Mon based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList2Mon_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList2Mon_Object = MibTableColumn
swhTimeRangePeriodicList2Mon = _SwhTimeRangePeriodicList2Mon_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 47),
    _SwhTimeRangePeriodicList2Mon_Type()
)
swhTimeRangePeriodicList2Mon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2Mon.setStatus("mandatory")


class _SwhTimeRangePeriodicList2Tue_Type(Integer32):
    """Custom type swhTimeRangePeriodicList2Tue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList2Tue_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList2Tue_Object = MibTableColumn
swhTimeRangePeriodicList2Tue = _SwhTimeRangePeriodicList2Tue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 48),
    _SwhTimeRangePeriodicList2Tue_Type()
)
swhTimeRangePeriodicList2Tue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2Tue.setStatus("mandatory")


class _SwhTimeRangePeriodicList2Wed_Type(Integer32):
    """Custom type swhTimeRangePeriodicList2Wed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList2Wed_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList2Wed_Object = MibTableColumn
swhTimeRangePeriodicList2Wed = _SwhTimeRangePeriodicList2Wed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 49),
    _SwhTimeRangePeriodicList2Wed_Type()
)
swhTimeRangePeriodicList2Wed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2Wed.setStatus("mandatory")


class _SwhTimeRangePeriodicList2Thr_Type(Integer32):
    """Custom type swhTimeRangePeriodicList2Thr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList2Thr_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList2Thr_Object = MibTableColumn
swhTimeRangePeriodicList2Thr = _SwhTimeRangePeriodicList2Thr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 50),
    _SwhTimeRangePeriodicList2Thr_Type()
)
swhTimeRangePeriodicList2Thr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2Thr.setStatus("mandatory")


class _SwhTimeRangePeriodicList2Fri_Type(Integer32):
    """Custom type swhTimeRangePeriodicList2Fri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList2Fri_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList2Fri_Object = MibTableColumn
swhTimeRangePeriodicList2Fri = _SwhTimeRangePeriodicList2Fri_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 51),
    _SwhTimeRangePeriodicList2Fri_Type()
)
swhTimeRangePeriodicList2Fri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2Fri.setStatus("mandatory")


class _SwhTimeRangePeriodicList2Sat_Type(Integer32):
    """Custom type swhTimeRangePeriodicList2Sat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhTimeRangePeriodicList2Sat_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList2Sat_Object = MibTableColumn
swhTimeRangePeriodicList2Sat = _SwhTimeRangePeriodicList2Sat_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 52),
    _SwhTimeRangePeriodicList2Sat_Type()
)
swhTimeRangePeriodicList2Sat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2Sat.setStatus("mandatory")


class _SwhTimeRangePeriodicList2Delete_Type(Integer32):
    """Custom type swhTimeRangePeriodicList2Delete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhTimeRangePeriodicList2Delete_Type.__name__ = "Integer32"
_SwhTimeRangePeriodicList2Delete_Object = MibTableColumn
swhTimeRangePeriodicList2Delete = _SwhTimeRangePeriodicList2Delete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 53),
    _SwhTimeRangePeriodicList2Delete_Type()
)
swhTimeRangePeriodicList2Delete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangePeriodicList2Delete.setStatus("mandatory")


class _SwhTimeRangeDelete_Type(Integer32):
    """Custom type swhTimeRangeDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhTimeRangeDelete_Type.__name__ = "Integer32"
_SwhTimeRangeDelete_Object = MibTableColumn
swhTimeRangeDelete = _SwhTimeRangeDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 3, 10, 1, 1, 56),
    _SwhTimeRangeDelete_Type()
)
swhTimeRangeDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTimeRangeDelete.setStatus("mandatory")
_SwhSwitchManagement_ObjectIdentity = ObjectIdentity
swhSwitchManagement = _SwhSwitchManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4)
)
_SwhSwitchConfiguration_ObjectIdentity = ObjectIdentity
swhSwitchConfiguration = _SwhSwitchConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 1)
)


class _SwhSwitchMaxFrameSize_Type(Integer32):
    """Custom type swhSwitchMaxFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1518, 9600),
    )


_SwhSwitchMaxFrameSize_Type.__name__ = "Integer32"
_SwhSwitchMaxFrameSize_Object = MibScalar
swhSwitchMaxFrameSize = _SwhSwitchMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 1, 1),
    _SwhSwitchMaxFrameSize_Type()
)
swhSwitchMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSwitchMaxFrameSize.setStatus("mandatory")


class _SwhSwitchAgingTime_Type(Integer32):
    """Custom type swhSwitchAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 77925),
    )


_SwhSwitchAgingTime_Type.__name__ = "Integer32"
_SwhSwitchAgingTime_Object = MibScalar
swhSwitchAgingTime = _SwhSwitchAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 1, 3),
    _SwhSwitchAgingTime_Type()
)
swhSwitchAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSwitchAgingTime.setStatus("mandatory")


class _SwhSwitch0180C2000000to0F_Type(Integer32):
    """Custom type swhSwitch0180C2000000to0F based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-filter", 0),
          ("filter", 1))
    )


_SwhSwitch0180C2000000to0F_Type.__name__ = "Integer32"
_SwhSwitch0180C2000000to0F_Object = MibScalar
swhSwitch0180C2000000to0F = _SwhSwitch0180C2000000to0F_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 1, 9),
    _SwhSwitch0180C2000000to0F_Type()
)
swhSwitch0180C2000000to0F.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSwitch0180C2000000to0F.setStatus("mandatory")


class _SwhSwitch0180C2000020to2F_Type(Integer32):
    """Custom type swhSwitch0180C2000020to2F based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-filter", 0),
          ("filter", 1))
    )


_SwhSwitch0180C2000020to2F_Type.__name__ = "Integer32"
_SwhSwitch0180C2000020to2F_Object = MibScalar
swhSwitch0180C2000020to2F = _SwhSwitch0180C2000020to2F_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 1, 10),
    _SwhSwitch0180C2000020to2F_Type()
)
swhSwitch0180C2000020to2F.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSwitch0180C2000020to2F.setStatus("mandatory")


class _SwhSwitch0180C2000010_Type(Integer32):
    """Custom type swhSwitch0180C2000010 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-filter", 0),
          ("filter", 1))
    )


_SwhSwitch0180C2000010_Type.__name__ = "Integer32"
_SwhSwitch0180C2000010_Object = MibScalar
swhSwitch0180C2000010 = _SwhSwitch0180C2000010_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 1, 11),
    _SwhSwitch0180C2000010_Type()
)
swhSwitch0180C2000010.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSwitch0180C2000010.setStatus("mandatory")
_SwhSwitchStatisticsPollingPort_Type = Integer32
_SwhSwitchStatisticsPollingPort_Object = MibScalar
swhSwitchStatisticsPollingPort = _SwhSwitchStatisticsPollingPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 1, 54),
    _SwhSwitchStatisticsPollingPort_Type()
)
swhSwitchStatisticsPollingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSwitchStatisticsPollingPort.setStatus("mandatory")
_SwhSwitchStatisticsPollingInterval_Type = Integer32
_SwhSwitchStatisticsPollingInterval_Object = MibScalar
swhSwitchStatisticsPollingInterval = _SwhSwitchStatisticsPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 1, 55),
    _SwhSwitchStatisticsPollingInterval_Type()
)
swhSwitchStatisticsPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSwitchStatisticsPollingInterval.setStatus("mandatory")
_SwhPortConfiguration_ObjectIdentity = ObjectIdentity
swhPortConfiguration = _SwhPortConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2)
)
_SwhPortConfigTable_Object = MibTable
swhPortConfigTable = _SwhPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1)
)
if mibBuilder.loadTexts:
    swhPortConfigTable.setStatus("mandatory")
_SwhPortConfigEntry_Object = MibTableRow
swhPortConfigEntry = _SwhPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1)
)
swhPortConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhPortConfigIndex"),
)
if mibBuilder.loadTexts:
    swhPortConfigEntry.setStatus("mandatory")


class _SwhPortConfigIndex_Type(Integer32):
    """Custom type swhPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhPortConfigIndex_Type.__name__ = "Integer32"
_SwhPortConfigIndex_Object = MibTableColumn
swhPortConfigIndex = _SwhPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1, 1),
    _SwhPortConfigIndex_Type()
)
swhPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhPortConfigIndex.setStatus("mandatory")


class _SwhPortConfigState_Type(Integer32):
    """Custom type swhPortConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhPortConfigState_Type.__name__ = "Integer32"
_SwhPortConfigState_Object = MibTableColumn
swhPortConfigState = _SwhPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1, 2),
    _SwhPortConfigState_Type()
)
swhPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortConfigState.setStatus("mandatory")


class _SwhPortConfigType_Type(Integer32):
    """Custom type swhPortConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiation", 0),
          ("manual", 1))
    )


_SwhPortConfigType_Type.__name__ = "Integer32"
_SwhPortConfigType_Object = MibTableColumn
swhPortConfigType = _SwhPortConfigType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1, 3),
    _SwhPortConfigType_Type()
)
swhPortConfigType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortConfigType.setStatus("mandatory")


class _SwhPortConfigSpeed_Type(Integer32):
    """Custom type swhPortConfigSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("speed-10M", 0),
          ("speed-100M", 1),
          ("speed-1000M", 2))
    )


_SwhPortConfigSpeed_Type.__name__ = "Integer32"
_SwhPortConfigSpeed_Object = MibTableColumn
swhPortConfigSpeed = _SwhPortConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1, 4),
    _SwhPortConfigSpeed_Type()
)
swhPortConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortConfigSpeed.setStatus("mandatory")


class _SwhPortConfigDuplex_Type(Integer32):
    """Custom type swhPortConfigDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("halfDuplex", 0),
          ("fullDuplex", 1))
    )


_SwhPortConfigDuplex_Type.__name__ = "Integer32"
_SwhPortConfigDuplex_Object = MibTableColumn
swhPortConfigDuplex = _SwhPortConfigDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1, 5),
    _SwhPortConfigDuplex_Type()
)
swhPortConfigDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortConfigDuplex.setStatus("mandatory")


class _SwhPortConfigFlowControl_Type(Integer32):
    """Custom type swhPortConfigFlowControl based on Integer32"""
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


_SwhPortConfigFlowControl_Type.__name__ = "Integer32"
_SwhPortConfigFlowControl_Object = MibTableColumn
swhPortConfigFlowControl = _SwhPortConfigFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1, 6),
    _SwhPortConfigFlowControl_Type()
)
swhPortConfigFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortConfigFlowControl.setStatus("mandatory")
_SwhPortConfigDescription_Type = DisplayString
_SwhPortConfigDescription_Object = MibTableColumn
swhPortConfigDescription = _SwhPortConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1, 7),
    _SwhPortConfigDescription_Type()
)
swhPortConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortConfigDescription.setStatus("mandatory")


class _SwhPortConfigMediaType_Type(Integer32):
    """Custom type swhPortConfigMediaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("copper", 0),
          ("fiber", 1))
    )


_SwhPortConfigMediaType_Type.__name__ = "Integer32"
_SwhPortConfigMediaType_Object = MibTableColumn
swhPortConfigMediaType = _SwhPortConfigMediaType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 2, 1, 1, 8),
    _SwhPortConfigMediaType_Type()
)
swhPortConfigMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortConfigMediaType.setStatus("mandatory")
_SwhVLANConfiguration_ObjectIdentity = ObjectIdentity
swhVLANConfiguration = _SwhVLANConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4)
)
_SwhPortVLANConfiguration_ObjectIdentity = ObjectIdentity
swhPortVLANConfiguration = _SwhPortVLANConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1)
)
_SwhPortVLANConfigTable_Object = MibTable
swhPortVLANConfigTable = _SwhPortVLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1)
)
if mibBuilder.loadTexts:
    swhPortVLANConfigTable.setStatus("mandatory")
_SwhPortVLANConfigEntry_Object = MibTableRow
swhPortVLANConfigEntry = _SwhPortVLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1)
)
swhPortVLANConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhPortVLANConfigIndex"),
)
if mibBuilder.loadTexts:
    swhPortVLANConfigEntry.setStatus("mandatory")


class _SwhPortVLANConfigIndex_Type(Integer32):
    """Custom type swhPortVLANConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhPortVLANConfigIndex_Type.__name__ = "Integer32"
_SwhPortVLANConfigIndex_Object = MibTableColumn
swhPortVLANConfigIndex = _SwhPortVLANConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 1),
    _SwhPortVLANConfigIndex_Type()
)
swhPortVLANConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhPortVLANConfigIndex.setStatus("mandatory")


class _SwhPortVLANConfigValid_Type(Integer32):
    """Custom type swhPortVLANConfigValid based on Integer32"""
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


_SwhPortVLANConfigValid_Type.__name__ = "Integer32"
_SwhPortVLANConfigValid_Object = MibTableColumn
swhPortVLANConfigValid = _SwhPortVLANConfigValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 2),
    _SwhPortVLANConfigValid_Type()
)
swhPortVLANConfigValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortVLANConfigValid.setStatus("mandatory")
_SwhPortVLANConfigName_Type = DisplayString
_SwhPortVLANConfigName_Object = MibTableColumn
swhPortVLANConfigName = _SwhPortVLANConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 4),
    _SwhPortVLANConfigName_Type()
)
swhPortVLANConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigName.setStatus("mandatory")


class _SwhPortVLANConfigPort1_Type(Integer32):
    """Custom type swhPortVLANConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortVLANConfigPort1_Type.__name__ = "Integer32"
_SwhPortVLANConfigPort1_Object = MibTableColumn
swhPortVLANConfigPort1 = _SwhPortVLANConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 5),
    _SwhPortVLANConfigPort1_Type()
)
swhPortVLANConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigPort1.setStatus("mandatory")


class _SwhPortVLANConfigPort2_Type(Integer32):
    """Custom type swhPortVLANConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortVLANConfigPort2_Type.__name__ = "Integer32"
_SwhPortVLANConfigPort2_Object = MibTableColumn
swhPortVLANConfigPort2 = _SwhPortVLANConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 6),
    _SwhPortVLANConfigPort2_Type()
)
swhPortVLANConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigPort2.setStatus("mandatory")


class _SwhPortVLANConfigPort3_Type(Integer32):
    """Custom type swhPortVLANConfigPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortVLANConfigPort3_Type.__name__ = "Integer32"
_SwhPortVLANConfigPort3_Object = MibTableColumn
swhPortVLANConfigPort3 = _SwhPortVLANConfigPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 7),
    _SwhPortVLANConfigPort3_Type()
)
swhPortVLANConfigPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigPort3.setStatus("mandatory")


class _SwhPortVLANConfigPort4_Type(Integer32):
    """Custom type swhPortVLANConfigPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortVLANConfigPort4_Type.__name__ = "Integer32"
_SwhPortVLANConfigPort4_Object = MibTableColumn
swhPortVLANConfigPort4 = _SwhPortVLANConfigPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 8),
    _SwhPortVLANConfigPort4_Type()
)
swhPortVLANConfigPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigPort4.setStatus("mandatory")


class _SwhPortVLANConfigPort5_Type(Integer32):
    """Custom type swhPortVLANConfigPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortVLANConfigPort5_Type.__name__ = "Integer32"
_SwhPortVLANConfigPort5_Object = MibTableColumn
swhPortVLANConfigPort5 = _SwhPortVLANConfigPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 9),
    _SwhPortVLANConfigPort5_Type()
)
swhPortVLANConfigPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigPort5.setStatus("mandatory")


class _SwhPortVLANConfigPort6_Type(Integer32):
    """Custom type swhPortVLANConfigPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortVLANConfigPort6_Type.__name__ = "Integer32"
_SwhPortVLANConfigPort6_Object = MibTableColumn
swhPortVLANConfigPort6 = _SwhPortVLANConfigPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 10),
    _SwhPortVLANConfigPort6_Type()
)
swhPortVLANConfigPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigPort6.setStatus("mandatory")


class _SwhPortVLANConfigCPU_Type(Integer32):
    """Custom type swhPortVLANConfigCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortVLANConfigCPU_Type.__name__ = "Integer32"
_SwhPortVLANConfigCPU_Object = MibTableColumn
swhPortVLANConfigCPU = _SwhPortVLANConfigCPU_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 55),
    _SwhPortVLANConfigCPU_Type()
)
swhPortVLANConfigCPU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigCPU.setStatus("mandatory")


class _SwhPortVLANConfigDelete_Type(Integer32):
    """Custom type swhPortVLANConfigDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhPortVLANConfigDelete_Type.__name__ = "Integer32"
_SwhPortVLANConfigDelete_Object = MibTableColumn
swhPortVLANConfigDelete = _SwhPortVLANConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 1, 1, 1, 56),
    _SwhPortVLANConfigDelete_Type()
)
swhPortVLANConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortVLANConfigDelete.setStatus("mandatory")
_Swh8021QVLANConfiguration_ObjectIdentity = ObjectIdentity
swh8021QVLANConfiguration = _Swh8021QVLANConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2)
)
_Swh8021QTrunkVLAN_ObjectIdentity = ObjectIdentity
swh8021QTrunkVLAN = _Swh8021QTrunkVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1)
)
_Swh8021QTrunkVLANTable_Object = MibTable
swh8021QTrunkVLANTable = _Swh8021QTrunkVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    swh8021QTrunkVLANTable.setStatus("mandatory")
_Swh8021QTrunkVLANEntry_Object = MibTableRow
swh8021QTrunkVLANEntry = _Swh8021QTrunkVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1)
)
swh8021QTrunkVLANEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swh8021QTrunkVLANIndex"),
)
if mibBuilder.loadTexts:
    swh8021QTrunkVLANEntry.setStatus("mandatory")


class _Swh8021QTrunkVLANIndex_Type(Integer32):
    """Custom type swh8021QTrunkVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Swh8021QTrunkVLANIndex_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANIndex_Object = MibTableColumn
swh8021QTrunkVLANIndex = _Swh8021QTrunkVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 1),
    _Swh8021QTrunkVLANIndex_Type()
)
swh8021QTrunkVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANIndex.setStatus("mandatory")


class _Swh8021QTrunkVLANValid_Type(Integer32):
    """Custom type swh8021QTrunkVLANValid based on Integer32"""
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


_Swh8021QTrunkVLANValid_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANValid_Object = MibTableColumn
swh8021QTrunkVLANValid = _Swh8021QTrunkVLANValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 2),
    _Swh8021QTrunkVLANValid_Type()
)
swh8021QTrunkVLANValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANValid.setStatus("mandatory")


class _Swh8021QTrunkVLANVID_Type(Integer32):
    """Custom type swh8021QTrunkVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Swh8021QTrunkVLANVID_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANVID_Object = MibTableColumn
swh8021QTrunkVLANVID = _Swh8021QTrunkVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 3),
    _Swh8021QTrunkVLANVID_Type()
)
swh8021QTrunkVLANVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANVID.setStatus("mandatory")
_Swh8021QTrunkVLANName_Type = DisplayString
_Swh8021QTrunkVLANName_Object = MibTableColumn
swh8021QTrunkVLANName = _Swh8021QTrunkVLANName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 4),
    _Swh8021QTrunkVLANName_Type()
)
swh8021QTrunkVLANName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANName.setStatus("mandatory")


class _Swh8021QTrunkVLANPort1_Type(Integer32):
    """Custom type swh8021QTrunkVLANPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QTrunkVLANPort1_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANPort1_Object = MibTableColumn
swh8021QTrunkVLANPort1 = _Swh8021QTrunkVLANPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 5),
    _Swh8021QTrunkVLANPort1_Type()
)
swh8021QTrunkVLANPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANPort1.setStatus("mandatory")


class _Swh8021QTrunkVLANPort2_Type(Integer32):
    """Custom type swh8021QTrunkVLANPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QTrunkVLANPort2_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANPort2_Object = MibTableColumn
swh8021QTrunkVLANPort2 = _Swh8021QTrunkVLANPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 6),
    _Swh8021QTrunkVLANPort2_Type()
)
swh8021QTrunkVLANPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANPort2.setStatus("mandatory")


class _Swh8021QTrunkVLANPort3_Type(Integer32):
    """Custom type swh8021QTrunkVLANPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QTrunkVLANPort3_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANPort3_Object = MibTableColumn
swh8021QTrunkVLANPort3 = _Swh8021QTrunkVLANPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 7),
    _Swh8021QTrunkVLANPort3_Type()
)
swh8021QTrunkVLANPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANPort3.setStatus("mandatory")


class _Swh8021QTrunkVLANPort4_Type(Integer32):
    """Custom type swh8021QTrunkVLANPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QTrunkVLANPort4_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANPort4_Object = MibTableColumn
swh8021QTrunkVLANPort4 = _Swh8021QTrunkVLANPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 8),
    _Swh8021QTrunkVLANPort4_Type()
)
swh8021QTrunkVLANPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANPort4.setStatus("mandatory")


class _Swh8021QTrunkVLANPort5_Type(Integer32):
    """Custom type swh8021QTrunkVLANPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QTrunkVLANPort5_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANPort5_Object = MibTableColumn
swh8021QTrunkVLANPort5 = _Swh8021QTrunkVLANPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 9),
    _Swh8021QTrunkVLANPort5_Type()
)
swh8021QTrunkVLANPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANPort5.setStatus("mandatory")


class _Swh8021QTrunkVLANPort6_Type(Integer32):
    """Custom type swh8021QTrunkVLANPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QTrunkVLANPort6_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANPort6_Object = MibTableColumn
swh8021QTrunkVLANPort6 = _Swh8021QTrunkVLANPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 10),
    _Swh8021QTrunkVLANPort6_Type()
)
swh8021QTrunkVLANPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANPort6.setStatus("mandatory")


class _Swh8021QTrunkVLANCPU_Type(Integer32):
    """Custom type swh8021QTrunkVLANCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QTrunkVLANCPU_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANCPU_Object = MibTableColumn
swh8021QTrunkVLANCPU = _Swh8021QTrunkVLANCPU_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 55),
    _Swh8021QTrunkVLANCPU_Type()
)
swh8021QTrunkVLANCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANCPU.setStatus("mandatory")


class _Swh8021QTrunkVLANDelete_Type(Integer32):
    """Custom type swh8021QTrunkVLANDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_Swh8021QTrunkVLANDelete_Type.__name__ = "Integer32"
_Swh8021QTrunkVLANDelete_Object = MibTableColumn
swh8021QTrunkVLANDelete = _Swh8021QTrunkVLANDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 1, 1, 1, 56),
    _Swh8021QTrunkVLANDelete_Type()
)
swh8021QTrunkVLANDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTrunkVLANDelete.setStatus("mandatory")
_Swh8021QPortVLANConfig_ObjectIdentity = ObjectIdentity
swh8021QPortVLANConfig = _Swh8021QPortVLANConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 2)
)
_Swh8021QPortVLANConfigTable_Object = MibTable
swh8021QPortVLANConfigTable = _Swh8021QPortVLANConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 2, 2)
)
if mibBuilder.loadTexts:
    swh8021QPortVLANConfigTable.setStatus("mandatory")
_Swh8021QPortVLANConfigEntry_Object = MibTableRow
swh8021QPortVLANConfigEntry = _Swh8021QPortVLANConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 2, 2, 1)
)
swh8021QPortVLANConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swh8021QPortIndex"),
)
if mibBuilder.loadTexts:
    swh8021QPortVLANConfigEntry.setStatus("mandatory")


class _Swh8021QPortIndex_Type(Integer32):
    """Custom type swh8021QPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Swh8021QPortIndex_Type.__name__ = "Integer32"
_Swh8021QPortIndex_Object = MibTableColumn
swh8021QPortIndex = _Swh8021QPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 2, 2, 1, 1),
    _Swh8021QPortIndex_Type()
)
swh8021QPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swh8021QPortIndex.setStatus("mandatory")


class _Swh8021QPortAccessVLAN_Type(Integer32):
    """Custom type swh8021QPortAccessVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Swh8021QPortAccessVLAN_Type.__name__ = "Integer32"
_Swh8021QPortAccessVLAN_Object = MibTableColumn
swh8021QPortAccessVLAN = _Swh8021QPortAccessVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 2, 2, 1, 2),
    _Swh8021QPortAccessVLAN_Type()
)
swh8021QPortAccessVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QPortAccessVLAN.setStatus("mandatory")


class _Swh8021QPortVLANMode_Type(Integer32):
    """Custom type swh8021QPortVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("trunk", 1),
          ("trunknative", 2),
          ("dot1qtunnel", 3))
    )


_Swh8021QPortVLANMode_Type.__name__ = "Integer32"
_Swh8021QPortVLANMode_Object = MibTableColumn
swh8021QPortVLANMode = _Swh8021QPortVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 2, 2, 1, 20),
    _Swh8021QPortVLANMode_Type()
)
swh8021QPortVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QPortVLANMode.setStatus("mandatory")
_Swh8021QPortTrunkVLAN_Type = DisplayString
_Swh8021QPortTrunkVLAN_Object = MibTableColumn
swh8021QPortTrunkVLAN = _Swh8021QPortTrunkVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 2, 2, 1, 25),
    _Swh8021QPortTrunkVLAN_Type()
)
swh8021QPortTrunkVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QPortTrunkVLAN.setStatus("mandatory")
_Swh8021QTunnelEtherType_Type = DisplayString
_Swh8021QTunnelEtherType_Object = MibScalar
swh8021QTunnelEtherType = _Swh8021QTunnelEtherType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 2, 14),
    _Swh8021QTunnelEtherType_Type()
)
swh8021QTunnelEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QTunnelEtherType.setStatus("mandatory")
_Swh8021QManagementVLANConfig_ObjectIdentity = ObjectIdentity
swh8021QManagementVLANConfig = _Swh8021QManagementVLANConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5)
)


class _Swh8021QManagementVLANConfigCPUVID_Type(Integer32):
    """Custom type swh8021QManagementVLANConfigCPUVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Swh8021QManagementVLANConfigCPUVID_Type.__name__ = "Integer32"
_Swh8021QManagementVLANConfigCPUVID_Object = MibScalar
swh8021QManagementVLANConfigCPUVID = _Swh8021QManagementVLANConfigCPUVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5, 1),
    _Swh8021QManagementVLANConfigCPUVID_Type()
)
swh8021QManagementVLANConfigCPUVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QManagementVLANConfigCPUVID.setStatus("mandatory")


class _Swh8021QManagementVLANConfigVLANMode_Type(Integer32):
    """Custom type swh8021QManagementVLANConfigVLANMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("trunk", 1),
          ("trunknative", 2))
    )


_Swh8021QManagementVLANConfigVLANMode_Type.__name__ = "Integer32"
_Swh8021QManagementVLANConfigVLANMode_Object = MibScalar
swh8021QManagementVLANConfigVLANMode = _Swh8021QManagementVLANConfigVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5, 3),
    _Swh8021QManagementVLANConfigVLANMode_Type()
)
swh8021QManagementVLANConfigVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QManagementVLANConfigVLANMode.setStatus("mandatory")


class _Swh8021QManagementVLANConfigPort1_Type(Integer32):
    """Custom type swh8021QManagementVLANConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QManagementVLANConfigPort1_Type.__name__ = "Integer32"
_Swh8021QManagementVLANConfigPort1_Object = MibScalar
swh8021QManagementVLANConfigPort1 = _Swh8021QManagementVLANConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5, 5),
    _Swh8021QManagementVLANConfigPort1_Type()
)
swh8021QManagementVLANConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QManagementVLANConfigPort1.setStatus("mandatory")


class _Swh8021QManagementVLANConfigPort2_Type(Integer32):
    """Custom type swh8021QManagementVLANConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QManagementVLANConfigPort2_Type.__name__ = "Integer32"
_Swh8021QManagementVLANConfigPort2_Object = MibScalar
swh8021QManagementVLANConfigPort2 = _Swh8021QManagementVLANConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5, 6),
    _Swh8021QManagementVLANConfigPort2_Type()
)
swh8021QManagementVLANConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QManagementVLANConfigPort2.setStatus("mandatory")


class _Swh8021QManagementVLANConfigPort3_Type(Integer32):
    """Custom type swh8021QManagementVLANConfigPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QManagementVLANConfigPort3_Type.__name__ = "Integer32"
_Swh8021QManagementVLANConfigPort3_Object = MibScalar
swh8021QManagementVLANConfigPort3 = _Swh8021QManagementVLANConfigPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5, 7),
    _Swh8021QManagementVLANConfigPort3_Type()
)
swh8021QManagementVLANConfigPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QManagementVLANConfigPort3.setStatus("mandatory")


class _Swh8021QManagementVLANConfigPort4_Type(Integer32):
    """Custom type swh8021QManagementVLANConfigPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QManagementVLANConfigPort4_Type.__name__ = "Integer32"
_Swh8021QManagementVLANConfigPort4_Object = MibScalar
swh8021QManagementVLANConfigPort4 = _Swh8021QManagementVLANConfigPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5, 8),
    _Swh8021QManagementVLANConfigPort4_Type()
)
swh8021QManagementVLANConfigPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QManagementVLANConfigPort4.setStatus("mandatory")


class _Swh8021QManagementVLANConfigPort5_Type(Integer32):
    """Custom type swh8021QManagementVLANConfigPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QManagementVLANConfigPort5_Type.__name__ = "Integer32"
_Swh8021QManagementVLANConfigPort5_Object = MibScalar
swh8021QManagementVLANConfigPort5 = _Swh8021QManagementVLANConfigPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5, 9),
    _Swh8021QManagementVLANConfigPort5_Type()
)
swh8021QManagementVLANConfigPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QManagementVLANConfigPort5.setStatus("mandatory")


class _Swh8021QManagementVLANConfigPort6_Type(Integer32):
    """Custom type swh8021QManagementVLANConfigPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QManagementVLANConfigPort6_Type.__name__ = "Integer32"
_Swh8021QManagementVLANConfigPort6_Object = MibScalar
swh8021QManagementVLANConfigPort6 = _Swh8021QManagementVLANConfigPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 2, 5, 10),
    _Swh8021QManagementVLANConfigPort6_Type()
)
swh8021QManagementVLANConfigPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021QManagementVLANConfigPort6.setStatus("mandatory")
_SwhVLANTranslationConfiguration_ObjectIdentity = ObjectIdentity
swhVLANTranslationConfiguration = _SwhVLANTranslationConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7)
)


class _SwhVLANTranslationConfigVLANTranslation_Type(Integer32):
    """Custom type swhVLANTranslationConfigVLANTranslation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhVLANTranslationConfigVLANTranslation_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigVLANTranslation_Object = MibScalar
swhVLANTranslationConfigVLANTranslation = _SwhVLANTranslationConfigVLANTranslation_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 1),
    _SwhVLANTranslationConfigVLANTranslation_Type()
)
swhVLANTranslationConfigVLANTranslation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigVLANTranslation.setStatus("mandatory")


class _SwhVLANTranslationConfigVLANTranslationDeleteAll_Type(Integer32):
    """Custom type swhVLANTranslationConfigVLANTranslationDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhVLANTranslationConfigVLANTranslationDeleteAll_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigVLANTranslationDeleteAll_Object = MibScalar
swhVLANTranslationConfigVLANTranslationDeleteAll = _SwhVLANTranslationConfigVLANTranslationDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 2),
    _SwhVLANTranslationConfigVLANTranslationDeleteAll_Type()
)
swhVLANTranslationConfigVLANTranslationDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigVLANTranslationDeleteAll.setStatus("mandatory")
_SwhVLANTranslationConfigTable_Object = MibTable
swhVLANTranslationConfigTable = _SwhVLANTranslationConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5)
)
if mibBuilder.loadTexts:
    swhVLANTranslationConfigTable.setStatus("mandatory")
_SwhVLANTranslationConfigEntry_Object = MibTableRow
swhVLANTranslationConfigEntry = _SwhVLANTranslationConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1)
)
swhVLANTranslationConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhVLANTranslationConfigIndex"),
)
if mibBuilder.loadTexts:
    swhVLANTranslationConfigEntry.setStatus("mandatory")


class _SwhVLANTranslationConfigIndex_Type(Integer32):
    """Custom type swhVLANTranslationConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhVLANTranslationConfigIndex_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigIndex_Object = MibTableColumn
swhVLANTranslationConfigIndex = _SwhVLANTranslationConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1, 1),
    _SwhVLANTranslationConfigIndex_Type()
)
swhVLANTranslationConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigIndex.setStatus("mandatory")


class _SwhVLANTranslationConfigValid_Type(Integer32):
    """Custom type swhVLANTranslationConfigValid based on Integer32"""
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


_SwhVLANTranslationConfigValid_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigValid_Object = MibTableColumn
swhVLANTranslationConfigValid = _SwhVLANTranslationConfigValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1, 2),
    _SwhVLANTranslationConfigValid_Type()
)
swhVLANTranslationConfigValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigValid.setStatus("mandatory")
_SwhVLANTranslationConfigName_Type = DisplayString
_SwhVLANTranslationConfigName_Object = MibTableColumn
swhVLANTranslationConfigName = _SwhVLANTranslationConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1, 4),
    _SwhVLANTranslationConfigName_Type()
)
swhVLANTranslationConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigName.setStatus("mandatory")


class _SwhVLANTranslationConfigPort_Type(Integer32):
    """Custom type swhVLANTranslationConfigPort based on Integer32"""
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
        *(("port01", 0),
          ("port02", 1),
          ("port03", 2),
          ("port04", 3),
          ("port05", 4),
          ("port06", 5))
    )


_SwhVLANTranslationConfigPort_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigPort_Object = MibTableColumn
swhVLANTranslationConfigPort = _SwhVLANTranslationConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1, 5),
    _SwhVLANTranslationConfigPort_Type()
)
swhVLANTranslationConfigPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigPort.setStatus("mandatory")


class _SwhVLANTranslationConfigOriginalVID_Type(Integer32):
    """Custom type swhVLANTranslationConfigOriginalVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwhVLANTranslationConfigOriginalVID_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigOriginalVID_Object = MibTableColumn
swhVLANTranslationConfigOriginalVID = _SwhVLANTranslationConfigOriginalVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1, 6),
    _SwhVLANTranslationConfigOriginalVID_Type()
)
swhVLANTranslationConfigOriginalVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigOriginalVID.setStatus("mandatory")


class _SwhVLANTranslationConfigMappedVID_Type(Integer32):
    """Custom type swhVLANTranslationConfigMappedVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwhVLANTranslationConfigMappedVID_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigMappedVID_Object = MibTableColumn
swhVLANTranslationConfigMappedVID = _SwhVLANTranslationConfigMappedVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1, 7),
    _SwhVLANTranslationConfigMappedVID_Type()
)
swhVLANTranslationConfigMappedVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigMappedVID.setStatus("mandatory")


class _SwhVLANTranslationConfigPriority_Type(Integer32):
    """Custom type swhVLANTranslationConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwhVLANTranslationConfigPriority_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigPriority_Object = MibTableColumn
swhVLANTranslationConfigPriority = _SwhVLANTranslationConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1, 8),
    _SwhVLANTranslationConfigPriority_Type()
)
swhVLANTranslationConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigPriority.setStatus("mandatory")


class _SwhVLANTranslationConfigDelete_Type(Integer32):
    """Custom type swhVLANTranslationConfigDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhVLANTranslationConfigDelete_Type.__name__ = "Integer32"
_SwhVLANTranslationConfigDelete_Object = MibTableColumn
swhVLANTranslationConfigDelete = _SwhVLANTranslationConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 4, 7, 5, 1, 10),
    _SwhVLANTranslationConfigDelete_Type()
)
swhVLANTranslationConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVLANTranslationConfigDelete.setStatus("mandatory")
_SwhLoopDetection_ObjectIdentity = ObjectIdentity
swhLoopDetection = _SwhLoopDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13)
)


class _SwhLoopConfigPort1_Type(Integer32):
    """Custom type swhLoopConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLoopConfigPort1_Type.__name__ = "Integer32"
_SwhLoopConfigPort1_Object = MibScalar
swhLoopConfigPort1 = _SwhLoopConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 1),
    _SwhLoopConfigPort1_Type()
)
swhLoopConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigPort1.setStatus("mandatory")


class _SwhLoopConfigPort2_Type(Integer32):
    """Custom type swhLoopConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLoopConfigPort2_Type.__name__ = "Integer32"
_SwhLoopConfigPort2_Object = MibScalar
swhLoopConfigPort2 = _SwhLoopConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 2),
    _SwhLoopConfigPort2_Type()
)
swhLoopConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigPort2.setStatus("mandatory")


class _SwhLoopConfigPort3_Type(Integer32):
    """Custom type swhLoopConfigPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLoopConfigPort3_Type.__name__ = "Integer32"
_SwhLoopConfigPort3_Object = MibScalar
swhLoopConfigPort3 = _SwhLoopConfigPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 3),
    _SwhLoopConfigPort3_Type()
)
swhLoopConfigPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigPort3.setStatus("mandatory")


class _SwhLoopConfigPort4_Type(Integer32):
    """Custom type swhLoopConfigPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLoopConfigPort4_Type.__name__ = "Integer32"
_SwhLoopConfigPort4_Object = MibScalar
swhLoopConfigPort4 = _SwhLoopConfigPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 4),
    _SwhLoopConfigPort4_Type()
)
swhLoopConfigPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigPort4.setStatus("mandatory")


class _SwhLoopConfigPort5_Type(Integer32):
    """Custom type swhLoopConfigPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLoopConfigPort5_Type.__name__ = "Integer32"
_SwhLoopConfigPort5_Object = MibScalar
swhLoopConfigPort5 = _SwhLoopConfigPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 5),
    _SwhLoopConfigPort5_Type()
)
swhLoopConfigPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigPort5.setStatus("mandatory")


class _SwhLoopConfigPort6_Type(Integer32):
    """Custom type swhLoopConfigPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLoopConfigPort6_Type.__name__ = "Integer32"
_SwhLoopConfigPort6_Object = MibScalar
swhLoopConfigPort6 = _SwhLoopConfigPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 6),
    _SwhLoopConfigPort6_Type()
)
swhLoopConfigPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigPort6.setStatus("mandatory")


class _SwhLoopConfigLoopDetection_Type(Integer32):
    """Custom type swhLoopConfigLoopDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLoopConfigLoopDetection_Type.__name__ = "Integer32"
_SwhLoopConfigLoopDetection_Object = MibScalar
swhLoopConfigLoopDetection = _SwhLoopConfigLoopDetection_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 60),
    _SwhLoopConfigLoopDetection_Type()
)
swhLoopConfigLoopDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigLoopDetection.setStatus("mandatory")


class _SwhLoopConfigDetectionInterval_Type(Integer32):
    """Custom type swhLoopConfigDetectionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_SwhLoopConfigDetectionInterval_Type.__name__ = "Integer32"
_SwhLoopConfigDetectionInterval_Object = MibScalar
swhLoopConfigDetectionInterval = _SwhLoopConfigDetectionInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 63),
    _SwhLoopConfigDetectionInterval_Type()
)
swhLoopConfigDetectionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigDetectionInterval.setStatus("mandatory")


class _SwhLoopConfigUnlockInterval_Type(Integer32):
    """Custom type swhLoopConfigUnlockInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_SwhLoopConfigUnlockInterval_Type.__name__ = "Integer32"
_SwhLoopConfigUnlockInterval_Object = MibScalar
swhLoopConfigUnlockInterval = _SwhLoopConfigUnlockInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 64),
    _SwhLoopConfigUnlockInterval_Type()
)
swhLoopConfigUnlockInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigUnlockInterval.setStatus("mandatory")


class _SwhLoopConfigVLAN1_Type(Integer32):
    """Custom type swhLoopConfigVLAN1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SwhLoopConfigVLAN1_Type.__name__ = "Integer32"
_SwhLoopConfigVLAN1_Object = MibScalar
swhLoopConfigVLAN1 = _SwhLoopConfigVLAN1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 65),
    _SwhLoopConfigVLAN1_Type()
)
swhLoopConfigVLAN1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigVLAN1.setStatus("mandatory")


class _SwhLoopConfigVLAN2_Type(Integer32):
    """Custom type swhLoopConfigVLAN2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SwhLoopConfigVLAN2_Type.__name__ = "Integer32"
_SwhLoopConfigVLAN2_Object = MibScalar
swhLoopConfigVLAN2 = _SwhLoopConfigVLAN2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 66),
    _SwhLoopConfigVLAN2_Type()
)
swhLoopConfigVLAN2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigVLAN2.setStatus("mandatory")


class _SwhLoopConfigVLAN3_Type(Integer32):
    """Custom type swhLoopConfigVLAN3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SwhLoopConfigVLAN3_Type.__name__ = "Integer32"
_SwhLoopConfigVLAN3_Object = MibScalar
swhLoopConfigVLAN3 = _SwhLoopConfigVLAN3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 67),
    _SwhLoopConfigVLAN3_Type()
)
swhLoopConfigVLAN3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigVLAN3.setStatus("mandatory")


class _SwhLoopConfigVLAN4_Type(Integer32):
    """Custom type swhLoopConfigVLAN4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_SwhLoopConfigVLAN4_Type.__name__ = "Integer32"
_SwhLoopConfigVLAN4_Object = MibScalar
swhLoopConfigVLAN4 = _SwhLoopConfigVLAN4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 68),
    _SwhLoopConfigVLAN4_Type()
)
swhLoopConfigVLAN4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigVLAN4.setStatus("mandatory")


class _SwhLoopConfigAllVLAN_Type(Integer32):
    """Custom type swhLoopConfigAllVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLoopConfigAllVLAN_Type.__name__ = "Integer32"
_SwhLoopConfigAllVLAN_Object = MibScalar
swhLoopConfigAllVLAN = _SwhLoopConfigAllVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 13, 69),
    _SwhLoopConfigAllVLAN_Type()
)
swhLoopConfigAllVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopConfigAllVLAN.setStatus("mandatory")
_SwhLLDPConfiguration_ObjectIdentity = ObjectIdentity
swhLLDPConfiguration = _SwhLLDPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14)
)


class _SwhLLDPConfigPort1_Type(Integer32):
    """Custom type swhLLDPConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLLDPConfigPort1_Type.__name__ = "Integer32"
_SwhLLDPConfigPort1_Object = MibScalar
swhLLDPConfigPort1 = _SwhLLDPConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 1),
    _SwhLLDPConfigPort1_Type()
)
swhLLDPConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigPort1.setStatus("mandatory")


class _SwhLLDPConfigPort2_Type(Integer32):
    """Custom type swhLLDPConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLLDPConfigPort2_Type.__name__ = "Integer32"
_SwhLLDPConfigPort2_Object = MibScalar
swhLLDPConfigPort2 = _SwhLLDPConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 2),
    _SwhLLDPConfigPort2_Type()
)
swhLLDPConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigPort2.setStatus("mandatory")


class _SwhLLDPConfigPort3_Type(Integer32):
    """Custom type swhLLDPConfigPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLLDPConfigPort3_Type.__name__ = "Integer32"
_SwhLLDPConfigPort3_Object = MibScalar
swhLLDPConfigPort3 = _SwhLLDPConfigPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 3),
    _SwhLLDPConfigPort3_Type()
)
swhLLDPConfigPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigPort3.setStatus("mandatory")


class _SwhLLDPConfigPort4_Type(Integer32):
    """Custom type swhLLDPConfigPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLLDPConfigPort4_Type.__name__ = "Integer32"
_SwhLLDPConfigPort4_Object = MibScalar
swhLLDPConfigPort4 = _SwhLLDPConfigPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 4),
    _SwhLLDPConfigPort4_Type()
)
swhLLDPConfigPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigPort4.setStatus("mandatory")


class _SwhLLDPConfigPort5_Type(Integer32):
    """Custom type swhLLDPConfigPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLLDPConfigPort5_Type.__name__ = "Integer32"
_SwhLLDPConfigPort5_Object = MibScalar
swhLLDPConfigPort5 = _SwhLLDPConfigPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 5),
    _SwhLLDPConfigPort5_Type()
)
swhLLDPConfigPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigPort5.setStatus("mandatory")


class _SwhLLDPConfigPort6_Type(Integer32):
    """Custom type swhLLDPConfigPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhLLDPConfigPort6_Type.__name__ = "Integer32"
_SwhLLDPConfigPort6_Object = MibScalar
swhLLDPConfigPort6 = _SwhLLDPConfigPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 6),
    _SwhLLDPConfigPort6_Type()
)
swhLLDPConfigPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigPort6.setStatus("mandatory")


class _SwhLLDPConfigReceiverHoldTime_Type(Integer32):
    """Custom type swhLLDPConfigReceiverHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_SwhLLDPConfigReceiverHoldTime_Type.__name__ = "Integer32"
_SwhLLDPConfigReceiverHoldTime_Object = MibScalar
swhLLDPConfigReceiverHoldTime = _SwhLLDPConfigReceiverHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 90),
    _SwhLLDPConfigReceiverHoldTime_Type()
)
swhLLDPConfigReceiverHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigReceiverHoldTime.setStatus("mandatory")


class _SwhLLDPConfigSendingLLDPPacketInterval_Type(Integer32):
    """Custom type swhLLDPConfigSendingLLDPPacketInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_SwhLLDPConfigSendingLLDPPacketInterval_Type.__name__ = "Integer32"
_SwhLLDPConfigSendingLLDPPacketInterval_Object = MibScalar
swhLLDPConfigSendingLLDPPacketInterval = _SwhLLDPConfigSendingLLDPPacketInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 91),
    _SwhLLDPConfigSendingLLDPPacketInterval_Type()
)
swhLLDPConfigSendingLLDPPacketInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigSendingLLDPPacketInterval.setStatus("mandatory")


class _SwhLLDPConfigSendingLLDPPacketPerDiscover_Type(Integer32):
    """Custom type swhLLDPConfigSendingLLDPPacketPerDiscover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SwhLLDPConfigSendingLLDPPacketPerDiscover_Type.__name__ = "Integer32"
_SwhLLDPConfigSendingLLDPPacketPerDiscover_Object = MibScalar
swhLLDPConfigSendingLLDPPacketPerDiscover = _SwhLLDPConfigSendingLLDPPacketPerDiscover_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 92),
    _SwhLLDPConfigSendingLLDPPacketPerDiscover_Type()
)
swhLLDPConfigSendingLLDPPacketPerDiscover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigSendingLLDPPacketPerDiscover.setStatus("mandatory")
_SwhLLDPConfigItem_Type = DisplayString
_SwhLLDPConfigItem_Object = MibScalar
swhLLDPConfigItem = _SwhLLDPConfigItem_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 94),
    _SwhLLDPConfigItem_Type()
)
swhLLDPConfigItem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPConfigItem.setStatus("mandatory")


class _SwhLLDPConfigPortDescription_Type(Integer32):
    """Custom type swhLLDPConfigPortDescription based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLLDPConfigPortDescription_Type.__name__ = "Integer32"
_SwhLLDPConfigPortDescription_Object = MibScalar
swhLLDPConfigPortDescription = _SwhLLDPConfigPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 95),
    _SwhLLDPConfigPortDescription_Type()
)
swhLLDPConfigPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigPortDescription.setStatus("mandatory")


class _SwhLLDPConfigSystemName_Type(Integer32):
    """Custom type swhLLDPConfigSystemName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLLDPConfigSystemName_Type.__name__ = "Integer32"
_SwhLLDPConfigSystemName_Object = MibScalar
swhLLDPConfigSystemName = _SwhLLDPConfigSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 96),
    _SwhLLDPConfigSystemName_Type()
)
swhLLDPConfigSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigSystemName.setStatus("mandatory")


class _SwhLLDPConfigSystemDescription_Type(Integer32):
    """Custom type swhLLDPConfigSystemDescription based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLLDPConfigSystemDescription_Type.__name__ = "Integer32"
_SwhLLDPConfigSystemDescription_Object = MibScalar
swhLLDPConfigSystemDescription = _SwhLLDPConfigSystemDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 97),
    _SwhLLDPConfigSystemDescription_Type()
)
swhLLDPConfigSystemDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigSystemDescription.setStatus("mandatory")


class _SwhLLDPConfigSystemCapabilities_Type(Integer32):
    """Custom type swhLLDPConfigSystemCapabilities based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLLDPConfigSystemCapabilities_Type.__name__ = "Integer32"
_SwhLLDPConfigSystemCapabilities_Object = MibScalar
swhLLDPConfigSystemCapabilities = _SwhLLDPConfigSystemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 98),
    _SwhLLDPConfigSystemCapabilities_Type()
)
swhLLDPConfigSystemCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigSystemCapabilities.setStatus("mandatory")


class _SwhLLDPConfigManagementAddress_Type(Integer32):
    """Custom type swhLLDPConfigManagementAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhLLDPConfigManagementAddress_Type.__name__ = "Integer32"
_SwhLLDPConfigManagementAddress_Object = MibScalar
swhLLDPConfigManagementAddress = _SwhLLDPConfigManagementAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 14, 99),
    _SwhLLDPConfigManagementAddress_Type()
)
swhLLDPConfigManagementAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLLDPConfigManagementAddress.setStatus("mandatory")
_SwhPortMirroring_ObjectIdentity = ObjectIdentity
swhPortMirroring = _SwhPortMirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 15)
)
_SwhPortMirrorSourcePortConfigTable_Object = MibTable
swhPortMirrorSourcePortConfigTable = _SwhPortMirrorSourcePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 15, 1)
)
if mibBuilder.loadTexts:
    swhPortMirrorSourcePortConfigTable.setStatus("mandatory")
_SwhPortMirrorSourcePortConfigEntry_Object = MibTableRow
swhPortMirrorSourcePortConfigEntry = _SwhPortMirrorSourcePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 15, 1, 1)
)
swhPortMirrorSourcePortConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhPortMirrorSourcePortConfigIndex"),
)
if mibBuilder.loadTexts:
    swhPortMirrorSourcePortConfigEntry.setStatus("mandatory")


class _SwhPortMirrorSourcePortConfigIndex_Type(Integer32):
    """Custom type swhPortMirrorSourcePortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhPortMirrorSourcePortConfigIndex_Type.__name__ = "Integer32"
_SwhPortMirrorSourcePortConfigIndex_Object = MibTableColumn
swhPortMirrorSourcePortConfigIndex = _SwhPortMirrorSourcePortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 15, 1, 1, 1),
    _SwhPortMirrorSourcePortConfigIndex_Type()
)
swhPortMirrorSourcePortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhPortMirrorSourcePortConfigIndex.setStatus("mandatory")


class _SwhPortMirrorSourcePortConfigMember_Type(Integer32):
    """Custom type swhPortMirrorSourcePortConfigMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhPortMirrorSourcePortConfigMember_Type.__name__ = "Integer32"
_SwhPortMirrorSourcePortConfigMember_Object = MibTableColumn
swhPortMirrorSourcePortConfigMember = _SwhPortMirrorSourcePortConfigMember_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 15, 1, 1, 2),
    _SwhPortMirrorSourcePortConfigMember_Type()
)
swhPortMirrorSourcePortConfigMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortMirrorSourcePortConfigMember.setStatus("mandatory")


class _SwhTargetPort_Type(Integer32):
    """Custom type swhTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("port01", 1),
          ("port02", 2),
          ("port03", 3),
          ("port04", 4),
          ("port05", 5),
          ("port06", 6))
    )


_SwhTargetPort_Type.__name__ = "Integer32"
_SwhTargetPort_Object = MibScalar
swhTargetPort = _SwhTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 15, 2),
    _SwhTargetPort_Type()
)
swhTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTargetPort.setStatus("mandatory")
_SwhDIDOConfiguration_ObjectIdentity = ObjectIdentity
swhDIDOConfiguration = _SwhDIDOConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22)
)
_SwhDIConfigTable_Object = MibTable
swhDIConfigTable = _SwhDIConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 1)
)
if mibBuilder.loadTexts:
    swhDIConfigTable.setStatus("mandatory")
_SwhDIConfigEntry_Object = MibTableRow
swhDIConfigEntry = _SwhDIConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 1, 1)
)
swhDIConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDIConfigIndex"),
)
if mibBuilder.loadTexts:
    swhDIConfigEntry.setStatus("mandatory")


class _SwhDIConfigIndex_Type(Integer32):
    """Custom type swhDIConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDIConfigIndex_Type.__name__ = "Integer32"
_SwhDIConfigIndex_Object = MibTableColumn
swhDIConfigIndex = _SwhDIConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 1, 1, 1),
    _SwhDIConfigIndex_Type()
)
swhDIConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDIConfigIndex.setStatus("mandatory")


class _SwhDIConfigNormal_Type(Integer32):
    """Custom type swhDIConfigNormal based on Integer32"""
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


_SwhDIConfigNormal_Type.__name__ = "Integer32"
_SwhDIConfigNormal_Object = MibTableColumn
swhDIConfigNormal = _SwhDIConfigNormal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 1, 1, 2),
    _SwhDIConfigNormal_Type()
)
swhDIConfigNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDIConfigNormal.setStatus("mandatory")
_SwhDOConfigTable_Object = MibTable
swhDOConfigTable = _SwhDOConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2)
)
if mibBuilder.loadTexts:
    swhDOConfigTable.setStatus("mandatory")
_SwhDOConfigEntry_Object = MibTableRow
swhDOConfigEntry = _SwhDOConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2, 1)
)
swhDOConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDOConfigIndex"),
)
if mibBuilder.loadTexts:
    swhDOConfigEntry.setStatus("mandatory")


class _SwhDOConfigIndex_Type(Integer32):
    """Custom type swhDOConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDOConfigIndex_Type.__name__ = "Integer32"
_SwhDOConfigIndex_Object = MibTableColumn
swhDOConfigIndex = _SwhDOConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2, 1, 1),
    _SwhDOConfigIndex_Type()
)
swhDOConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDOConfigIndex.setStatus("mandatory")


class _SwhDOConfigNormal_Type(Integer32):
    """Custom type swhDOConfigNormal based on Integer32"""
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


_SwhDOConfigNormal_Type.__name__ = "Integer32"
_SwhDOConfigNormal_Object = MibTableColumn
swhDOConfigNormal = _SwhDOConfigNormal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2, 1, 2),
    _SwhDOConfigNormal_Type()
)
swhDOConfigNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDOConfigNormal.setStatus("mandatory")


class _SwhDOConfigEventTrigger_Type(Integer32):
    """Custom type swhDOConfigEventTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDOConfigEventTrigger_Type.__name__ = "Integer32"
_SwhDOConfigEventTrigger_Object = MibTableColumn
swhDOConfigEventTrigger = _SwhDOConfigEventTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2, 1, 3),
    _SwhDOConfigEventTrigger_Type()
)
swhDOConfigEventTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDOConfigEventTrigger.setStatus("mandatory")


class _SwhDOConfigEventDigitalInput1_Type(Integer32):
    """Custom type swhDOConfigEventDigitalInput1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDOConfigEventDigitalInput1_Type.__name__ = "Integer32"
_SwhDOConfigEventDigitalInput1_Object = MibTableColumn
swhDOConfigEventDigitalInput1 = _SwhDOConfigEventDigitalInput1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2, 1, 4),
    _SwhDOConfigEventDigitalInput1_Type()
)
swhDOConfigEventDigitalInput1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDOConfigEventDigitalInput1.setStatus("mandatory")


class _SwhDOConfigEventPortList_Type(DisplayString):
    """Custom type swhDOConfigEventPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhDOConfigEventPortList_Type.__name__ = "DisplayString"
_SwhDOConfigEventPortList_Object = MibTableColumn
swhDOConfigEventPortList = _SwhDOConfigEventPortList_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2, 1, 6),
    _SwhDOConfigEventPortList_Type()
)
swhDOConfigEventPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDOConfigEventPortList.setStatus("mandatory")


class _SwhDOConfigEventPower1_Type(Integer32):
    """Custom type swhDOConfigEventPower1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDOConfigEventPower1_Type.__name__ = "Integer32"
_SwhDOConfigEventPower1_Object = MibTableColumn
swhDOConfigEventPower1 = _SwhDOConfigEventPower1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2, 1, 7),
    _SwhDOConfigEventPower1_Type()
)
swhDOConfigEventPower1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDOConfigEventPower1.setStatus("mandatory")


class _SwhDOConfigEventPower2_Type(Integer32):
    """Custom type swhDOConfigEventPower2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDOConfigEventPower2_Type.__name__ = "Integer32"
_SwhDOConfigEventPower2_Object = MibTableColumn
swhDOConfigEventPower2 = _SwhDOConfigEventPower2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 22, 2, 1, 8),
    _SwhDOConfigEventPower2_Type()
)
swhDOConfigEventPower2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDOConfigEventPower2.setStatus("mandatory")
_SwhPOEConfiguration_ObjectIdentity = ObjectIdentity
swhPOEConfiguration = _SwhPOEConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23)
)
_SwhPOEPortConfigTable_Object = MibTable
swhPOEPortConfigTable = _SwhPOEPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2)
)
if mibBuilder.loadTexts:
    swhPOEPortConfigTable.setStatus("mandatory")
_SwhPOEPortConfigEntry_Object = MibTableRow
swhPOEPortConfigEntry = _SwhPOEPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2, 1)
)
swhPOEPortConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhPOEPortConfigIndex"),
)
if mibBuilder.loadTexts:
    swhPOEPortConfigEntry.setStatus("mandatory")
_SwhPOEPortConfigIndex_Type = Integer32
_SwhPOEPortConfigIndex_Object = MibTableColumn
swhPOEPortConfigIndex = _SwhPOEPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2, 1, 1),
    _SwhPOEPortConfigIndex_Type()
)
swhPOEPortConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEPortConfigIndex.setStatus("mandatory")


class _SwhPOEPortConfigState_Type(Integer32):
    """Custom type swhPOEPortConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("shutdown", 0),
          ("injector-30watt", 1),
          ("auto-afat", 2))
    )


_SwhPOEPortConfigState_Type.__name__ = "Integer32"
_SwhPOEPortConfigState_Object = MibTableColumn
swhPOEPortConfigState = _SwhPOEPortConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2, 1, 2),
    _SwhPOEPortConfigState_Type()
)
swhPOEPortConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPOEPortConfigState.setStatus("mandatory")


class _SwhPOEPortConfigPort_Type(Integer32):
    """Custom type swhPOEPortConfigPort based on Integer32"""
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
        *(("port01", 0),
          ("port02", 1),
          ("port03", 2),
          ("port04", 3),
          ("port05", 4),
          ("port06", 5))
    )


_SwhPOEPortConfigPort_Type.__name__ = "Integer32"
_SwhPOEPortConfigPort_Object = MibTableColumn
swhPOEPortConfigPort = _SwhPOEPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2, 1, 3),
    _SwhPOEPortConfigPort_Type()
)
swhPOEPortConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEPortConfigPort.setStatus("mandatory")


class _SwhPOEPortConfigName_Type(DisplayString):
    """Custom type swhPOEPortConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPOEPortConfigName_Type.__name__ = "DisplayString"
_SwhPOEPortConfigName_Object = MibTableColumn
swhPOEPortConfigName = _SwhPOEPortConfigName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2, 1, 4),
    _SwhPOEPortConfigName_Type()
)
swhPOEPortConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPOEPortConfigName.setStatus("mandatory")


class _SwhPOEPortConfigTimeRange_Type(DisplayString):
    """Custom type swhPOEPortConfigTimeRange based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPOEPortConfigTimeRange_Type.__name__ = "DisplayString"
_SwhPOEPortConfigTimeRange_Object = MibTableColumn
swhPOEPortConfigTimeRange = _SwhPOEPortConfigTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2, 1, 5),
    _SwhPOEPortConfigTimeRange_Type()
)
swhPOEPortConfigTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPOEPortConfigTimeRange.setStatus("mandatory")


class _SwhPOEPortConfigSchedule_Type(Integer32):
    """Custom type swhPOEPortConfigSchedule based on Integer32"""
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


_SwhPOEPortConfigSchedule_Type.__name__ = "Integer32"
_SwhPOEPortConfigSchedule_Object = MibTableColumn
swhPOEPortConfigSchedule = _SwhPOEPortConfigSchedule_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2, 1, 6),
    _SwhPOEPortConfigSchedule_Type()
)
swhPOEPortConfigSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPOEPortConfigSchedule.setStatus("mandatory")


class _SwhPOEPortConfigPriority_Type(Integer32):
    """Custom type swhPOEPortConfigPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("high", 1),
          ("low", 2))
    )


_SwhPOEPortConfigPriority_Type.__name__ = "Integer32"
_SwhPOEPortConfigPriority_Object = MibTableColumn
swhPOEPortConfigPriority = _SwhPOEPortConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 2, 1, 7),
    _SwhPOEPortConfigPriority_Type()
)
swhPOEPortConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPOEPortConfigPriority.setStatus("mandatory")


class _SwhPOEConfigTotalBudget_Type(Integer32):
    """Custom type swhPOEConfigTotalBudget based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SwhPOEConfigTotalBudget_Type.__name__ = "Integer32"
_SwhPOEConfigTotalBudget_Object = MibScalar
swhPOEConfigTotalBudget = _SwhPOEConfigTotalBudget_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 23, 5),
    _SwhPOEConfigTotalBudget_Type()
)
swhPOEConfigTotalBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPOEConfigTotalBudget.setStatus("mandatory")
_SwhRingDetection_ObjectIdentity = ObjectIdentity
swhRingDetection = _SwhRingDetection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 24)
)


class _SwhRingDetectionEnable_Type(Integer32):
    """Custom type swhRingDetectionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhRingDetectionEnable_Type.__name__ = "Integer32"
_SwhRingDetectionEnable_Object = MibScalar
swhRingDetectionEnable = _SwhRingDetectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 24, 1),
    _SwhRingDetectionEnable_Type()
)
swhRingDetectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRingDetectionEnable.setStatus("mandatory")


class _SwhRingDetectionSoftwareRole_Type(Integer32):
    """Custom type swhRingDetectionSoftwareRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slave", 0),
          ("master", 1))
    )


_SwhRingDetectionSoftwareRole_Type.__name__ = "Integer32"
_SwhRingDetectionSoftwareRole_Object = MibScalar
swhRingDetectionSoftwareRole = _SwhRingDetectionSoftwareRole_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 24, 2),
    _SwhRingDetectionSoftwareRole_Type()
)
swhRingDetectionSoftwareRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRingDetectionSoftwareRole.setStatus("mandatory")
_SwhRingDetectionPortList_Type = DisplayString
_SwhRingDetectionPortList_Object = MibScalar
swhRingDetectionPortList = _SwhRingDetectionPortList_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 24, 4),
    _SwhRingDetectionPortList_Type()
)
swhRingDetectionPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRingDetectionPortList.setStatus("mandatory")
_SwhMacAddressManagement_ObjectIdentity = ObjectIdentity
swhMacAddressManagement = _SwhMacAddressManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35)
)
_SwhMACTableLearning_ObjectIdentity = ObjectIdentity
swhMACTableLearning = _SwhMACTableLearning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 1)
)
_SwhMACTableLearningTable_Object = MibTable
swhMACTableLearningTable = _SwhMACTableLearningTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 1, 2)
)
if mibBuilder.loadTexts:
    swhMACTableLearningTable.setStatus("mandatory")
_SwhMACTableLearningEntry_Object = MibTableRow
swhMACTableLearningEntry = _SwhMACTableLearningEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 1, 2, 1)
)
swhMACTableLearningEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhMACTableLearningIndex"),
)
if mibBuilder.loadTexts:
    swhMACTableLearningEntry.setStatus("mandatory")


class _SwhMACTableLearningIndex_Type(Integer32):
    """Custom type swhMACTableLearningIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMACTableLearningIndex_Type.__name__ = "Integer32"
_SwhMACTableLearningIndex_Object = MibTableColumn
swhMACTableLearningIndex = _SwhMACTableLearningIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 1, 2, 1, 1),
    _SwhMACTableLearningIndex_Type()
)
swhMACTableLearningIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhMACTableLearningIndex.setStatus("mandatory")


class _SwhMACTableLearningLearning_Type(Integer32):
    """Custom type swhMACTableLearningLearning based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("disable", 1))
    )


_SwhMACTableLearningLearning_Type.__name__ = "Integer32"
_SwhMACTableLearningLearning_Object = MibTableColumn
swhMACTableLearningLearning = _SwhMACTableLearningLearning_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 1, 2, 1, 2),
    _SwhMACTableLearningLearning_Type()
)
swhMACTableLearningLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMACTableLearningLearning.setStatus("mandatory")
_SwhStaticMACTableConfiguration_ObjectIdentity = ObjectIdentity
swhStaticMACTableConfiguration = _SwhStaticMACTableConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3)
)
_SwhStaticForwardTable_Object = MibTable
swhStaticForwardTable = _SwhStaticForwardTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3, 2)
)
if mibBuilder.loadTexts:
    swhStaticForwardTable.setStatus("mandatory")
_SwhStaticForwardEntry_Object = MibTableRow
swhStaticForwardEntry = _SwhStaticForwardEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3, 2, 1)
)
swhStaticForwardEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhStaticForwardIndex"),
)
if mibBuilder.loadTexts:
    swhStaticForwardEntry.setStatus("mandatory")


class _SwhStaticForwardIndex_Type(Integer32):
    """Custom type swhStaticForwardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhStaticForwardIndex_Type.__name__ = "Integer32"
_SwhStaticForwardIndex_Object = MibTableColumn
swhStaticForwardIndex = _SwhStaticForwardIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3, 2, 1, 1),
    _SwhStaticForwardIndex_Type()
)
swhStaticForwardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhStaticForwardIndex.setStatus("mandatory")


class _SwhStaticForwardValid_Type(Integer32):
    """Custom type swhStaticForwardValid based on Integer32"""
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


_SwhStaticForwardValid_Type.__name__ = "Integer32"
_SwhStaticForwardValid_Object = MibTableColumn
swhStaticForwardValid = _SwhStaticForwardValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3, 2, 1, 2),
    _SwhStaticForwardValid_Type()
)
swhStaticForwardValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhStaticForwardValid.setStatus("mandatory")
_SwhStaticForwardMacAddress_Type = MacAddress
_SwhStaticForwardMacAddress_Object = MibTableColumn
swhStaticForwardMacAddress = _SwhStaticForwardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3, 2, 1, 3),
    _SwhStaticForwardMacAddress_Type()
)
swhStaticForwardMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticForwardMacAddress.setStatus("mandatory")


class _SwhStaticForwardVID_Type(Integer32):
    """Custom type swhStaticForwardVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwhStaticForwardVID_Type.__name__ = "Integer32"
_SwhStaticForwardVID_Object = MibTableColumn
swhStaticForwardVID = _SwhStaticForwardVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3, 2, 1, 4),
    _SwhStaticForwardVID_Type()
)
swhStaticForwardVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticForwardVID.setStatus("mandatory")


class _SwhStaticForwardPort_Type(Integer32):
    """Custom type swhStaticForwardPort based on Integer32"""
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
        *(("port01", 0),
          ("port02", 1),
          ("port03", 2),
          ("port04", 3),
          ("port05", 4),
          ("port06", 5))
    )


_SwhStaticForwardPort_Type.__name__ = "Integer32"
_SwhStaticForwardPort_Object = MibTableColumn
swhStaticForwardPort = _SwhStaticForwardPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3, 2, 1, 5),
    _SwhStaticForwardPort_Type()
)
swhStaticForwardPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticForwardPort.setStatus("mandatory")


class _SwhStaticForwardDelete_Type(Integer32):
    """Custom type swhStaticForwardDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhStaticForwardDelete_Type.__name__ = "Integer32"
_SwhStaticForwardDelete_Object = MibTableColumn
swhStaticForwardDelete = _SwhStaticForwardDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 35, 3, 2, 1, 6),
    _SwhStaticForwardDelete_Type()
)
swhStaticForwardDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticForwardDelete.setStatus("mandatory")
_SwhLayer2ProtocolTunnel_ObjectIdentity = ObjectIdentity
swhLayer2ProtocolTunnel = _SwhLayer2ProtocolTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37)
)


class _SwhL2PTConfigState_Type(Integer32):
    """Custom type swhL2PTConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhL2PTConfigState_Type.__name__ = "Integer32"
_SwhL2PTConfigState_Object = MibScalar
swhL2PTConfigState = _SwhL2PTConfigState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 1),
    _SwhL2PTConfigState_Type()
)
swhL2PTConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTConfigState.setStatus("mandatory")


class _SwhL2PTConfigDestinationMACAddress_Type(DisplayString):
    """Custom type swhL2PTConfigDestinationMACAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_SwhL2PTConfigDestinationMACAddress_Type.__name__ = "DisplayString"
_SwhL2PTConfigDestinationMACAddress_Object = MibScalar
swhL2PTConfigDestinationMACAddress = _SwhL2PTConfigDestinationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 2),
    _SwhL2PTConfigDestinationMACAddress_Type()
)
swhL2PTConfigDestinationMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTConfigDestinationMACAddress.setStatus("mandatory")


class _SwhL2PTConfigClassOfService_Type(Integer32):
    """Custom type swhL2PTConfigClassOfService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwhL2PTConfigClassOfService_Type.__name__ = "Integer32"
_SwhL2PTConfigClassOfService_Object = MibScalar
swhL2PTConfigClassOfService = _SwhL2PTConfigClassOfService_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 3),
    _SwhL2PTConfigClassOfService_Type()
)
swhL2PTConfigClassOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTConfigClassOfService.setStatus("mandatory")
_SwhL2PTPortConfigTable_Object = MibTable
swhL2PTPortConfigTable = _SwhL2PTPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5)
)
if mibBuilder.loadTexts:
    swhL2PTPortConfigTable.setStatus("mandatory")
_SwhL2PTPortConfigEntry_Object = MibTableRow
swhL2PTPortConfigEntry = _SwhL2PTPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1)
)
swhL2PTPortConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhL2PTPortConfigIndex"),
)
if mibBuilder.loadTexts:
    swhL2PTPortConfigEntry.setStatus("mandatory")


class _SwhL2PTPortConfigIndex_Type(Integer32):
    """Custom type swhL2PTPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhL2PTPortConfigIndex_Type.__name__ = "Integer32"
_SwhL2PTPortConfigIndex_Object = MibTableColumn
swhL2PTPortConfigIndex = _SwhL2PTPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 1),
    _SwhL2PTPortConfigIndex_Type()
)
swhL2PTPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhL2PTPortConfigIndex.setStatus("mandatory")
_SwhL2PTPortConfigPort_Type = DisplayString
_SwhL2PTPortConfigPort_Object = MibTableColumn
swhL2PTPortConfigPort = _SwhL2PTPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 2),
    _SwhL2PTPortConfigPort_Type()
)
swhL2PTPortConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhL2PTPortConfigPort.setStatus("mandatory")


class _SwhL2PTPortConfigCDP_Type(Integer32):
    """Custom type swhL2PTPortConfigCDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhL2PTPortConfigCDP_Type.__name__ = "Integer32"
_SwhL2PTPortConfigCDP_Object = MibTableColumn
swhL2PTPortConfigCDP = _SwhL2PTPortConfigCDP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 3),
    _SwhL2PTPortConfigCDP_Type()
)
swhL2PTPortConfigCDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTPortConfigCDP.setStatus("mandatory")


class _SwhL2PTPortConfigLLDP_Type(Integer32):
    """Custom type swhL2PTPortConfigLLDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhL2PTPortConfigLLDP_Type.__name__ = "Integer32"
_SwhL2PTPortConfigLLDP_Object = MibTableColumn
swhL2PTPortConfigLLDP = _SwhL2PTPortConfigLLDP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 4),
    _SwhL2PTPortConfigLLDP_Type()
)
swhL2PTPortConfigLLDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTPortConfigLLDP.setStatus("mandatory")


class _SwhL2PTPortConfigSTP_Type(Integer32):
    """Custom type swhL2PTPortConfigSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhL2PTPortConfigSTP_Type.__name__ = "Integer32"
_SwhL2PTPortConfigSTP_Object = MibTableColumn
swhL2PTPortConfigSTP = _SwhL2PTPortConfigSTP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 5),
    _SwhL2PTPortConfigSTP_Type()
)
swhL2PTPortConfigSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTPortConfigSTP.setStatus("mandatory")


class _SwhL2PTPortConfigVTP_Type(Integer32):
    """Custom type swhL2PTPortConfigVTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhL2PTPortConfigVTP_Type.__name__ = "Integer32"
_SwhL2PTPortConfigVTP_Object = MibTableColumn
swhL2PTPortConfigVTP = _SwhL2PTPortConfigVTP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 6),
    _SwhL2PTPortConfigVTP_Type()
)
swhL2PTPortConfigVTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTPortConfigVTP.setStatus("mandatory")


class _SwhL2PTPortConfigLACP_Type(Integer32):
    """Custom type swhL2PTPortConfigLACP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhL2PTPortConfigLACP_Type.__name__ = "Integer32"
_SwhL2PTPortConfigLACP_Object = MibTableColumn
swhL2PTPortConfigLACP = _SwhL2PTPortConfigLACP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 7),
    _SwhL2PTPortConfigLACP_Type()
)
swhL2PTPortConfigLACP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTPortConfigLACP.setStatus("mandatory")


class _SwhL2PTPortConfigPAgP_Type(Integer32):
    """Custom type swhL2PTPortConfigPAgP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhL2PTPortConfigPAgP_Type.__name__ = "Integer32"
_SwhL2PTPortConfigPAgP_Object = MibTableColumn
swhL2PTPortConfigPAgP = _SwhL2PTPortConfigPAgP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 8),
    _SwhL2PTPortConfigPAgP_Type()
)
swhL2PTPortConfigPAgP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTPortConfigPAgP.setStatus("mandatory")


class _SwhL2PTPortConfigUDLD_Type(Integer32):
    """Custom type swhL2PTPortConfigUDLD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhL2PTPortConfigUDLD_Type.__name__ = "Integer32"
_SwhL2PTPortConfigUDLD_Object = MibTableColumn
swhL2PTPortConfigUDLD = _SwhL2PTPortConfigUDLD_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 9),
    _SwhL2PTPortConfigUDLD_Type()
)
swhL2PTPortConfigUDLD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTPortConfigUDLD.setStatus("mandatory")


class _SwhL2PTPortConfigClear_Type(Integer32):
    """Custom type swhL2PTPortConfigClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhL2PTPortConfigClear_Type.__name__ = "Integer32"
_SwhL2PTPortConfigClear_Object = MibTableColumn
swhL2PTPortConfigClear = _SwhL2PTPortConfigClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 37, 5, 1, 50),
    _SwhL2PTPortConfigClear_Type()
)
swhL2PTPortConfigClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTPortConfigClear.setStatus("mandatory")
_SwhRapidSpanningTree_ObjectIdentity = ObjectIdentity
swhRapidSpanningTree = _SwhRapidSpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40)
)
_SwhRSTPSwitchSettings_ObjectIdentity = ObjectIdentity
swhRSTPSwitchSettings = _SwhRSTPSwitchSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 3)
)


class _SwhRSTPSwitchSettingsSystemPriority_Type(Integer32):
    """Custom type swhRSTPSwitchSettingsSystemPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRSTPSwitchSettingsSystemPriority_Type.__name__ = "Integer32"
_SwhRSTPSwitchSettingsSystemPriority_Object = MibScalar
swhRSTPSwitchSettingsSystemPriority = _SwhRSTPSwitchSettingsSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 3, 6),
    _SwhRSTPSwitchSettingsSystemPriority_Type()
)
swhRSTPSwitchSettingsSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPSwitchSettingsSystemPriority.setStatus("mandatory")


class _SwhRSTPSwitchSettingsSystemPriorityIndex_Type(Integer32):
    """Custom type swhRSTPSwitchSettingsSystemPriorityIndex based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-4096", 1),
          ("priority-8192", 2),
          ("priority-12288", 3),
          ("priority-16384", 4),
          ("priority-20480", 5),
          ("priority-24576", 6),
          ("priority-28672", 7),
          ("priority-32768", 8),
          ("priority-36864", 9),
          ("priority-40960", 10),
          ("priority-45056", 11),
          ("priority-49152", 12),
          ("priority-53248", 13),
          ("priority-57344", 14),
          ("priority-61440", 15))
    )


_SwhRSTPSwitchSettingsSystemPriorityIndex_Type.__name__ = "Integer32"
_SwhRSTPSwitchSettingsSystemPriorityIndex_Object = MibScalar
swhRSTPSwitchSettingsSystemPriorityIndex = _SwhRSTPSwitchSettingsSystemPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 3, 9),
    _SwhRSTPSwitchSettingsSystemPriorityIndex_Type()
)
swhRSTPSwitchSettingsSystemPriorityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPSwitchSettingsSystemPriorityIndex.setStatus("mandatory")


class _SwhRSTPSwitchSettingsMaxAge_Type(Integer32):
    """Custom type swhRSTPSwitchSettingsMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 200),
    )


_SwhRSTPSwitchSettingsMaxAge_Type.__name__ = "Integer32"
_SwhRSTPSwitchSettingsMaxAge_Object = MibScalar
swhRSTPSwitchSettingsMaxAge = _SwhRSTPSwitchSettingsMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 3, 12),
    _SwhRSTPSwitchSettingsMaxAge_Type()
)
swhRSTPSwitchSettingsMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPSwitchSettingsMaxAge.setStatus("mandatory")


class _SwhRSTPSwitchSettingsHelloTime_Type(Integer32):
    """Custom type swhRSTPSwitchSettingsHelloTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SwhRSTPSwitchSettingsHelloTime_Type.__name__ = "Integer32"
_SwhRSTPSwitchSettingsHelloTime_Object = MibScalar
swhRSTPSwitchSettingsHelloTime = _SwhRSTPSwitchSettingsHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 3, 15),
    _SwhRSTPSwitchSettingsHelloTime_Type()
)
swhRSTPSwitchSettingsHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPSwitchSettingsHelloTime.setStatus("mandatory")


class _SwhRSTPSwitchSettingsForwardDelay_Type(Integer32):
    """Custom type swhRSTPSwitchSettingsForwardDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_SwhRSTPSwitchSettingsForwardDelay_Type.__name__ = "Integer32"
_SwhRSTPSwitchSettingsForwardDelay_Object = MibScalar
swhRSTPSwitchSettingsForwardDelay = _SwhRSTPSwitchSettingsForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 3, 18),
    _SwhRSTPSwitchSettingsForwardDelay_Type()
)
swhRSTPSwitchSettingsForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPSwitchSettingsForwardDelay.setStatus("mandatory")


class _SwhRSTPSwitchSettingsForceVersion_Type(Integer32):
    """Custom type swhRSTPSwitchSettingsForceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 0),
          ("normal", 1))
    )


_SwhRSTPSwitchSettingsForceVersion_Type.__name__ = "Integer32"
_SwhRSTPSwitchSettingsForceVersion_Object = MibScalar
swhRSTPSwitchSettingsForceVersion = _SwhRSTPSwitchSettingsForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 3, 21),
    _SwhRSTPSwitchSettingsForceVersion_Type()
)
swhRSTPSwitchSettingsForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPSwitchSettingsForceVersion.setStatus("mandatory")
_SwhRSTPAggregatedPortSettings_ObjectIdentity = ObjectIdentity
swhRSTPAggregatedPortSettings = _SwhRSTPAggregatedPortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 9)
)


class _SwhRSTPAggregatedPortSettingsState_Type(Integer32):
    """Custom type swhRSTPAggregatedPortSettingsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhRSTPAggregatedPortSettingsState_Type.__name__ = "Integer32"
_SwhRSTPAggregatedPortSettingsState_Object = MibScalar
swhRSTPAggregatedPortSettingsState = _SwhRSTPAggregatedPortSettingsState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 9, 3),
    _SwhRSTPAggregatedPortSettingsState_Type()
)
swhRSTPAggregatedPortSettingsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPAggregatedPortSettingsState.setStatus("mandatory")


class _SwhRSTPAggregatedPortSettingsCost_Type(Integer32):
    """Custom type swhRSTPAggregatedPortSettingsCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_SwhRSTPAggregatedPortSettingsCost_Type.__name__ = "Integer32"
_SwhRSTPAggregatedPortSettingsCost_Object = MibScalar
swhRSTPAggregatedPortSettingsCost = _SwhRSTPAggregatedPortSettingsCost_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 9, 6),
    _SwhRSTPAggregatedPortSettingsCost_Type()
)
swhRSTPAggregatedPortSettingsCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPAggregatedPortSettingsCost.setStatus("mandatory")


class _SwhRSTPAggregatedPortSettingsPriority_Type(Integer32):
    """Custom type swhRSTPAggregatedPortSettingsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRSTPAggregatedPortSettingsPriority_Type.__name__ = "Integer32"
_SwhRSTPAggregatedPortSettingsPriority_Object = MibScalar
swhRSTPAggregatedPortSettingsPriority = _SwhRSTPAggregatedPortSettingsPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 9, 9),
    _SwhRSTPAggregatedPortSettingsPriority_Type()
)
swhRSTPAggregatedPortSettingsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPAggregatedPortSettingsPriority.setStatus("mandatory")


class _SwhRSTPAggregatedPortSettingsPriorityIndex_Type(Integer32):
    """Custom type swhRSTPAggregatedPortSettingsPriorityIndex based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-16", 1),
          ("priority-32", 2),
          ("priority-48", 3),
          ("priority-64", 4),
          ("priority-80", 5),
          ("priority-96", 6),
          ("priority-112", 7),
          ("priority-128", 8),
          ("priority-144", 9),
          ("priority-160", 10),
          ("priority-176", 11),
          ("priority-192", 12),
          ("priority-208", 13),
          ("priority-224", 14),
          ("priority-240", 15))
    )


_SwhRSTPAggregatedPortSettingsPriorityIndex_Type.__name__ = "Integer32"
_SwhRSTPAggregatedPortSettingsPriorityIndex_Object = MibScalar
swhRSTPAggregatedPortSettingsPriorityIndex = _SwhRSTPAggregatedPortSettingsPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 9, 12),
    _SwhRSTPAggregatedPortSettingsPriorityIndex_Type()
)
swhRSTPAggregatedPortSettingsPriorityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPAggregatedPortSettingsPriorityIndex.setStatus("mandatory")


class _SwhRSTPAggregatedPortSettingsEdge_Type(Integer32):
    """Custom type swhRSTPAggregatedPortSettingsEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhRSTPAggregatedPortSettingsEdge_Type.__name__ = "Integer32"
_SwhRSTPAggregatedPortSettingsEdge_Object = MibScalar
swhRSTPAggregatedPortSettingsEdge = _SwhRSTPAggregatedPortSettingsEdge_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 9, 15),
    _SwhRSTPAggregatedPortSettingsEdge_Type()
)
swhRSTPAggregatedPortSettingsEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPAggregatedPortSettingsEdge.setStatus("mandatory")


class _SwhRSTPAggregatedPortSettingsPoint2point_Type(Integer32):
    """Custom type swhRSTPAggregatedPortSettingsPoint2point based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedtrue", 0),
          ("forcedfalse", 1),
          ("auto", 2))
    )


_SwhRSTPAggregatedPortSettingsPoint2point_Type.__name__ = "Integer32"
_SwhRSTPAggregatedPortSettingsPoint2point_Object = MibScalar
swhRSTPAggregatedPortSettingsPoint2point = _SwhRSTPAggregatedPortSettingsPoint2point_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 9, 18),
    _SwhRSTPAggregatedPortSettingsPoint2point_Type()
)
swhRSTPAggregatedPortSettingsPoint2point.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPAggregatedPortSettingsPoint2point.setStatus("mandatory")
_SwhRSTPPhysicalPortSettings_ObjectIdentity = ObjectIdentity
swhRSTPPhysicalPortSettings = _SwhRSTPPhysicalPortSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12)
)
_SwhRSTPPhysicalPortSettingsTable_Object = MibTable
swhRSTPPhysicalPortSettingsTable = _SwhRSTPPhysicalPortSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3)
)
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsTable.setStatus("mandatory")
_SwhRSTPPhysicalPortSettingsEntry_Object = MibTableRow
swhRSTPPhysicalPortSettingsEntry = _SwhRSTPPhysicalPortSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3, 1)
)
swhRSTPPhysicalPortSettingsEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhRSTPPhysicalPortSettingsIndex"),
)
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsEntry.setStatus("mandatory")


class _SwhRSTPPhysicalPortSettingsIndex_Type(Integer32):
    """Custom type swhRSTPPhysicalPortSettingsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRSTPPhysicalPortSettingsIndex_Type.__name__ = "Integer32"
_SwhRSTPPhysicalPortSettingsIndex_Object = MibTableColumn
swhRSTPPhysicalPortSettingsIndex = _SwhRSTPPhysicalPortSettingsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3, 1, 3),
    _SwhRSTPPhysicalPortSettingsIndex_Type()
)
swhRSTPPhysicalPortSettingsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsIndex.setStatus("mandatory")


class _SwhRSTPPhysicalPortSettingsState_Type(Integer32):
    """Custom type swhRSTPPhysicalPortSettingsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhRSTPPhysicalPortSettingsState_Type.__name__ = "Integer32"
_SwhRSTPPhysicalPortSettingsState_Object = MibTableColumn
swhRSTPPhysicalPortSettingsState = _SwhRSTPPhysicalPortSettingsState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3, 1, 6),
    _SwhRSTPPhysicalPortSettingsState_Type()
)
swhRSTPPhysicalPortSettingsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsState.setStatus("mandatory")


class _SwhRSTPPhysicalPortSettingsEdge_Type(Integer32):
    """Custom type swhRSTPPhysicalPortSettingsEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhRSTPPhysicalPortSettingsEdge_Type.__name__ = "Integer32"
_SwhRSTPPhysicalPortSettingsEdge_Object = MibTableColumn
swhRSTPPhysicalPortSettingsEdge = _SwhRSTPPhysicalPortSettingsEdge_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3, 1, 9),
    _SwhRSTPPhysicalPortSettingsEdge_Type()
)
swhRSTPPhysicalPortSettingsEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsEdge.setStatus("mandatory")


class _SwhRSTPPhysicalPortSettingsPathCost_Type(Integer32):
    """Custom type swhRSTPPhysicalPortSettingsPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_SwhRSTPPhysicalPortSettingsPathCost_Type.__name__ = "Integer32"
_SwhRSTPPhysicalPortSettingsPathCost_Object = MibTableColumn
swhRSTPPhysicalPortSettingsPathCost = _SwhRSTPPhysicalPortSettingsPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3, 1, 12),
    _SwhRSTPPhysicalPortSettingsPathCost_Type()
)
swhRSTPPhysicalPortSettingsPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsPathCost.setStatus("mandatory")


class _SwhRSTPPhysicalPortSettingsPriority_Type(Integer32):
    """Custom type swhRSTPPhysicalPortSettingsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRSTPPhysicalPortSettingsPriority_Type.__name__ = "Integer32"
_SwhRSTPPhysicalPortSettingsPriority_Object = MibTableColumn
swhRSTPPhysicalPortSettingsPriority = _SwhRSTPPhysicalPortSettingsPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3, 1, 15),
    _SwhRSTPPhysicalPortSettingsPriority_Type()
)
swhRSTPPhysicalPortSettingsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsPriority.setStatus("mandatory")


class _SwhRSTPPhysicalPortSettingsPriorityIndex_Type(Integer32):
    """Custom type swhRSTPPhysicalPortSettingsPriorityIndex based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("priority-0", 0),
          ("priority-16", 1),
          ("priority-32", 2),
          ("priority-48", 3),
          ("priority-64", 4),
          ("priority-80", 5),
          ("priority-96", 6),
          ("priority-112", 7),
          ("priority-128", 8),
          ("priority-144", 9),
          ("priority-160", 10),
          ("priority-176", 11),
          ("priority-192", 12),
          ("priority-208", 13),
          ("priority-224", 14),
          ("priority-240", 15))
    )


_SwhRSTPPhysicalPortSettingsPriorityIndex_Type.__name__ = "Integer32"
_SwhRSTPPhysicalPortSettingsPriorityIndex_Object = MibTableColumn
swhRSTPPhysicalPortSettingsPriorityIndex = _SwhRSTPPhysicalPortSettingsPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3, 1, 18),
    _SwhRSTPPhysicalPortSettingsPriorityIndex_Type()
)
swhRSTPPhysicalPortSettingsPriorityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsPriorityIndex.setStatus("mandatory")


class _SwhRSTPPhysicalPortSettingsPoint2point_Type(Integer32):
    """Custom type swhRSTPPhysicalPortSettingsPoint2point based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forcedtrue", 0),
          ("forcedfalse", 1),
          ("auto", 2))
    )


_SwhRSTPPhysicalPortSettingsPoint2point_Type.__name__ = "Integer32"
_SwhRSTPPhysicalPortSettingsPoint2point_Object = MibTableColumn
swhRSTPPhysicalPortSettingsPoint2point = _SwhRSTPPhysicalPortSettingsPoint2point_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 40, 12, 3, 1, 21),
    _SwhRSTPPhysicalPortSettingsPoint2point_Type()
)
swhRSTPPhysicalPortSettingsPoint2point.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRSTPPhysicalPortSettingsPoint2point.setStatus("mandatory")
_SwhLinkAggregation_ObjectIdentity = ObjectIdentity
swhLinkAggregation = _SwhLinkAggregation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45)
)
_SwhDistributionRule_ObjectIdentity = ObjectIdentity
swhDistributionRule = _SwhDistributionRule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 1)
)


class _SwhDistributionRuleSourceIPAddress_Type(Integer32):
    """Custom type swhDistributionRuleSourceIPAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDistributionRuleSourceIPAddress_Type.__name__ = "Integer32"
_SwhDistributionRuleSourceIPAddress_Object = MibScalar
swhDistributionRuleSourceIPAddress = _SwhDistributionRuleSourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 1, 1),
    _SwhDistributionRuleSourceIPAddress_Type()
)
swhDistributionRuleSourceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDistributionRuleSourceIPAddress.setStatus("mandatory")


class _SwhDistributionRuleDestinationIPAddress_Type(Integer32):
    """Custom type swhDistributionRuleDestinationIPAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDistributionRuleDestinationIPAddress_Type.__name__ = "Integer32"
_SwhDistributionRuleDestinationIPAddress_Object = MibScalar
swhDistributionRuleDestinationIPAddress = _SwhDistributionRuleDestinationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 1, 2),
    _SwhDistributionRuleDestinationIPAddress_Type()
)
swhDistributionRuleDestinationIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDistributionRuleDestinationIPAddress.setStatus("mandatory")


class _SwhDistributionRuleSourceL4Port_Type(Integer32):
    """Custom type swhDistributionRuleSourceL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDistributionRuleSourceL4Port_Type.__name__ = "Integer32"
_SwhDistributionRuleSourceL4Port_Object = MibScalar
swhDistributionRuleSourceL4Port = _SwhDistributionRuleSourceL4Port_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 1, 3),
    _SwhDistributionRuleSourceL4Port_Type()
)
swhDistributionRuleSourceL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDistributionRuleSourceL4Port.setStatus("mandatory")


class _SwhDistributionRuleDestinationL4Port_Type(Integer32):
    """Custom type swhDistributionRuleDestinationL4Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDistributionRuleDestinationL4Port_Type.__name__ = "Integer32"
_SwhDistributionRuleDestinationL4Port_Object = MibScalar
swhDistributionRuleDestinationL4Port = _SwhDistributionRuleDestinationL4Port_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 1, 4),
    _SwhDistributionRuleDestinationL4Port_Type()
)
swhDistributionRuleDestinationL4Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDistributionRuleDestinationL4Port.setStatus("mandatory")


class _SwhDistributionRuleSourceMACAddress_Type(Integer32):
    """Custom type swhDistributionRuleSourceMACAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDistributionRuleSourceMACAddress_Type.__name__ = "Integer32"
_SwhDistributionRuleSourceMACAddress_Object = MibScalar
swhDistributionRuleSourceMACAddress = _SwhDistributionRuleSourceMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 1, 5),
    _SwhDistributionRuleSourceMACAddress_Type()
)
swhDistributionRuleSourceMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDistributionRuleSourceMACAddress.setStatus("mandatory")


class _SwhDistributionRuleDestinationMACAddress_Type(Integer32):
    """Custom type swhDistributionRuleDestinationMACAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDistributionRuleDestinationMACAddress_Type.__name__ = "Integer32"
_SwhDistributionRuleDestinationMACAddress_Object = MibScalar
swhDistributionRuleDestinationMACAddress = _SwhDistributionRuleDestinationMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 1, 6),
    _SwhDistributionRuleDestinationMACAddress_Type()
)
swhDistributionRuleDestinationMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDistributionRuleDestinationMACAddress.setStatus("mandatory")
_SwhPortTrunkConfiguration_ObjectIdentity = ObjectIdentity
swhPortTrunkConfiguration = _SwhPortTrunkConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3)
)
_SwhPortTrunkConfigTable_Object = MibTable
swhPortTrunkConfigTable = _SwhPortTrunkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6)
)
if mibBuilder.loadTexts:
    swhPortTrunkConfigTable.setStatus("mandatory")
_SwhPortTrunkConfigEntry_Object = MibTableRow
swhPortTrunkConfigEntry = _SwhPortTrunkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1)
)
swhPortTrunkConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhPortTrunkConfigIndex"),
)
if mibBuilder.loadTexts:
    swhPortTrunkConfigEntry.setStatus("mandatory")


class _SwhPortTrunkConfigIndex_Type(Integer32):
    """Custom type swhPortTrunkConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhPortTrunkConfigIndex_Type.__name__ = "Integer32"
_SwhPortTrunkConfigIndex_Object = MibTableColumn
swhPortTrunkConfigIndex = _SwhPortTrunkConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 1),
    _SwhPortTrunkConfigIndex_Type()
)
swhPortTrunkConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhPortTrunkConfigIndex.setStatus("mandatory")


class _SwhPortTrunkConfigValid_Type(Integer32):
    """Custom type swhPortTrunkConfigValid based on Integer32"""
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


_SwhPortTrunkConfigValid_Type.__name__ = "Integer32"
_SwhPortTrunkConfigValid_Object = MibTableColumn
swhPortTrunkConfigValid = _SwhPortTrunkConfigValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 2),
    _SwhPortTrunkConfigValid_Type()
)
swhPortTrunkConfigValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortTrunkConfigValid.setStatus("mandatory")
_SwhPortTrunkConfigGroupName_Type = DisplayString
_SwhPortTrunkConfigGroupName_Object = MibTableColumn
swhPortTrunkConfigGroupName = _SwhPortTrunkConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 4),
    _SwhPortTrunkConfigGroupName_Type()
)
swhPortTrunkConfigGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortTrunkConfigGroupName.setStatus("mandatory")


class _SwhPortTrunkConfigPort1_Type(Integer32):
    """Custom type swhPortTrunkConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortTrunkConfigPort1_Type.__name__ = "Integer32"
_SwhPortTrunkConfigPort1_Object = MibTableColumn
swhPortTrunkConfigPort1 = _SwhPortTrunkConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 5),
    _SwhPortTrunkConfigPort1_Type()
)
swhPortTrunkConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortTrunkConfigPort1.setStatus("mandatory")


class _SwhPortTrunkConfigPort2_Type(Integer32):
    """Custom type swhPortTrunkConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortTrunkConfigPort2_Type.__name__ = "Integer32"
_SwhPortTrunkConfigPort2_Object = MibTableColumn
swhPortTrunkConfigPort2 = _SwhPortTrunkConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 6),
    _SwhPortTrunkConfigPort2_Type()
)
swhPortTrunkConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortTrunkConfigPort2.setStatus("mandatory")


class _SwhPortTrunkConfigPort3_Type(Integer32):
    """Custom type swhPortTrunkConfigPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortTrunkConfigPort3_Type.__name__ = "Integer32"
_SwhPortTrunkConfigPort3_Object = MibTableColumn
swhPortTrunkConfigPort3 = _SwhPortTrunkConfigPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 7),
    _SwhPortTrunkConfigPort3_Type()
)
swhPortTrunkConfigPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortTrunkConfigPort3.setStatus("mandatory")


class _SwhPortTrunkConfigPort4_Type(Integer32):
    """Custom type swhPortTrunkConfigPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortTrunkConfigPort4_Type.__name__ = "Integer32"
_SwhPortTrunkConfigPort4_Object = MibTableColumn
swhPortTrunkConfigPort4 = _SwhPortTrunkConfigPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 8),
    _SwhPortTrunkConfigPort4_Type()
)
swhPortTrunkConfigPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortTrunkConfigPort4.setStatus("mandatory")


class _SwhPortTrunkConfigPort5_Type(Integer32):
    """Custom type swhPortTrunkConfigPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortTrunkConfigPort5_Type.__name__ = "Integer32"
_SwhPortTrunkConfigPort5_Object = MibTableColumn
swhPortTrunkConfigPort5 = _SwhPortTrunkConfigPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 9),
    _SwhPortTrunkConfigPort5_Type()
)
swhPortTrunkConfigPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortTrunkConfigPort5.setStatus("mandatory")


class _SwhPortTrunkConfigPort6_Type(Integer32):
    """Custom type swhPortTrunkConfigPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhPortTrunkConfigPort6_Type.__name__ = "Integer32"
_SwhPortTrunkConfigPort6_Object = MibTableColumn
swhPortTrunkConfigPort6 = _SwhPortTrunkConfigPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 10),
    _SwhPortTrunkConfigPort6_Type()
)
swhPortTrunkConfigPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortTrunkConfigPort6.setStatus("mandatory")


class _SwhPortTrunkConfigDelete_Type(Integer32):
    """Custom type swhPortTrunkConfigDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhPortTrunkConfigDelete_Type.__name__ = "Integer32"
_SwhPortTrunkConfigDelete_Object = MibTableColumn
swhPortTrunkConfigDelete = _SwhPortTrunkConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 3, 6, 1, 56),
    _SwhPortTrunkConfigDelete_Type()
)
swhPortTrunkConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortTrunkConfigDelete.setStatus("mandatory")
_SwhLACPPortConfiguration_ObjectIdentity = ObjectIdentity
swhLACPPortConfiguration = _SwhLACPPortConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 6)
)
_SwhLACPPortConfigTable_Object = MibTable
swhLACPPortConfigTable = _SwhLACPPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 6, 1)
)
if mibBuilder.loadTexts:
    swhLACPPortConfigTable.setStatus("mandatory")
_SwhLACPPortConfigEntry_Object = MibTableRow
swhLACPPortConfigEntry = _SwhLACPPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 6, 1, 1)
)
swhLACPPortConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhLACPPortConfigIndex"),
)
if mibBuilder.loadTexts:
    swhLACPPortConfigEntry.setStatus("mandatory")


class _SwhLACPPortConfigIndex_Type(Integer32):
    """Custom type swhLACPPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhLACPPortConfigIndex_Type.__name__ = "Integer32"
_SwhLACPPortConfigIndex_Object = MibTableColumn
swhLACPPortConfigIndex = _SwhLACPPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 6, 1, 1, 3),
    _SwhLACPPortConfigIndex_Type()
)
swhLACPPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhLACPPortConfigIndex.setStatus("mandatory")


class _SwhLACPPortConfigKeyValue_Type(Integer32):
    """Custom type swhLACPPortConfigKeyValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SwhLACPPortConfigKeyValue_Type.__name__ = "Integer32"
_SwhLACPPortConfigKeyValue_Object = MibTableColumn
swhLACPPortConfigKeyValue = _SwhLACPPortConfigKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 6, 1, 1, 9),
    _SwhLACPPortConfigKeyValue_Type()
)
swhLACPPortConfigKeyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLACPPortConfigKeyValue.setStatus("mandatory")


class _SwhLACPPortConfigRole_Type(Integer32):
    """Custom type swhLACPPortConfigRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("passive", 1),
          ("active", 2))
    )


_SwhLACPPortConfigRole_Type.__name__ = "Integer32"
_SwhLACPPortConfigRole_Object = MibTableColumn
swhLACPPortConfigRole = _SwhLACPPortConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 45, 6, 1, 1, 12),
    _SwhLACPPortConfigRole_Type()
)
swhLACPPortConfigRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLACPPortConfigRole.setStatus("mandatory")
_SwhIGMPSnooping_ObjectIdentity = ObjectIdentity
swhIGMPSnooping = _SwhIGMPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50)
)
_SwhIGMPConfiguration_ObjectIdentity = ObjectIdentity
swhIGMPConfiguration = _SwhIGMPConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1)
)


class _SwhIGMPConfigSnooping_Type(Integer32):
    """Custom type swhIGMPConfigSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhIGMPConfigSnooping_Type.__name__ = "Integer32"
_SwhIGMPConfigSnooping_Object = MibScalar
swhIGMPConfigSnooping = _SwhIGMPConfigSnooping_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 1),
    _SwhIGMPConfigSnooping_Type()
)
swhIGMPConfigSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigSnooping.setStatus("mandatory")


class _SwhIGMPConfigFastLeave_Type(Integer32):
    """Custom type swhIGMPConfigFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhIGMPConfigFastLeave_Type.__name__ = "Integer32"
_SwhIGMPConfigFastLeave_Object = MibScalar
swhIGMPConfigFastLeave = _SwhIGMPConfigFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 2),
    _SwhIGMPConfigFastLeave_Type()
)
swhIGMPConfigFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigFastLeave.setStatus("mandatory")


class _SwhIGMPConfigRouterPort1_Type(Integer32):
    """Custom type swhIGMPConfigRouterPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPConfigRouterPort1_Type.__name__ = "Integer32"
_SwhIGMPConfigRouterPort1_Object = MibScalar
swhIGMPConfigRouterPort1 = _SwhIGMPConfigRouterPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 5),
    _SwhIGMPConfigRouterPort1_Type()
)
swhIGMPConfigRouterPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigRouterPort1.setStatus("mandatory")


class _SwhIGMPConfigRouterPort2_Type(Integer32):
    """Custom type swhIGMPConfigRouterPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPConfigRouterPort2_Type.__name__ = "Integer32"
_SwhIGMPConfigRouterPort2_Object = MibScalar
swhIGMPConfigRouterPort2 = _SwhIGMPConfigRouterPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 6),
    _SwhIGMPConfigRouterPort2_Type()
)
swhIGMPConfigRouterPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigRouterPort2.setStatus("mandatory")


class _SwhIGMPConfigRouterPort3_Type(Integer32):
    """Custom type swhIGMPConfigRouterPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPConfigRouterPort3_Type.__name__ = "Integer32"
_SwhIGMPConfigRouterPort3_Object = MibScalar
swhIGMPConfigRouterPort3 = _SwhIGMPConfigRouterPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 7),
    _SwhIGMPConfigRouterPort3_Type()
)
swhIGMPConfigRouterPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigRouterPort3.setStatus("mandatory")


class _SwhIGMPConfigRouterPort4_Type(Integer32):
    """Custom type swhIGMPConfigRouterPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPConfigRouterPort4_Type.__name__ = "Integer32"
_SwhIGMPConfigRouterPort4_Object = MibScalar
swhIGMPConfigRouterPort4 = _SwhIGMPConfigRouterPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 8),
    _SwhIGMPConfigRouterPort4_Type()
)
swhIGMPConfigRouterPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigRouterPort4.setStatus("mandatory")


class _SwhIGMPConfigRouterPort5_Type(Integer32):
    """Custom type swhIGMPConfigRouterPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPConfigRouterPort5_Type.__name__ = "Integer32"
_SwhIGMPConfigRouterPort5_Object = MibScalar
swhIGMPConfigRouterPort5 = _SwhIGMPConfigRouterPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 9),
    _SwhIGMPConfigRouterPort5_Type()
)
swhIGMPConfigRouterPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigRouterPort5.setStatus("mandatory")


class _SwhIGMPConfigRouterPort6_Type(Integer32):
    """Custom type swhIGMPConfigRouterPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPConfigRouterPort6_Type.__name__ = "Integer32"
_SwhIGMPConfigRouterPort6_Object = MibScalar
swhIGMPConfigRouterPort6 = _SwhIGMPConfigRouterPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 10),
    _SwhIGMPConfigRouterPort6_Type()
)
swhIGMPConfigRouterPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigRouterPort6.setStatus("mandatory")


class _SwhIGMPConfigUnregisteredIPMCFlooding_Type(Integer32):
    """Custom type swhIGMPConfigUnregisteredIPMCFlooding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhIGMPConfigUnregisteredIPMCFlooding_Type.__name__ = "Integer32"
_SwhIGMPConfigUnregisteredIPMCFlooding_Object = MibScalar
swhIGMPConfigUnregisteredIPMCFlooding = _SwhIGMPConfigUnregisteredIPMCFlooding_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 56),
    _SwhIGMPConfigUnregisteredIPMCFlooding_Type()
)
swhIGMPConfigUnregisteredIPMCFlooding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigUnregisteredIPMCFlooding.setStatus("mandatory")


class _SwhIGMPConfigQueryResponseInterval_Type(Integer32):
    """Custom type swhIGMPConfigQueryResponseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SwhIGMPConfigQueryResponseInterval_Type.__name__ = "Integer32"
_SwhIGMPConfigQueryResponseInterval_Object = MibScalar
swhIGMPConfigQueryResponseInterval = _SwhIGMPConfigQueryResponseInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 57),
    _SwhIGMPConfigQueryResponseInterval_Type()
)
swhIGMPConfigQueryResponseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigQueryResponseInterval.setStatus("mandatory")


class _SwhIGMPConfigQueryInterval_Type(Integer32):
    """Custom type swhIGMPConfigQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6000),
    )


_SwhIGMPConfigQueryInterval_Type.__name__ = "Integer32"
_SwhIGMPConfigQueryInterval_Object = MibScalar
swhIGMPConfigQueryInterval = _SwhIGMPConfigQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 58),
    _SwhIGMPConfigQueryInterval_Type()
)
swhIGMPConfigQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigQueryInterval.setStatus("mandatory")


class _SwhIGMPConfigSnoopingV3_Type(Integer32):
    """Custom type swhIGMPConfigSnoopingV3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhIGMPConfigSnoopingV3_Type.__name__ = "Integer32"
_SwhIGMPConfigSnoopingV3_Object = MibScalar
swhIGMPConfigSnoopingV3 = _SwhIGMPConfigSnoopingV3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 1, 60),
    _SwhIGMPConfigSnoopingV3_Type()
)
swhIGMPConfigSnoopingV3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPConfigSnoopingV3.setStatus("mandatory")
_SwhIGMPVIDConfiguration_ObjectIdentity = ObjectIdentity
swhIGMPVIDConfiguration = _SwhIGMPVIDConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 5)
)
_SwhIGMPVIDConfigTable_Object = MibTable
swhIGMPVIDConfigTable = _SwhIGMPVIDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 5, 1)
)
if mibBuilder.loadTexts:
    swhIGMPVIDConfigTable.setStatus("mandatory")
_SwhIGMPVIDConfigEntry_Object = MibTableRow
swhIGMPVIDConfigEntry = _SwhIGMPVIDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 5, 1, 1)
)
swhIGMPVIDConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhIGMPVIDConfigIndex"),
)
if mibBuilder.loadTexts:
    swhIGMPVIDConfigEntry.setStatus("mandatory")


class _SwhIGMPVIDConfigIndex_Type(Integer32):
    """Custom type swhIGMPVIDConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhIGMPVIDConfigIndex_Type.__name__ = "Integer32"
_SwhIGMPVIDConfigIndex_Object = MibTableColumn
swhIGMPVIDConfigIndex = _SwhIGMPVIDConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 5, 1, 1, 1),
    _SwhIGMPVIDConfigIndex_Type()
)
swhIGMPVIDConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhIGMPVIDConfigIndex.setStatus("mandatory")
_SwhIGMPVIDConfigVLANName_Type = DisplayString
_SwhIGMPVIDConfigVLANName_Object = MibTableColumn
swhIGMPVIDConfigVLANName = _SwhIGMPVIDConfigVLANName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 5, 1, 1, 5),
    _SwhIGMPVIDConfigVLANName_Type()
)
swhIGMPVIDConfigVLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPVIDConfigVLANName.setStatus("mandatory")
_SwhIGMPVIDConfigVLANID_Type = Integer32
_SwhIGMPVIDConfigVLANID_Object = MibTableColumn
swhIGMPVIDConfigVLANID = _SwhIGMPVIDConfigVLANID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 5, 1, 1, 7),
    _SwhIGMPVIDConfigVLANID_Type()
)
swhIGMPVIDConfigVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPVIDConfigVLANID.setStatus("mandatory")


class _SwhIGMPVIDConfigSnooping_Type(Integer32):
    """Custom type swhIGMPVIDConfigSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPVIDConfigSnooping_Type.__name__ = "Integer32"
_SwhIGMPVIDConfigSnooping_Object = MibTableColumn
swhIGMPVIDConfigSnooping = _SwhIGMPVIDConfigSnooping_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 5, 1, 1, 9),
    _SwhIGMPVIDConfigSnooping_Type()
)
swhIGMPVIDConfigSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPVIDConfigSnooping.setStatus("mandatory")


class _SwhIGMPVIDConfigQuerying_Type(Integer32):
    """Custom type swhIGMPVIDConfigQuerying based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPVIDConfigQuerying_Type.__name__ = "Integer32"
_SwhIGMPVIDConfigQuerying_Object = MibTableColumn
swhIGMPVIDConfigQuerying = _SwhIGMPVIDConfigQuerying_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 5, 1, 1, 11),
    _SwhIGMPVIDConfigQuerying_Type()
)
swhIGMPVIDConfigQuerying.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPVIDConfigQuerying.setStatus("mandatory")
_SwhIPMCSegment_ObjectIdentity = ObjectIdentity
swhIPMCSegment = _SwhIPMCSegment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7)
)
_SwhIPMCSegmentTable_Object = MibTable
swhIPMCSegmentTable = _SwhIPMCSegmentTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1)
)
if mibBuilder.loadTexts:
    swhIPMCSegmentTable.setStatus("mandatory")
_SwhIPMCSegmentEntry_Object = MibTableRow
swhIPMCSegmentEntry = _SwhIPMCSegmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1, 1)
)
swhIPMCSegmentEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhIPMCSegmentIndex"),
)
if mibBuilder.loadTexts:
    swhIPMCSegmentEntry.setStatus("mandatory")


class _SwhIPMCSegmentIndex_Type(Integer32):
    """Custom type swhIPMCSegmentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhIPMCSegmentIndex_Type.__name__ = "Integer32"
_SwhIPMCSegmentIndex_Object = MibTableColumn
swhIPMCSegmentIndex = _SwhIPMCSegmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1, 1, 1),
    _SwhIPMCSegmentIndex_Type()
)
swhIPMCSegmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhIPMCSegmentIndex.setStatus("mandatory")


class _SwhIPMCSegmentValid_Type(Integer32):
    """Custom type swhIPMCSegmentValid based on Integer32"""
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


_SwhIPMCSegmentValid_Type.__name__ = "Integer32"
_SwhIPMCSegmentValid_Object = MibTableColumn
swhIPMCSegmentValid = _SwhIPMCSegmentValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1, 1, 2),
    _SwhIPMCSegmentValid_Type()
)
swhIPMCSegmentValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIPMCSegmentValid.setStatus("mandatory")


class _SwhIPMCSegmentSegmentID_Type(Integer32):
    """Custom type swhIPMCSegmentSegmentID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCSegmentSegmentID_Type.__name__ = "Integer32"
_SwhIPMCSegmentSegmentID_Object = MibTableColumn
swhIPMCSegmentSegmentID = _SwhIPMCSegmentSegmentID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1, 1, 3),
    _SwhIPMCSegmentSegmentID_Type()
)
swhIPMCSegmentSegmentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCSegmentSegmentID.setStatus("mandatory")
_SwhIPMCSegmentSegmentName_Type = DisplayString
_SwhIPMCSegmentSegmentName_Object = MibTableColumn
swhIPMCSegmentSegmentName = _SwhIPMCSegmentSegmentName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1, 1, 4),
    _SwhIPMCSegmentSegmentName_Type()
)
swhIPMCSegmentSegmentName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCSegmentSegmentName.setStatus("mandatory")
_SwhIPMCSegmentIPRange1_Type = IpAddress
_SwhIPMCSegmentIPRange1_Object = MibTableColumn
swhIPMCSegmentIPRange1 = _SwhIPMCSegmentIPRange1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1, 1, 5),
    _SwhIPMCSegmentIPRange1_Type()
)
swhIPMCSegmentIPRange1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCSegmentIPRange1.setStatus("mandatory")
_SwhIPMCSegmentIPRange2_Type = IpAddress
_SwhIPMCSegmentIPRange2_Object = MibTableColumn
swhIPMCSegmentIPRange2 = _SwhIPMCSegmentIPRange2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1, 1, 6),
    _SwhIPMCSegmentIPRange2_Type()
)
swhIPMCSegmentIPRange2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCSegmentIPRange2.setStatus("mandatory")


class _SwhIPMCSegmentDelete_Type(Integer32):
    """Custom type swhIPMCSegmentDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhIPMCSegmentDelete_Type.__name__ = "Integer32"
_SwhIPMCSegmentDelete_Object = MibTableColumn
swhIPMCSegmentDelete = _SwhIPMCSegmentDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 7, 1, 1, 10),
    _SwhIPMCSegmentDelete_Type()
)
swhIPMCSegmentDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCSegmentDelete.setStatus("mandatory")
_SwhIPMCProfile_ObjectIdentity = ObjectIdentity
swhIPMCProfile = _SwhIPMCProfile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8)
)
_SwhIPMCProfileTable_Object = MibTable
swhIPMCProfileTable = _SwhIPMCProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1)
)
if mibBuilder.loadTexts:
    swhIPMCProfileTable.setStatus("mandatory")
_SwhIPMCProfileEntry_Object = MibTableRow
swhIPMCProfileEntry = _SwhIPMCProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1)
)
swhIPMCProfileEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhIPMCProfileIndex"),
)
if mibBuilder.loadTexts:
    swhIPMCProfileEntry.setStatus("mandatory")


class _SwhIPMCProfileIndex_Type(Integer32):
    """Custom type swhIPMCProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhIPMCProfileIndex_Type.__name__ = "Integer32"
_SwhIPMCProfileIndex_Object = MibTableColumn
swhIPMCProfileIndex = _SwhIPMCProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 1),
    _SwhIPMCProfileIndex_Type()
)
swhIPMCProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhIPMCProfileIndex.setStatus("mandatory")


class _SwhIPMCProfileValid_Type(Integer32):
    """Custom type swhIPMCProfileValid based on Integer32"""
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


_SwhIPMCProfileValid_Type.__name__ = "Integer32"
_SwhIPMCProfileValid_Object = MibTableColumn
swhIPMCProfileValid = _SwhIPMCProfileValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 2),
    _SwhIPMCProfileValid_Type()
)
swhIPMCProfileValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIPMCProfileValid.setStatus("mandatory")
_SwhIPMCProfileProfileName_Type = DisplayString
_SwhIPMCProfileProfileName_Object = MibTableColumn
swhIPMCProfileProfileName = _SwhIPMCProfileProfileName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 3),
    _SwhIPMCProfileProfileName_Type()
)
swhIPMCProfileProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileProfileName.setStatus("mandatory")


class _SwhIPMCProfileSegment1_Type(Integer32):
    """Custom type swhIPMCProfileSegment1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment1_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment1_Object = MibTableColumn
swhIPMCProfileSegment1 = _SwhIPMCProfileSegment1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 4),
    _SwhIPMCProfileSegment1_Type()
)
swhIPMCProfileSegment1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment1.setStatus("mandatory")


class _SwhIPMCProfileSegment2_Type(Integer32):
    """Custom type swhIPMCProfileSegment2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment2_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment2_Object = MibTableColumn
swhIPMCProfileSegment2 = _SwhIPMCProfileSegment2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 5),
    _SwhIPMCProfileSegment2_Type()
)
swhIPMCProfileSegment2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment2.setStatus("mandatory")


class _SwhIPMCProfileSegment3_Type(Integer32):
    """Custom type swhIPMCProfileSegment3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment3_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment3_Object = MibTableColumn
swhIPMCProfileSegment3 = _SwhIPMCProfileSegment3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 6),
    _SwhIPMCProfileSegment3_Type()
)
swhIPMCProfileSegment3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment3.setStatus("mandatory")


class _SwhIPMCProfileSegment4_Type(Integer32):
    """Custom type swhIPMCProfileSegment4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment4_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment4_Object = MibTableColumn
swhIPMCProfileSegment4 = _SwhIPMCProfileSegment4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 7),
    _SwhIPMCProfileSegment4_Type()
)
swhIPMCProfileSegment4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment4.setStatus("mandatory")


class _SwhIPMCProfileSegment5_Type(Integer32):
    """Custom type swhIPMCProfileSegment5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment5_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment5_Object = MibTableColumn
swhIPMCProfileSegment5 = _SwhIPMCProfileSegment5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 8),
    _SwhIPMCProfileSegment5_Type()
)
swhIPMCProfileSegment5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment5.setStatus("mandatory")


class _SwhIPMCProfileSegment6_Type(Integer32):
    """Custom type swhIPMCProfileSegment6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment6_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment6_Object = MibTableColumn
swhIPMCProfileSegment6 = _SwhIPMCProfileSegment6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 9),
    _SwhIPMCProfileSegment6_Type()
)
swhIPMCProfileSegment6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment6.setStatus("mandatory")


class _SwhIPMCProfileSegment7_Type(Integer32):
    """Custom type swhIPMCProfileSegment7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment7_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment7_Object = MibTableColumn
swhIPMCProfileSegment7 = _SwhIPMCProfileSegment7_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 10),
    _SwhIPMCProfileSegment7_Type()
)
swhIPMCProfileSegment7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment7.setStatus("mandatory")


class _SwhIPMCProfileSegment8_Type(Integer32):
    """Custom type swhIPMCProfileSegment8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment8_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment8_Object = MibTableColumn
swhIPMCProfileSegment8 = _SwhIPMCProfileSegment8_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 11),
    _SwhIPMCProfileSegment8_Type()
)
swhIPMCProfileSegment8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment8.setStatus("mandatory")


class _SwhIPMCProfileSegment9_Type(Integer32):
    """Custom type swhIPMCProfileSegment9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment9_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment9_Object = MibTableColumn
swhIPMCProfileSegment9 = _SwhIPMCProfileSegment9_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 12),
    _SwhIPMCProfileSegment9_Type()
)
swhIPMCProfileSegment9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment9.setStatus("mandatory")


class _SwhIPMCProfileSegment10_Type(Integer32):
    """Custom type swhIPMCProfileSegment10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SwhIPMCProfileSegment10_Type.__name__ = "Integer32"
_SwhIPMCProfileSegment10_Object = MibTableColumn
swhIPMCProfileSegment10 = _SwhIPMCProfileSegment10_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 13),
    _SwhIPMCProfileSegment10_Type()
)
swhIPMCProfileSegment10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileSegment10.setStatus("mandatory")


class _SwhIPMCProfileDelete_Type(Integer32):
    """Custom type swhIPMCProfileDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhIPMCProfileDelete_Type.__name__ = "Integer32"
_SwhIPMCProfileDelete_Object = MibTableColumn
swhIPMCProfileDelete = _SwhIPMCProfileDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 8, 1, 1, 15),
    _SwhIPMCProfileDelete_Type()
)
swhIPMCProfileDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPMCProfileDelete.setStatus("mandatory")
_SwhIGMPFiltering_ObjectIdentity = ObjectIdentity
swhIGMPFiltering = _SwhIGMPFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9)
)
_SwhIGMPFilterTable_Object = MibTable
swhIGMPFilterTable = _SwhIGMPFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1)
)
if mibBuilder.loadTexts:
    swhIGMPFilterTable.setStatus("mandatory")
_SwhIGMPFilterEntry_Object = MibTableRow
swhIGMPFilterEntry = _SwhIGMPFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1)
)
swhIGMPFilterEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhIGMPFilterIndex"),
)
if mibBuilder.loadTexts:
    swhIGMPFilterEntry.setStatus("mandatory")


class _SwhIGMPFilterIndex_Type(Integer32):
    """Custom type swhIGMPFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhIGMPFilterIndex_Type.__name__ = "Integer32"
_SwhIGMPFilterIndex_Object = MibTableColumn
swhIGMPFilterIndex = _SwhIGMPFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1, 1),
    _SwhIGMPFilterIndex_Type()
)
swhIGMPFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhIGMPFilterIndex.setStatus("mandatory")


class _SwhIGMPFilterEnable_Type(Integer32):
    """Custom type swhIGMPFilterEnable based on Integer32"""
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


_SwhIGMPFilterEnable_Type.__name__ = "Integer32"
_SwhIGMPFilterEnable_Object = MibTableColumn
swhIGMPFilterEnable = _SwhIGMPFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1, 3),
    _SwhIGMPFilterEnable_Type()
)
swhIGMPFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPFilterEnable.setStatus("mandatory")
_SwhIGMPFilterPortName_Type = DisplayString
_SwhIGMPFilterPortName_Object = MibTableColumn
swhIGMPFilterPortName = _SwhIGMPFilterPortName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1, 4),
    _SwhIGMPFilterPortName_Type()
)
swhIGMPFilterPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPFilterPortName.setStatus("mandatory")
_SwhIGMPFilterIPMCProfile1_Type = DisplayString
_SwhIGMPFilterIPMCProfile1_Object = MibTableColumn
swhIGMPFilterIPMCProfile1 = _SwhIGMPFilterIPMCProfile1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1, 6),
    _SwhIGMPFilterIPMCProfile1_Type()
)
swhIGMPFilterIPMCProfile1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPFilterIPMCProfile1.setStatus("mandatory")
_SwhIGMPFilterIPMCProfile2_Type = DisplayString
_SwhIGMPFilterIPMCProfile2_Object = MibTableColumn
swhIGMPFilterIPMCProfile2 = _SwhIGMPFilterIPMCProfile2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1, 7),
    _SwhIGMPFilterIPMCProfile2_Type()
)
swhIGMPFilterIPMCProfile2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPFilterIPMCProfile2.setStatus("mandatory")
_SwhIGMPFilterIPMCProfile3_Type = DisplayString
_SwhIGMPFilterIPMCProfile3_Object = MibTableColumn
swhIGMPFilterIPMCProfile3 = _SwhIGMPFilterIPMCProfile3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1, 8),
    _SwhIGMPFilterIPMCProfile3_Type()
)
swhIGMPFilterIPMCProfile3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPFilterIPMCProfile3.setStatus("mandatory")
_SwhIGMPFilterIPMCProfile4_Type = DisplayString
_SwhIGMPFilterIPMCProfile4_Object = MibTableColumn
swhIGMPFilterIPMCProfile4 = _SwhIGMPFilterIPMCProfile4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1, 9),
    _SwhIGMPFilterIPMCProfile4_Type()
)
swhIGMPFilterIPMCProfile4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPFilterIPMCProfile4.setStatus("mandatory")


class _SwhIGMPFilterChannelLimit_Type(Integer32):
    """Custom type swhIGMPFilterChannelLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_SwhIGMPFilterChannelLimit_Type.__name__ = "Integer32"
_SwhIGMPFilterChannelLimit_Object = MibTableColumn
swhIGMPFilterChannelLimit = _SwhIGMPFilterChannelLimit_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 1, 1, 10),
    _SwhIGMPFilterChannelLimit_Type()
)
swhIGMPFilterChannelLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPFilterChannelLimit.setStatus("mandatory")


class _SwhIGMPFilterState_Type(Integer32):
    """Custom type swhIGMPFilterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhIGMPFilterState_Type.__name__ = "Integer32"
_SwhIGMPFilterState_Object = MibScalar
swhIGMPFilterState = _SwhIGMPFilterState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 50, 9, 2),
    _SwhIGMPFilterState_Type()
)
swhIGMPFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIGMPFilterState.setStatus("mandatory")
_Swh8021XConfiguration_ObjectIdentity = ObjectIdentity
swh8021XConfiguration = _Swh8021XConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55)
)
_Swh8021XSystemConfig_ObjectIdentity = ObjectIdentity
swh8021XSystemConfig = _Swh8021XSystemConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 3)
)


class _Swh8021XSystemConfigMode_Type(Integer32):
    """Custom type swh8021XSystemConfigMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Swh8021XSystemConfigMode_Type.__name__ = "Integer32"
_Swh8021XSystemConfigMode_Object = MibScalar
swh8021XSystemConfigMode = _Swh8021XSystemConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 3, 1),
    _Swh8021XSystemConfigMode_Type()
)
swh8021XSystemConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XSystemConfigMode.setStatus("mandatory")
_Swh8021XSystemConfigRADIUSIP_Type = DisplayString
_Swh8021XSystemConfigRADIUSIP_Object = MibScalar
swh8021XSystemConfigRADIUSIP = _Swh8021XSystemConfigRADIUSIP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 3, 3),
    _Swh8021XSystemConfigRADIUSIP_Type()
)
swh8021XSystemConfigRADIUSIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XSystemConfigRADIUSIP.setStatus("mandatory")
_Swh8021XSystemConfigRADIUSSecret_Type = DisplayString
_Swh8021XSystemConfigRADIUSSecret_Object = MibScalar
swh8021XSystemConfigRADIUSSecret = _Swh8021XSystemConfigRADIUSSecret_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 3, 5),
    _Swh8021XSystemConfigRADIUSSecret_Type()
)
swh8021XSystemConfigRADIUSSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XSystemConfigRADIUSSecret.setStatus("mandatory")


class _Swh8021XSystemConfigRauthenticationEn_Type(Integer32):
    """Custom type swh8021XSystemConfigRauthenticationEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Swh8021XSystemConfigRauthenticationEn_Type.__name__ = "Integer32"
_Swh8021XSystemConfigRauthenticationEn_Object = MibScalar
swh8021XSystemConfigRauthenticationEn = _Swh8021XSystemConfigRauthenticationEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 3, 9),
    _Swh8021XSystemConfigRauthenticationEn_Type()
)
swh8021XSystemConfigRauthenticationEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XSystemConfigRauthenticationEn.setStatus("mandatory")


class _Swh8021XSystemConfigRadiusAssignedVLANEn_Type(Integer32):
    """Custom type swh8021XSystemConfigRadiusAssignedVLANEn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Swh8021XSystemConfigRadiusAssignedVLANEn_Type.__name__ = "Integer32"
_Swh8021XSystemConfigRadiusAssignedVLANEn_Object = MibScalar
swh8021XSystemConfigRadiusAssignedVLANEn = _Swh8021XSystemConfigRadiusAssignedVLANEn_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 3, 15),
    _Swh8021XSystemConfigRadiusAssignedVLANEn_Type()
)
swh8021XSystemConfigRadiusAssignedVLANEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XSystemConfigRadiusAssignedVLANEn.setStatus("mandatory")
_Swh8021XPortConfig_ObjectIdentity = ObjectIdentity
swh8021XPortConfig = _Swh8021XPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6)
)
_Swh8021XPortConfigTable_Object = MibTable
swh8021XPortConfigTable = _Swh8021XPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1)
)
if mibBuilder.loadTexts:
    swh8021XPortConfigTable.setStatus("mandatory")
_Swh8021XPortConfigEntry_Object = MibTableRow
swh8021XPortConfigEntry = _Swh8021XPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1)
)
swh8021XPortConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swh8021XPortConfigIndex"),
)
if mibBuilder.loadTexts:
    swh8021XPortConfigEntry.setStatus("mandatory")


class _Swh8021XPortConfigIndex_Type(Integer32):
    """Custom type swh8021XPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Swh8021XPortConfigIndex_Type.__name__ = "Integer32"
_Swh8021XPortConfigIndex_Object = MibTableColumn
swh8021XPortConfigIndex = _Swh8021XPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 1),
    _Swh8021XPortConfigIndex_Type()
)
swh8021XPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swh8021XPortConfigIndex.setStatus("mandatory")


class _Swh8021XPortConfigAdminState_Type(Integer32):
    """Custom type swh8021XPortConfigAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("authorized", 1),
          ("unauthorized", 2))
    )


_Swh8021XPortConfigAdminState_Type.__name__ = "Integer32"
_Swh8021XPortConfigAdminState_Object = MibTableColumn
swh8021XPortConfigAdminState = _Swh8021XPortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 3),
    _Swh8021XPortConfigAdminState_Type()
)
swh8021XPortConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XPortConfigAdminState.setStatus("mandatory")


class _Swh8021XPortConfigReauthenticate_Type(Integer32):
    """Custom type swh8021XPortConfigReauthenticate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Swh8021XPortConfigReauthenticate_Type.__name__ = "Integer32"
_Swh8021XPortConfigReauthenticate_Object = MibTableColumn
swh8021XPortConfigReauthenticate = _Swh8021XPortConfigReauthenticate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 5),
    _Swh8021XPortConfigReauthenticate_Type()
)
swh8021XPortConfigReauthenticate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XPortConfigReauthenticate.setStatus("mandatory")


class _Swh8021XPortConfigRadiusAssignedVLAN_Type(Integer32):
    """Custom type swh8021XPortConfigRadiusAssignedVLAN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Swh8021XPortConfigRadiusAssignedVLAN_Type.__name__ = "Integer32"
_Swh8021XPortConfigRadiusAssignedVLAN_Object = MibTableColumn
swh8021XPortConfigRadiusAssignedVLAN = _Swh8021XPortConfigRadiusAssignedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 7),
    _Swh8021XPortConfigRadiusAssignedVLAN_Type()
)
swh8021XPortConfigRadiusAssignedVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XPortConfigRadiusAssignedVLAN.setStatus("mandatory")


class _Swh8021XPortConfigMAB_Type(Integer32):
    """Custom type swh8021XPortConfigMAB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Swh8021XPortConfigMAB_Type.__name__ = "Integer32"
_Swh8021XPortConfigMAB_Object = MibTableColumn
swh8021XPortConfigMAB = _Swh8021XPortConfigMAB_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 9),
    _Swh8021XPortConfigMAB_Type()
)
swh8021XPortConfigMAB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XPortConfigMAB.setStatus("mandatory")


class _Swh8021XPortConfigreAuthEnable_Type(Integer32):
    """Custom type swh8021XPortConfigreAuthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Swh8021XPortConfigreAuthEnable_Type.__name__ = "Integer32"
_Swh8021XPortConfigreAuthEnable_Object = MibTableColumn
swh8021XPortConfigreAuthEnable = _Swh8021XPortConfigreAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 11),
    _Swh8021XPortConfigreAuthEnable_Type()
)
swh8021XPortConfigreAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XPortConfigreAuthEnable.setStatus("mandatory")


class _Swh8021XPortConfigreAuthSec_Type(Integer32):
    """Custom type swh8021XPortConfigreAuthSec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Swh8021XPortConfigreAuthSec_Type.__name__ = "Integer32"
_Swh8021XPortConfigreAuthSec_Object = MibTableColumn
swh8021XPortConfigreAuthSec = _Swh8021XPortConfigreAuthSec_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 13),
    _Swh8021XPortConfigreAuthSec_Type()
)
swh8021XPortConfigreAuthSec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XPortConfigreAuthSec.setStatus("mandatory")


class _Swh8021XPortConfigEAPTimeout_Type(Integer32):
    """Custom type swh8021XPortConfigEAPTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Swh8021XPortConfigEAPTimeout_Type.__name__ = "Integer32"
_Swh8021XPortConfigEAPTimeout_Object = MibTableColumn
swh8021XPortConfigEAPTimeout = _Swh8021XPortConfigEAPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 15),
    _Swh8021XPortConfigEAPTimeout_Type()
)
swh8021XPortConfigEAPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XPortConfigEAPTimeout.setStatus("mandatory")


class _Swh8021XPortConfigMaxreq_Type(Integer32):
    """Custom type swh8021XPortConfigMaxreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Swh8021XPortConfigMaxreq_Type.__name__ = "Integer32"
_Swh8021XPortConfigMaxreq_Object = MibTableColumn
swh8021XPortConfigMaxreq = _Swh8021XPortConfigMaxreq_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 55, 6, 1, 1, 17),
    _Swh8021XPortConfigMaxreq_Type()
)
swh8021XPortConfigMaxreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XPortConfigMaxreq.setStatus("mandatory")
_SwhQoSConfiguration_ObjectIdentity = ObjectIdentity
swhQoSConfiguration = _SwhQoSConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60)
)
_SwhQoSConfigPriority_ObjectIdentity = ObjectIdentity
swhQoSConfigPriority = _SwhQoSConfigPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1)
)


class _SwhQoSConfigPriorityMode_Type(Integer32):
    """Custom type swhQoSConfigPriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("ieee8021p", 2),
          ("dscp", 3))
    )


_SwhQoSConfigPriorityMode_Type.__name__ = "Integer32"
_SwhQoSConfigPriorityMode_Object = MibScalar
swhQoSConfigPriorityMode = _SwhQoSConfigPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 1),
    _SwhQoSConfigPriorityMode_Type()
)
swhQoSConfigPriorityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigPriorityMode.setStatus("mandatory")


class _SwhQoSConfigPriorityQueuingMode_Type(Integer32):
    """Custom type swhQoSConfigPriorityQueuingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("weight", 0),
          ("strict", 1))
    )


_SwhQoSConfigPriorityQueuingMode_Type.__name__ = "Integer32"
_SwhQoSConfigPriorityQueuingMode_Object = MibScalar
swhQoSConfigPriorityQueuingMode = _SwhQoSConfigPriorityQueuingMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 2),
    _SwhQoSConfigPriorityQueuingMode_Type()
)
swhQoSConfigPriorityQueuingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigPriorityQueuingMode.setStatus("mandatory")
_SwhQoSConfig8021pPriorityTable_Object = MibTable
swhQoSConfig8021pPriorityTable = _SwhQoSConfig8021pPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 5)
)
if mibBuilder.loadTexts:
    swhQoSConfig8021pPriorityTable.setStatus("mandatory")
_SwhQoSConfig8021pPriorityEntry_Object = MibTableRow
swhQoSConfig8021pPriorityEntry = _SwhQoSConfig8021pPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 5, 1)
)
swhQoSConfig8021pPriorityEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhQoSConfig8021pPriorityIndex"),
)
if mibBuilder.loadTexts:
    swhQoSConfig8021pPriorityEntry.setStatus("mandatory")


class _SwhQoSConfig8021pPriorityIndex_Type(Integer32):
    """Custom type swhQoSConfig8021pPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhQoSConfig8021pPriorityIndex_Type.__name__ = "Integer32"
_SwhQoSConfig8021pPriorityIndex_Object = MibTableColumn
swhQoSConfig8021pPriorityIndex = _SwhQoSConfig8021pPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 5, 1, 1),
    _SwhQoSConfig8021pPriorityIndex_Type()
)
swhQoSConfig8021pPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhQoSConfig8021pPriorityIndex.setStatus("mandatory")


class _SwhQoSConfig8021pPriorityPriority_Type(Integer32):
    """Custom type swhQoSConfig8021pPriorityPriority based on Integer32"""
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
        *(("dot1p-0", 0),
          ("dot1p-1", 1),
          ("dot1p-2", 2),
          ("dot1p-3", 3),
          ("dot1p-4", 4),
          ("dot1p-5", 5),
          ("dot1p-6", 6),
          ("dot1p-7", 7))
    )


_SwhQoSConfig8021pPriorityPriority_Type.__name__ = "Integer32"
_SwhQoSConfig8021pPriorityPriority_Object = MibTableColumn
swhQoSConfig8021pPriorityPriority = _SwhQoSConfig8021pPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 5, 1, 2),
    _SwhQoSConfig8021pPriorityPriority_Type()
)
swhQoSConfig8021pPriorityPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhQoSConfig8021pPriorityPriority.setStatus("mandatory")


class _SwhQoSConfig8021pPriorityQueue_Type(Integer32):
    """Custom type swhQoSConfig8021pPriorityQueue based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_SwhQoSConfig8021pPriorityQueue_Type.__name__ = "Integer32"
_SwhQoSConfig8021pPriorityQueue_Object = MibTableColumn
swhQoSConfig8021pPriorityQueue = _SwhQoSConfig8021pPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 5, 1, 3),
    _SwhQoSConfig8021pPriorityQueue_Type()
)
swhQoSConfig8021pPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfig8021pPriorityQueue.setStatus("mandatory")
_SwhQoSConfigDSCPPriorityTable_Object = MibTable
swhQoSConfigDSCPPriorityTable = _SwhQoSConfigDSCPPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 6)
)
if mibBuilder.loadTexts:
    swhQoSConfigDSCPPriorityTable.setStatus("mandatory")
_SwhQoSConfigDSCPPriorityEntry_Object = MibTableRow
swhQoSConfigDSCPPriorityEntry = _SwhQoSConfigDSCPPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 6, 1)
)
swhQoSConfigDSCPPriorityEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhQoSConfigDSCPPriorityIndex"),
)
if mibBuilder.loadTexts:
    swhQoSConfigDSCPPriorityEntry.setStatus("mandatory")


class _SwhQoSConfigDSCPPriorityIndex_Type(Integer32):
    """Custom type swhQoSConfigDSCPPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhQoSConfigDSCPPriorityIndex_Type.__name__ = "Integer32"
_SwhQoSConfigDSCPPriorityIndex_Object = MibTableColumn
swhQoSConfigDSCPPriorityIndex = _SwhQoSConfigDSCPPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 6, 1, 1),
    _SwhQoSConfigDSCPPriorityIndex_Type()
)
swhQoSConfigDSCPPriorityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhQoSConfigDSCPPriorityIndex.setStatus("mandatory")


class _SwhQoSConfigDSCPPriorityPriority_Type(Integer32):
    """Custom type swhQoSConfigDSCPPriorityPriority based on Integer32"""
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
              63)
        )
    )
    namedValues = NamedValues(
        *(("dscp-0", 0),
          ("dscp-1", 1),
          ("dscp-2", 2),
          ("dscp-3", 3),
          ("dscp-4", 4),
          ("dscp-5", 5),
          ("dscp-6", 6),
          ("dscp-7", 7),
          ("dscp-8", 8),
          ("dscp-9", 9),
          ("dscp-10", 10),
          ("dscp-11", 11),
          ("dscp-12", 12),
          ("dscp-13", 13),
          ("dscp-14", 14),
          ("dscp-15", 15),
          ("dscp-16", 16),
          ("dscp-17", 17),
          ("dscp-18", 18),
          ("dscp-19", 19),
          ("dscp-20", 20),
          ("dscp-21", 21),
          ("dscp-22", 22),
          ("dscp-23", 23),
          ("dscp-24", 24),
          ("dscp-25", 25),
          ("dscp-26", 26),
          ("dscp-27", 27),
          ("dscp-28", 28),
          ("dscp-29", 29),
          ("dscp-30", 30),
          ("dscp-31", 31),
          ("dscp-32", 32),
          ("dscp-33", 33),
          ("dscp-34", 34),
          ("dscp-35", 35),
          ("dscp-36", 36),
          ("dscp-37", 37),
          ("dscp-38", 38),
          ("dscp-39", 39),
          ("dscp-40", 40),
          ("dscp-41", 41),
          ("dscp-42", 42),
          ("dscp-43", 43),
          ("dscp-44", 44),
          ("dscp-45", 45),
          ("dscp-46", 46),
          ("dscp-47", 47),
          ("dscp-48", 48),
          ("dscp-49", 49),
          ("dscp-50", 50),
          ("dscp-51", 51),
          ("dscp-52", 52),
          ("dscp-53", 53),
          ("dscp-54", 54),
          ("dscp-55", 55),
          ("dscp-56", 56),
          ("dscp-57", 57),
          ("dscp-58", 58),
          ("dscp-59", 59),
          ("dscp-60", 60),
          ("dscp-61", 61),
          ("dscp-62", 62),
          ("dscp-63", 63))
    )


_SwhQoSConfigDSCPPriorityPriority_Type.__name__ = "Integer32"
_SwhQoSConfigDSCPPriorityPriority_Object = MibTableColumn
swhQoSConfigDSCPPriorityPriority = _SwhQoSConfigDSCPPriorityPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 6, 1, 2),
    _SwhQoSConfigDSCPPriorityPriority_Type()
)
swhQoSConfigDSCPPriorityPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhQoSConfigDSCPPriorityPriority.setStatus("mandatory")


class _SwhQoSConfigDSCPPriorityQueue_Type(Integer32):
    """Custom type swhQoSConfigDSCPPriorityQueue based on Integer32"""
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
        *(("q0", 0),
          ("q1", 1),
          ("q2", 2),
          ("q3", 3),
          ("q4", 4),
          ("q5", 5),
          ("q6", 6),
          ("q7", 7))
    )


_SwhQoSConfigDSCPPriorityQueue_Type.__name__ = "Integer32"
_SwhQoSConfigDSCPPriorityQueue_Object = MibTableColumn
swhQoSConfigDSCPPriorityQueue = _SwhQoSConfigDSCPPriorityQueue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 6, 1, 3),
    _SwhQoSConfigDSCPPriorityQueue_Type()
)
swhQoSConfigDSCPPriorityQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigDSCPPriorityQueue.setStatus("mandatory")


class _SwhQoSConfigPriorityManagementPriority_Type(Integer32):
    """Custom type swhQoSConfigPriorityManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwhQoSConfigPriorityManagementPriority_Type.__name__ = "Integer32"
_SwhQoSConfigPriorityManagementPriority_Object = MibScalar
swhQoSConfigPriorityManagementPriority = _SwhQoSConfigPriorityManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 10),
    _SwhQoSConfigPriorityManagementPriority_Type()
)
swhQoSConfigPriorityManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigPriorityManagementPriority.setStatus("mandatory")


class _SwhQoSConfigPriorityQueueWeighted_Type(DisplayString):
    """Custom type swhQoSConfigPriorityQueueWeighted based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhQoSConfigPriorityQueueWeighted_Type.__name__ = "DisplayString"
_SwhQoSConfigPriorityQueueWeighted_Object = MibScalar
swhQoSConfigPriorityQueueWeighted = _SwhQoSConfigPriorityQueueWeighted_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 11),
    _SwhQoSConfigPriorityQueueWeighted_Type()
)
swhQoSConfigPriorityQueueWeighted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigPriorityQueueWeighted.setStatus("mandatory")


class _SwhQoSConfigPriority8021pRemarking_Type(Integer32):
    """Custom type swhQoSConfigPriority8021pRemarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhQoSConfigPriority8021pRemarking_Type.__name__ = "Integer32"
_SwhQoSConfigPriority8021pRemarking_Object = MibScalar
swhQoSConfigPriority8021pRemarking = _SwhQoSConfigPriority8021pRemarking_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 30),
    _SwhQoSConfigPriority8021pRemarking_Type()
)
swhQoSConfigPriority8021pRemarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigPriority8021pRemarking.setStatus("mandatory")
_SwhQoSConfig8021pRemarkingTable_Object = MibTable
swhQoSConfig8021pRemarkingTable = _SwhQoSConfig8021pRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 31)
)
if mibBuilder.loadTexts:
    swhQoSConfig8021pRemarkingTable.setStatus("mandatory")
_SwhQoSConfig8021pRemarkingEntry_Object = MibTableRow
swhQoSConfig8021pRemarkingEntry = _SwhQoSConfig8021pRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 31, 1)
)
swhQoSConfig8021pRemarkingEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhQoSConfig8021pRemarkingIndex"),
)
if mibBuilder.loadTexts:
    swhQoSConfig8021pRemarkingEntry.setStatus("mandatory")


class _SwhQoSConfig8021pRemarkingIndex_Type(Integer32):
    """Custom type swhQoSConfig8021pRemarkingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhQoSConfig8021pRemarkingIndex_Type.__name__ = "Integer32"
_SwhQoSConfig8021pRemarkingIndex_Object = MibTableColumn
swhQoSConfig8021pRemarkingIndex = _SwhQoSConfig8021pRemarkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 31, 1, 1),
    _SwhQoSConfig8021pRemarkingIndex_Type()
)
swhQoSConfig8021pRemarkingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhQoSConfig8021pRemarkingIndex.setStatus("mandatory")


class _SwhQoSConfig8021pRemarkingNew8021p_Type(Integer32):
    """Custom type swhQoSConfig8021pRemarkingNew8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwhQoSConfig8021pRemarkingNew8021p_Type.__name__ = "Integer32"
_SwhQoSConfig8021pRemarkingNew8021p_Object = MibTableColumn
swhQoSConfig8021pRemarkingNew8021p = _SwhQoSConfig8021pRemarkingNew8021p_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 31, 1, 3),
    _SwhQoSConfig8021pRemarkingNew8021p_Type()
)
swhQoSConfig8021pRemarkingNew8021p.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfig8021pRemarkingNew8021p.setStatus("mandatory")


class _SwhQoSConfig8021pRemarkingRx8021p_Type(Integer32):
    """Custom type swhQoSConfig8021pRemarkingRx8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SwhQoSConfig8021pRemarkingRx8021p_Type.__name__ = "Integer32"
_SwhQoSConfig8021pRemarkingRx8021p_Object = MibTableColumn
swhQoSConfig8021pRemarkingRx8021p = _SwhQoSConfig8021pRemarkingRx8021p_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 31, 1, 5),
    _SwhQoSConfig8021pRemarkingRx8021p_Type()
)
swhQoSConfig8021pRemarkingRx8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhQoSConfig8021pRemarkingRx8021p.setStatus("mandatory")


class _SwhQoSConfigPriorityDSCPRemarking_Type(Integer32):
    """Custom type swhQoSConfigPriorityDSCPRemarking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhQoSConfigPriorityDSCPRemarking_Type.__name__ = "Integer32"
_SwhQoSConfigPriorityDSCPRemarking_Object = MibScalar
swhQoSConfigPriorityDSCPRemarking = _SwhQoSConfigPriorityDSCPRemarking_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 40),
    _SwhQoSConfigPriorityDSCPRemarking_Type()
)
swhQoSConfigPriorityDSCPRemarking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigPriorityDSCPRemarking.setStatus("mandatory")
_SwhQoSConfigDSCPRemarkingTable_Object = MibTable
swhQoSConfigDSCPRemarkingTable = _SwhQoSConfigDSCPRemarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 41)
)
if mibBuilder.loadTexts:
    swhQoSConfigDSCPRemarkingTable.setStatus("mandatory")
_SwhQoSConfigDSCPRemarkingEntry_Object = MibTableRow
swhQoSConfigDSCPRemarkingEntry = _SwhQoSConfigDSCPRemarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 41, 1)
)
swhQoSConfigDSCPRemarkingEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhQoSConfigDSCPRemarkingIndex"),
)
if mibBuilder.loadTexts:
    swhQoSConfigDSCPRemarkingEntry.setStatus("mandatory")


class _SwhQoSConfigDSCPRemarkingIndex_Type(Integer32):
    """Custom type swhQoSConfigDSCPRemarkingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhQoSConfigDSCPRemarkingIndex_Type.__name__ = "Integer32"
_SwhQoSConfigDSCPRemarkingIndex_Object = MibTableColumn
swhQoSConfigDSCPRemarkingIndex = _SwhQoSConfigDSCPRemarkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 41, 1, 1),
    _SwhQoSConfigDSCPRemarkingIndex_Type()
)
swhQoSConfigDSCPRemarkingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhQoSConfigDSCPRemarkingIndex.setStatus("mandatory")


class _SwhQoSConfigDSCPRemarkingNewDSCP_Type(Integer32):
    """Custom type swhQoSConfigDSCPRemarkingNewDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwhQoSConfigDSCPRemarkingNewDSCP_Type.__name__ = "Integer32"
_SwhQoSConfigDSCPRemarkingNewDSCP_Object = MibTableColumn
swhQoSConfigDSCPRemarkingNewDSCP = _SwhQoSConfigDSCPRemarkingNewDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 41, 1, 3),
    _SwhQoSConfigDSCPRemarkingNewDSCP_Type()
)
swhQoSConfigDSCPRemarkingNewDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigDSCPRemarkingNewDSCP.setStatus("mandatory")


class _SwhQoSConfigDSCPRemarkingRxDSCP_Type(Integer32):
    """Custom type swhQoSConfigDSCPRemarkingRxDSCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_SwhQoSConfigDSCPRemarkingRxDSCP_Type.__name__ = "Integer32"
_SwhQoSConfigDSCPRemarkingRxDSCP_Object = MibTableColumn
swhQoSConfigDSCPRemarkingRxDSCP = _SwhQoSConfigDSCPRemarkingRxDSCP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 1, 41, 1, 5),
    _SwhQoSConfigDSCPRemarkingRxDSCP_Type()
)
swhQoSConfigDSCPRemarkingRxDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigDSCPRemarkingRxDSCP.setStatus("mandatory")
_SwhQoSConfigPortConfig_ObjectIdentity = ObjectIdentity
swhQoSConfigPortConfig = _SwhQoSConfigPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 3)
)
_SwhQoSConfigPortConfigTable_Object = MibTable
swhQoSConfigPortConfigTable = _SwhQoSConfigPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 3, 1)
)
if mibBuilder.loadTexts:
    swhQoSConfigPortConfigTable.setStatus("mandatory")
_SwhQoSConfigPortConfigEntry_Object = MibTableRow
swhQoSConfigPortConfigEntry = _SwhQoSConfigPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 3, 1, 1)
)
swhQoSConfigPortConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhQoSConfigPortConfigIndex"),
)
if mibBuilder.loadTexts:
    swhQoSConfigPortConfigEntry.setStatus("mandatory")


class _SwhQoSConfigPortConfigIndex_Type(Integer32):
    """Custom type swhQoSConfigPortConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhQoSConfigPortConfigIndex_Type.__name__ = "Integer32"
_SwhQoSConfigPortConfigIndex_Object = MibTableColumn
swhQoSConfigPortConfigIndex = _SwhQoSConfigPortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 3, 1, 1, 1),
    _SwhQoSConfigPortConfigIndex_Type()
)
swhQoSConfigPortConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhQoSConfigPortConfigIndex.setStatus("mandatory")
_SwhQoSConfigPortConfigUserPriority_Type = Integer32
_SwhQoSConfigPortConfigUserPriority_Object = MibTableColumn
swhQoSConfigPortConfigUserPriority = _SwhQoSConfigPortConfigUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 3, 1, 1, 7),
    _SwhQoSConfigPortConfigUserPriority_Type()
)
swhQoSConfigPortConfigUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigPortConfigUserPriority.setStatus("mandatory")
_SwhQoSConfigRateLimiters_ObjectIdentity = ObjectIdentity
swhQoSConfigRateLimiters = _SwhQoSConfigRateLimiters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 9)
)
_SwhQoSConfigRateLimitersTable_Object = MibTable
swhQoSConfigRateLimitersTable = _SwhQoSConfigRateLimitersTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 9, 1)
)
if mibBuilder.loadTexts:
    swhQoSConfigRateLimitersTable.setStatus("mandatory")
_SwhQoSConfigRateLimitersEntry_Object = MibTableRow
swhQoSConfigRateLimitersEntry = _SwhQoSConfigRateLimitersEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 9, 1, 1)
)
swhQoSConfigRateLimitersEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhQoSConfigRateLimitersIndex"),
)
if mibBuilder.loadTexts:
    swhQoSConfigRateLimitersEntry.setStatus("mandatory")


class _SwhQoSConfigRateLimitersIndex_Type(Integer32):
    """Custom type swhQoSConfigRateLimitersIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhQoSConfigRateLimitersIndex_Type.__name__ = "Integer32"
_SwhQoSConfigRateLimitersIndex_Object = MibTableColumn
swhQoSConfigRateLimitersIndex = _SwhQoSConfigRateLimitersIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 9, 1, 1, 1),
    _SwhQoSConfigRateLimitersIndex_Type()
)
swhQoSConfigRateLimitersIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhQoSConfigRateLimitersIndex.setStatus("mandatory")


class _SwhQoSConfigRateLimitersIngressRate_Type(Integer32):
    """Custom type swhQoSConfigRateLimitersIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1000000),
    )


_SwhQoSConfigRateLimitersIngressRate_Type.__name__ = "Integer32"
_SwhQoSConfigRateLimitersIngressRate_Object = MibTableColumn
swhQoSConfigRateLimitersIngressRate = _SwhQoSConfigRateLimitersIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 9, 1, 1, 3),
    _SwhQoSConfigRateLimitersIngressRate_Type()
)
swhQoSConfigRateLimitersIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigRateLimitersIngressRate.setStatus("mandatory")


class _SwhQoSConfigRateLimitersEgressRate_Type(Integer32):
    """Custom type swhQoSConfigRateLimitersEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1000000),
    )


_SwhQoSConfigRateLimitersEgressRate_Type.__name__ = "Integer32"
_SwhQoSConfigRateLimitersEgressRate_Object = MibTableColumn
swhQoSConfigRateLimitersEgressRate = _SwhQoSConfigRateLimitersEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 60, 9, 1, 1, 5),
    _SwhQoSConfigRateLimitersEgressRate_Type()
)
swhQoSConfigRateLimitersEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhQoSConfigRateLimitersEgressRate.setStatus("mandatory")
_SwhDSCPRemark_ObjectIdentity = ObjectIdentity
swhDSCPRemark = _SwhDSCPRemark_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 61)
)
_SwhACLConfiguration_ObjectIdentity = ObjectIdentity
swhACLConfiguration = _SwhACLConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65)
)
_SwhAccessControlList_ObjectIdentity = ObjectIdentity
swhAccessControlList = _SwhAccessControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3)
)
_SwhAccessControlListTable_Object = MibTable
swhAccessControlListTable = _SwhAccessControlListTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1)
)
if mibBuilder.loadTexts:
    swhAccessControlListTable.setStatus("mandatory")
_SwhAccessControlListEntry_Object = MibTableRow
swhAccessControlListEntry = _SwhAccessControlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1)
)
swhAccessControlListEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhAccessControlListIndex"),
)
if mibBuilder.loadTexts:
    swhAccessControlListEntry.setStatus("mandatory")


class _SwhAccessControlListIndex_Type(Integer32):
    """Custom type swhAccessControlListIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhAccessControlListIndex_Type.__name__ = "Integer32"
_SwhAccessControlListIndex_Object = MibTableColumn
swhAccessControlListIndex = _SwhAccessControlListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 1),
    _SwhAccessControlListIndex_Type()
)
swhAccessControlListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhAccessControlListIndex.setStatus("mandatory")


class _SwhAccessControlListValid_Type(Integer32):
    """Custom type swhAccessControlListValid based on Integer32"""
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


_SwhAccessControlListValid_Type.__name__ = "Integer32"
_SwhAccessControlListValid_Object = MibTableColumn
swhAccessControlListValid = _SwhAccessControlListValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 2),
    _SwhAccessControlListValid_Type()
)
swhAccessControlListValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhAccessControlListValid.setStatus("mandatory")


class _SwhAccessControlListRuleID_Type(Integer32):
    """Custom type swhAccessControlListRuleID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 110),
    )


_SwhAccessControlListRuleID_Type.__name__ = "Integer32"
_SwhAccessControlListRuleID_Object = MibTableColumn
swhAccessControlListRuleID = _SwhAccessControlListRuleID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 3),
    _SwhAccessControlListRuleID_Type()
)
swhAccessControlListRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhAccessControlListRuleID.setStatus("mandatory")
_SwhAccessControlListIngressPort_Type = DisplayString
_SwhAccessControlListIngressPort_Object = MibTableColumn
swhAccessControlListIngressPort = _SwhAccessControlListIngressPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 4),
    _SwhAccessControlListIngressPort_Type()
)
swhAccessControlListIngressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIngressPort.setStatus("mandatory")


class _SwhAccessControlListAction_Type(Integer32):
    """Custom type swhAccessControlListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 0),
          ("permit", 1),
          ("mirror", 2),
          ("redirct", 3))
    )


_SwhAccessControlListAction_Type.__name__ = "Integer32"
_SwhAccessControlListAction_Object = MibTableColumn
swhAccessControlListAction = _SwhAccessControlListAction_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 6),
    _SwhAccessControlListAction_Type()
)
swhAccessControlListAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListAction.setStatus("mandatory")
_SwhAccessControlListRateLimiter_Type = Integer32
_SwhAccessControlListRateLimiter_Object = MibTableColumn
swhAccessControlListRateLimiter = _SwhAccessControlListRateLimiter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 7),
    _SwhAccessControlListRateLimiter_Type()
)
swhAccessControlListRateLimiter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListRateLimiter.setStatus("mandatory")
_SwhAccessControlListPortCopy_Type = Integer32
_SwhAccessControlListPortCopy_Object = MibTableColumn
swhAccessControlListPortCopy = _SwhAccessControlListPortCopy_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 8),
    _SwhAccessControlListPortCopy_Type()
)
swhAccessControlListPortCopy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListPortCopy.setStatus("mandatory")


class _SwhAccessControlListDelete_Type(Integer32):
    """Custom type swhAccessControlListDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhAccessControlListDelete_Type.__name__ = "Integer32"
_SwhAccessControlListDelete_Object = MibTableColumn
swhAccessControlListDelete = _SwhAccessControlListDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 10),
    _SwhAccessControlListDelete_Type()
)
swhAccessControlListDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListDelete.setStatus("mandatory")


class _SwhAccessControlListSourceMACFilter_Type(Integer32):
    """Custom type swhAccessControlListSourceMACFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListSourceMACFilter_Type.__name__ = "Integer32"
_SwhAccessControlListSourceMACFilter_Object = MibTableColumn
swhAccessControlListSourceMACFilter = _SwhAccessControlListSourceMACFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 11),
    _SwhAccessControlListSourceMACFilter_Type()
)
swhAccessControlListSourceMACFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListSourceMACFilter.setStatus("mandatory")
_SwhAccessControlListSourceMACValue_Type = DisplayString
_SwhAccessControlListSourceMACValue_Object = MibTableColumn
swhAccessControlListSourceMACValue = _SwhAccessControlListSourceMACValue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 12),
    _SwhAccessControlListSourceMACValue_Type()
)
swhAccessControlListSourceMACValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListSourceMACValue.setStatus("mandatory")


class _SwhAccessControlListDestinationMACFilter_Type(Integer32):
    """Custom type swhAccessControlListDestinationMACFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListDestinationMACFilter_Type.__name__ = "Integer32"
_SwhAccessControlListDestinationMACFilter_Object = MibTableColumn
swhAccessControlListDestinationMACFilter = _SwhAccessControlListDestinationMACFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 13),
    _SwhAccessControlListDestinationMACFilter_Type()
)
swhAccessControlListDestinationMACFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListDestinationMACFilter.setStatus("mandatory")
_SwhAccessControlListDestinationMACValue_Type = DisplayString
_SwhAccessControlListDestinationMACValue_Object = MibTableColumn
swhAccessControlListDestinationMACValue = _SwhAccessControlListDestinationMACValue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 14),
    _SwhAccessControlListDestinationMACValue_Type()
)
swhAccessControlListDestinationMACValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListDestinationMACValue.setStatus("mandatory")


class _SwhAccessControlListVLANIDFilter_Type(Integer32):
    """Custom type swhAccessControlListVLANIDFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListVLANIDFilter_Type.__name__ = "Integer32"
_SwhAccessControlListVLANIDFilter_Object = MibTableColumn
swhAccessControlListVLANIDFilter = _SwhAccessControlListVLANIDFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 15),
    _SwhAccessControlListVLANIDFilter_Type()
)
swhAccessControlListVLANIDFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListVLANIDFilter.setStatus("mandatory")


class _SwhAccessControlListVLANID_Type(Integer32):
    """Custom type swhAccessControlListVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwhAccessControlListVLANID_Type.__name__ = "Integer32"
_SwhAccessControlListVLANID_Object = MibTableColumn
swhAccessControlListVLANID = _SwhAccessControlListVLANID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 16),
    _SwhAccessControlListVLANID_Type()
)
swhAccessControlListVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListVLANID.setStatus("mandatory")


class _SwhAccessControlListEtherTypeFilter_Type(Integer32):
    """Custom type swhAccessControlListEtherTypeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListEtherTypeFilter_Type.__name__ = "Integer32"
_SwhAccessControlListEtherTypeFilter_Object = MibTableColumn
swhAccessControlListEtherTypeFilter = _SwhAccessControlListEtherTypeFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 18),
    _SwhAccessControlListEtherTypeFilter_Type()
)
swhAccessControlListEtherTypeFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListEtherTypeFilter.setStatus("mandatory")
_SwhAccessControlListEthernetTypeValue_Type = DisplayString
_SwhAccessControlListEthernetTypeValue_Object = MibTableColumn
swhAccessControlListEthernetTypeValue = _SwhAccessControlListEthernetTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 19),
    _SwhAccessControlListEthernetTypeValue_Type()
)
swhAccessControlListEthernetTypeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListEthernetTypeValue.setStatus("mandatory")


class _SwhAccessControlListIngressPortFilter_Type(Integer32):
    """Custom type swhAccessControlListIngressPortFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListIngressPortFilter_Type.__name__ = "Integer32"
_SwhAccessControlListIngressPortFilter_Object = MibTableColumn
swhAccessControlListIngressPortFilter = _SwhAccessControlListIngressPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 63),
    _SwhAccessControlListIngressPortFilter_Type()
)
swhAccessControlListIngressPortFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIngressPortFilter.setStatus("mandatory")
_SwhAccessControlListSourceMACMask_Type = DisplayString
_SwhAccessControlListSourceMACMask_Object = MibTableColumn
swhAccessControlListSourceMACMask = _SwhAccessControlListSourceMACMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 64),
    _SwhAccessControlListSourceMACMask_Type()
)
swhAccessControlListSourceMACMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListSourceMACMask.setStatus("mandatory")
_SwhAccessControlListDestinationMACMask_Type = DisplayString
_SwhAccessControlListDestinationMACMask_Object = MibTableColumn
swhAccessControlListDestinationMACMask = _SwhAccessControlListDestinationMACMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 65),
    _SwhAccessControlListDestinationMACMask_Type()
)
swhAccessControlListDestinationMACMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListDestinationMACMask.setStatus("mandatory")


class _SwhAccessControlListTOSTrafficClassFilter_Type(Integer32):
    """Custom type swhAccessControlListTOSTrafficClassFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListTOSTrafficClassFilter_Type.__name__ = "Integer32"
_SwhAccessControlListTOSTrafficClassFilter_Object = MibTableColumn
swhAccessControlListTOSTrafficClassFilter = _SwhAccessControlListTOSTrafficClassFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 66),
    _SwhAccessControlListTOSTrafficClassFilter_Type()
)
swhAccessControlListTOSTrafficClassFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListTOSTrafficClassFilter.setStatus("mandatory")
_SwhAccessControlListTOSTrafficClass_Type = DisplayString
_SwhAccessControlListTOSTrafficClass_Object = MibTableColumn
swhAccessControlListTOSTrafficClass = _SwhAccessControlListTOSTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 67),
    _SwhAccessControlListTOSTrafficClass_Type()
)
swhAccessControlListTOSTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListTOSTrafficClass.setStatus("mandatory")


class _SwhAccessControlListProtocolNextHeaderFilter_Type(Integer32):
    """Custom type swhAccessControlListProtocolNextHeaderFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListProtocolNextHeaderFilter_Type.__name__ = "Integer32"
_SwhAccessControlListProtocolNextHeaderFilter_Object = MibTableColumn
swhAccessControlListProtocolNextHeaderFilter = _SwhAccessControlListProtocolNextHeaderFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 68),
    _SwhAccessControlListProtocolNextHeaderFilter_Type()
)
swhAccessControlListProtocolNextHeaderFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListProtocolNextHeaderFilter.setStatus("mandatory")
_SwhAccessControlListProtocolNextHeader_Type = DisplayString
_SwhAccessControlListProtocolNextHeader_Object = MibTableColumn
swhAccessControlListProtocolNextHeader = _SwhAccessControlListProtocolNextHeader_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 69),
    _SwhAccessControlListProtocolNextHeader_Type()
)
swhAccessControlListProtocolNextHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListProtocolNextHeader.setStatus("mandatory")


class _SwhAccessControlListIPv4SourceIPFilter_Type(Integer32):
    """Custom type swhAccessControlListIPv4SourceIPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("network", 1))
    )


_SwhAccessControlListIPv4SourceIPFilter_Type.__name__ = "Integer32"
_SwhAccessControlListIPv4SourceIPFilter_Object = MibTableColumn
swhAccessControlListIPv4SourceIPFilter = _SwhAccessControlListIPv4SourceIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 70),
    _SwhAccessControlListIPv4SourceIPFilter_Type()
)
swhAccessControlListIPv4SourceIPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv4SourceIPFilter.setStatus("mandatory")
_SwhAccessControlListIPv4SourceIPAddress_Type = DisplayString
_SwhAccessControlListIPv4SourceIPAddress_Object = MibTableColumn
swhAccessControlListIPv4SourceIPAddress = _SwhAccessControlListIPv4SourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 71),
    _SwhAccessControlListIPv4SourceIPAddress_Type()
)
swhAccessControlListIPv4SourceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv4SourceIPAddress.setStatus("mandatory")
_SwhAccessControlListIPv4SourceIPMask_Type = DisplayString
_SwhAccessControlListIPv4SourceIPMask_Object = MibTableColumn
swhAccessControlListIPv4SourceIPMask = _SwhAccessControlListIPv4SourceIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 72),
    _SwhAccessControlListIPv4SourceIPMask_Type()
)
swhAccessControlListIPv4SourceIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv4SourceIPMask.setStatus("mandatory")


class _SwhAccessControlListIPv4DestinationIPFilter_Type(Integer32):
    """Custom type swhAccessControlListIPv4DestinationIPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("network", 1))
    )


_SwhAccessControlListIPv4DestinationIPFilter_Type.__name__ = "Integer32"
_SwhAccessControlListIPv4DestinationIPFilter_Object = MibTableColumn
swhAccessControlListIPv4DestinationIPFilter = _SwhAccessControlListIPv4DestinationIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 73),
    _SwhAccessControlListIPv4DestinationIPFilter_Type()
)
swhAccessControlListIPv4DestinationIPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv4DestinationIPFilter.setStatus("mandatory")
_SwhAccessControlListIPv4DestinationIPAddress_Type = DisplayString
_SwhAccessControlListIPv4DestinationIPAddress_Object = MibTableColumn
swhAccessControlListIPv4DestinationIPAddress = _SwhAccessControlListIPv4DestinationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 74),
    _SwhAccessControlListIPv4DestinationIPAddress_Type()
)
swhAccessControlListIPv4DestinationIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv4DestinationIPAddress.setStatus("mandatory")
_SwhAccessControlListIPv4DestinationIPMask_Type = DisplayString
_SwhAccessControlListIPv4DestinationIPMask_Object = MibTableColumn
swhAccessControlListIPv4DestinationIPMask = _SwhAccessControlListIPv4DestinationIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 75),
    _SwhAccessControlListIPv4DestinationIPMask_Type()
)
swhAccessControlListIPv4DestinationIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv4DestinationIPMask.setStatus("mandatory")


class _SwhAccessControlListIPv6SourceIPFilter_Type(Integer32):
    """Custom type swhAccessControlListIPv6SourceIPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("network", 1))
    )


_SwhAccessControlListIPv6SourceIPFilter_Type.__name__ = "Integer32"
_SwhAccessControlListIPv6SourceIPFilter_Object = MibTableColumn
swhAccessControlListIPv6SourceIPFilter = _SwhAccessControlListIPv6SourceIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 76),
    _SwhAccessControlListIPv6SourceIPFilter_Type()
)
swhAccessControlListIPv6SourceIPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv6SourceIPFilter.setStatus("mandatory")
_SwhAccessControlListIPv6SourceIPAddress_Type = DisplayString
_SwhAccessControlListIPv6SourceIPAddress_Object = MibTableColumn
swhAccessControlListIPv6SourceIPAddress = _SwhAccessControlListIPv6SourceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 77),
    _SwhAccessControlListIPv6SourceIPAddress_Type()
)
swhAccessControlListIPv6SourceIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv6SourceIPAddress.setStatus("mandatory")
_SwhAccessControlListIPv6SourceIPMask_Type = Integer32
_SwhAccessControlListIPv6SourceIPMask_Object = MibTableColumn
swhAccessControlListIPv6SourceIPMask = _SwhAccessControlListIPv6SourceIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 78),
    _SwhAccessControlListIPv6SourceIPMask_Type()
)
swhAccessControlListIPv6SourceIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv6SourceIPMask.setStatus("mandatory")


class _SwhAccessControlListIPv6DestinationIPFilter_Type(Integer32):
    """Custom type swhAccessControlListIPv6DestinationIPFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("network", 1))
    )


_SwhAccessControlListIPv6DestinationIPFilter_Type.__name__ = "Integer32"
_SwhAccessControlListIPv6DestinationIPFilter_Object = MibTableColumn
swhAccessControlListIPv6DestinationIPFilter = _SwhAccessControlListIPv6DestinationIPFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 79),
    _SwhAccessControlListIPv6DestinationIPFilter_Type()
)
swhAccessControlListIPv6DestinationIPFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv6DestinationIPFilter.setStatus("mandatory")
_SwhAccessControlListIPv6DestinationIPAddress_Type = DisplayString
_SwhAccessControlListIPv6DestinationIPAddress_Object = MibTableColumn
swhAccessControlListIPv6DestinationIPAddress = _SwhAccessControlListIPv6DestinationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 80),
    _SwhAccessControlListIPv6DestinationIPAddress_Type()
)
swhAccessControlListIPv6DestinationIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv6DestinationIPAddress.setStatus("mandatory")
_SwhAccessControlListIPv6DestinationIPMask_Type = Integer32
_SwhAccessControlListIPv6DestinationIPMask_Object = MibTableColumn
swhAccessControlListIPv6DestinationIPMask = _SwhAccessControlListIPv6DestinationIPMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 81),
    _SwhAccessControlListIPv6DestinationIPMask_Type()
)
swhAccessControlListIPv6DestinationIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListIPv6DestinationIPMask.setStatus("mandatory")


class _SwhAccessControlListTCPUDPSourcePortFilter_Type(Integer32):
    """Custom type swhAccessControlListTCPUDPSourcePortFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListTCPUDPSourcePortFilter_Type.__name__ = "Integer32"
_SwhAccessControlListTCPUDPSourcePortFilter_Object = MibTableColumn
swhAccessControlListTCPUDPSourcePortFilter = _SwhAccessControlListTCPUDPSourcePortFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 82),
    _SwhAccessControlListTCPUDPSourcePortFilter_Type()
)
swhAccessControlListTCPUDPSourcePortFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListTCPUDPSourcePortFilter.setStatus("mandatory")
_SwhAccessControlListTCPUDPSourcePort_Type = Integer32
_SwhAccessControlListTCPUDPSourcePort_Object = MibTableColumn
swhAccessControlListTCPUDPSourcePort = _SwhAccessControlListTCPUDPSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 83),
    _SwhAccessControlListTCPUDPSourcePort_Type()
)
swhAccessControlListTCPUDPSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListTCPUDPSourcePort.setStatus("mandatory")
_SwhAccessControlListTCPUDPSourcePortMask_Type = DisplayString
_SwhAccessControlListTCPUDPSourcePortMask_Object = MibTableColumn
swhAccessControlListTCPUDPSourcePortMask = _SwhAccessControlListTCPUDPSourcePortMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 84),
    _SwhAccessControlListTCPUDPSourcePortMask_Type()
)
swhAccessControlListTCPUDPSourcePortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListTCPUDPSourcePortMask.setStatus("mandatory")


class _SwhAccessControlListTCPUDPDestinationPortFilter_Type(Integer32):
    """Custom type swhAccessControlListTCPUDPDestinationPortFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("specific", 1))
    )


_SwhAccessControlListTCPUDPDestinationPortFilter_Type.__name__ = "Integer32"
_SwhAccessControlListTCPUDPDestinationPortFilter_Object = MibTableColumn
swhAccessControlListTCPUDPDestinationPortFilter = _SwhAccessControlListTCPUDPDestinationPortFilter_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 85),
    _SwhAccessControlListTCPUDPDestinationPortFilter_Type()
)
swhAccessControlListTCPUDPDestinationPortFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListTCPUDPDestinationPortFilter.setStatus("mandatory")
_SwhAccessControlListTCPUDPDestinationPort_Type = Integer32
_SwhAccessControlListTCPUDPDestinationPort_Object = MibTableColumn
swhAccessControlListTCPUDPDestinationPort = _SwhAccessControlListTCPUDPDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 86),
    _SwhAccessControlListTCPUDPDestinationPort_Type()
)
swhAccessControlListTCPUDPDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListTCPUDPDestinationPort.setStatus("mandatory")
_SwhAccessControlListTCPUDPDestinationPortMask_Type = DisplayString
_SwhAccessControlListTCPUDPDestinationPortMask_Object = MibTableColumn
swhAccessControlListTCPUDPDestinationPortMask = _SwhAccessControlListTCPUDPDestinationPortMask_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 87),
    _SwhAccessControlListTCPUDPDestinationPortMask_Type()
)
swhAccessControlListTCPUDPDestinationPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListTCPUDPDestinationPortMask.setStatus("mandatory")


class _SwhAccessControlListApply_Type(Integer32):
    """Custom type swhAccessControlListApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("apply", 1))
    )


_SwhAccessControlListApply_Type.__name__ = "Integer32"
_SwhAccessControlListApply_Object = MibTableColumn
swhAccessControlListApply = _SwhAccessControlListApply_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 65, 3, 1, 1, 200),
    _SwhAccessControlListApply_Type()
)
swhAccessControlListApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhAccessControlListApply.setStatus("mandatory")
_SwhStaticMulticastConfiguration_ObjectIdentity = ObjectIdentity
swhStaticMulticastConfiguration = _SwhStaticMulticastConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70)
)
_SwhMulticastTable_Object = MibTable
swhMulticastTable = _SwhMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1)
)
if mibBuilder.loadTexts:
    swhMulticastTable.setStatus("mandatory")
_SwhMulticastEntry_Object = MibTableRow
swhMulticastEntry = _SwhMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1, 1)
)
swhMulticastEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhMulticastIndex"),
)
if mibBuilder.loadTexts:
    swhMulticastEntry.setStatus("mandatory")


class _SwhMulticastIndex_Type(Integer32):
    """Custom type swhMulticastIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMulticastIndex_Type.__name__ = "Integer32"
_SwhMulticastIndex_Object = MibTableColumn
swhMulticastIndex = _SwhMulticastIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1, 1, 1),
    _SwhMulticastIndex_Type()
)
swhMulticastIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhMulticastIndex.setStatus("mandatory")


class _SwhMulticastValid_Type(Integer32):
    """Custom type swhMulticastValid based on Integer32"""
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


_SwhMulticastValid_Type.__name__ = "Integer32"
_SwhMulticastValid_Object = MibTableColumn
swhMulticastValid = _SwhMulticastValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1, 1, 2),
    _SwhMulticastValid_Type()
)
swhMulticastValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMulticastValid.setStatus("mandatory")
_SwhMulticastIPAddress_Type = IpAddress
_SwhMulticastIPAddress_Object = MibTableColumn
swhMulticastIPAddress = _SwhMulticastIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1, 1, 3),
    _SwhMulticastIPAddress_Type()
)
swhMulticastIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMulticastIPAddress.setStatus("mandatory")


class _SwhMulticastVLANID_Type(Integer32):
    """Custom type swhMulticastVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwhMulticastVLANID_Type.__name__ = "Integer32"
_SwhMulticastVLANID_Object = MibTableColumn
swhMulticastVLANID = _SwhMulticastVLANID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1, 1, 6),
    _SwhMulticastVLANID_Type()
)
swhMulticastVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMulticastVLANID.setStatus("mandatory")


class _SwhMulticastForwardingPort_Type(Integer32):
    """Custom type swhMulticastForwardingPort based on Integer32"""
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
        *(("port01", 0),
          ("port02", 1),
          ("port03", 2),
          ("port04", 3),
          ("port05", 4),
          ("port06", 5))
    )


_SwhMulticastForwardingPort_Type.__name__ = "Integer32"
_SwhMulticastForwardingPort_Object = MibTableColumn
swhMulticastForwardingPort = _SwhMulticastForwardingPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1, 1, 7),
    _SwhMulticastForwardingPort_Type()
)
swhMulticastForwardingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMulticastForwardingPort.setStatus("mandatory")


class _SwhMulticastDelete_Type(Integer32):
    """Custom type swhMulticastDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhMulticastDelete_Type.__name__ = "Integer32"
_SwhMulticastDelete_Object = MibTableColumn
swhMulticastDelete = _SwhMulticastDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1, 1, 10),
    _SwhMulticastDelete_Type()
)
swhMulticastDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMulticastDelete.setStatus("mandatory")
_SwhMulticastIPv6Address_Type = DisplayString
_SwhMulticastIPv6Address_Object = MibTableColumn
swhMulticastIPv6Address = _SwhMulticastIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 70, 1, 1, 11),
    _SwhMulticastIPv6Address_Type()
)
swhMulticastIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMulticastIPv6Address.setStatus("mandatory")
_SwhSecurityConfiguration_ObjectIdentity = ObjectIdentity
swhSecurityConfiguration = _SwhSecurityConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80)
)
_SwhDHCPOpt82Settings_ObjectIdentity = ObjectIdentity
swhDHCPOpt82Settings = _SwhDHCPOpt82Settings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 1)
)


class _SwhSecurityConfigDHCPOpt82RelayAgent_Type(Integer32):
    """Custom type swhSecurityConfigDHCPOpt82RelayAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhSecurityConfigDHCPOpt82RelayAgent_Type.__name__ = "Integer32"
_SwhSecurityConfigDHCPOpt82RelayAgent_Object = MibScalar
swhSecurityConfigDHCPOpt82RelayAgent = _SwhSecurityConfigDHCPOpt82RelayAgent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 1, 1),
    _SwhSecurityConfigDHCPOpt82RelayAgent_Type()
)
swhSecurityConfigDHCPOpt82RelayAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityConfigDHCPOpt82RelayAgent.setStatus("mandatory")
_SwhSecurityConfigRemoteID_Type = DisplayString
_SwhSecurityConfigRemoteID_Object = MibScalar
swhSecurityConfigRemoteID = _SwhSecurityConfigRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 1, 2),
    _SwhSecurityConfigRemoteID_Type()
)
swhSecurityConfigRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSecurityConfigRemoteID.setStatus("mandatory")
_SwhSecurityConfigDHCPOpt82PortTable_Object = MibTable
swhSecurityConfigDHCPOpt82PortTable = _SwhSecurityConfigDHCPOpt82PortTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 1, 3)
)
if mibBuilder.loadTexts:
    swhSecurityConfigDHCPOpt82PortTable.setStatus("mandatory")
_SwhSecurityConfigDHCPOpt82PortTableEntry_Object = MibTableRow
swhSecurityConfigDHCPOpt82PortTableEntry = _SwhSecurityConfigDHCPOpt82PortTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 1, 3, 1)
)
swhSecurityConfigDHCPOpt82PortTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDHCPOpt82PortIndex"),
)
if mibBuilder.loadTexts:
    swhSecurityConfigDHCPOpt82PortTableEntry.setStatus("mandatory")


class _SwhDHCPOpt82PortIndex_Type(Integer32):
    """Custom type swhDHCPOpt82PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDHCPOpt82PortIndex_Type.__name__ = "Integer32"
_SwhDHCPOpt82PortIndex_Object = MibTableColumn
swhDHCPOpt82PortIndex = _SwhDHCPOpt82PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 1, 3, 1, 1),
    _SwhDHCPOpt82PortIndex_Type()
)
swhDHCPOpt82PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDHCPOpt82PortIndex.setStatus("mandatory")


class _SwhDHCPOpt82PortOpt82Port_Type(Integer32):
    """Custom type swhDHCPOpt82PortOpt82Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhDHCPOpt82PortOpt82Port_Type.__name__ = "Integer32"
_SwhDHCPOpt82PortOpt82Port_Object = MibTableColumn
swhDHCPOpt82PortOpt82Port = _SwhDHCPOpt82PortOpt82Port_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 1, 3, 1, 2),
    _SwhDHCPOpt82PortOpt82Port_Type()
)
swhDHCPOpt82PortOpt82Port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82PortOpt82Port.setStatus("mandatory")


class _SwhDHCPOpt82PortTrustPort_Type(Integer32):
    """Custom type swhDHCPOpt82PortTrustPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhDHCPOpt82PortTrustPort_Type.__name__ = "Integer32"
_SwhDHCPOpt82PortTrustPort_Object = MibTableColumn
swhDHCPOpt82PortTrustPort = _SwhDHCPOpt82PortTrustPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 1, 3, 1, 3),
    _SwhDHCPOpt82PortTrustPort_Type()
)
swhDHCPOpt82PortTrustPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82PortTrustPort.setStatus("mandatory")
_SwhIPSourceGuardSettings_ObjectIdentity = ObjectIdentity
swhIPSourceGuardSettings = _SwhIPSourceGuardSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 2)
)


class _SwhIPSourceGuardSettingsPort1_Type(Integer32):
    """Custom type swhIPSourceGuardSettingsPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-ip", 0),
          ("dhcp", 1),
          ("unlimited", 2))
    )


_SwhIPSourceGuardSettingsPort1_Type.__name__ = "Integer32"
_SwhIPSourceGuardSettingsPort1_Object = MibScalar
swhIPSourceGuardSettingsPort1 = _SwhIPSourceGuardSettingsPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 2, 1),
    _SwhIPSourceGuardSettingsPort1_Type()
)
swhIPSourceGuardSettingsPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPSourceGuardSettingsPort1.setStatus("mandatory")


class _SwhIPSourceGuardSettingsPort2_Type(Integer32):
    """Custom type swhIPSourceGuardSettingsPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-ip", 0),
          ("dhcp", 1),
          ("unlimited", 2))
    )


_SwhIPSourceGuardSettingsPort2_Type.__name__ = "Integer32"
_SwhIPSourceGuardSettingsPort2_Object = MibScalar
swhIPSourceGuardSettingsPort2 = _SwhIPSourceGuardSettingsPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 2, 2),
    _SwhIPSourceGuardSettingsPort2_Type()
)
swhIPSourceGuardSettingsPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPSourceGuardSettingsPort2.setStatus("mandatory")


class _SwhIPSourceGuardSettingsPort3_Type(Integer32):
    """Custom type swhIPSourceGuardSettingsPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-ip", 0),
          ("dhcp", 1),
          ("unlimited", 2))
    )


_SwhIPSourceGuardSettingsPort3_Type.__name__ = "Integer32"
_SwhIPSourceGuardSettingsPort3_Object = MibScalar
swhIPSourceGuardSettingsPort3 = _SwhIPSourceGuardSettingsPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 2, 3),
    _SwhIPSourceGuardSettingsPort3_Type()
)
swhIPSourceGuardSettingsPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPSourceGuardSettingsPort3.setStatus("mandatory")


class _SwhIPSourceGuardSettingsPort4_Type(Integer32):
    """Custom type swhIPSourceGuardSettingsPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-ip", 0),
          ("dhcp", 1),
          ("unlimited", 2))
    )


_SwhIPSourceGuardSettingsPort4_Type.__name__ = "Integer32"
_SwhIPSourceGuardSettingsPort4_Object = MibScalar
swhIPSourceGuardSettingsPort4 = _SwhIPSourceGuardSettingsPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 2, 4),
    _SwhIPSourceGuardSettingsPort4_Type()
)
swhIPSourceGuardSettingsPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPSourceGuardSettingsPort4.setStatus("mandatory")


class _SwhIPSourceGuardSettingsPort5_Type(Integer32):
    """Custom type swhIPSourceGuardSettingsPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-ip", 0),
          ("dhcp", 1),
          ("unlimited", 2))
    )


_SwhIPSourceGuardSettingsPort5_Type.__name__ = "Integer32"
_SwhIPSourceGuardSettingsPort5_Object = MibScalar
swhIPSourceGuardSettingsPort5 = _SwhIPSourceGuardSettingsPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 2, 5),
    _SwhIPSourceGuardSettingsPort5_Type()
)
swhIPSourceGuardSettingsPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPSourceGuardSettingsPort5.setStatus("mandatory")


class _SwhIPSourceGuardSettingsPort6_Type(Integer32):
    """Custom type swhIPSourceGuardSettingsPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fix-ip", 0),
          ("dhcp", 1),
          ("unlimited", 2))
    )


_SwhIPSourceGuardSettingsPort6_Type.__name__ = "Integer32"
_SwhIPSourceGuardSettingsPort6_Object = MibScalar
swhIPSourceGuardSettingsPort6 = _SwhIPSourceGuardSettingsPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 2, 6),
    _SwhIPSourceGuardSettingsPort6_Type()
)
swhIPSourceGuardSettingsPort6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhIPSourceGuardSettingsPort6.setStatus("mandatory")
_SwhDHCPSnooping_ObjectIdentity = ObjectIdentity
swhDHCPSnooping = _SwhDHCPSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3)
)


class _SwhFilterConfigDHCPSnooping_Type(Integer32):
    """Custom type swhFilterConfigDHCPSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhFilterConfigDHCPSnooping_Type.__name__ = "Integer32"
_SwhFilterConfigDHCPSnooping_Object = MibScalar
swhFilterConfigDHCPSnooping = _SwhFilterConfigDHCPSnooping_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 1),
    _SwhFilterConfigDHCPSnooping_Type()
)
swhFilterConfigDHCPSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFilterConfigDHCPSnooping.setStatus("mandatory")


class _SwhFilterConfigDefaultDHCPInitiatedTime_Type(Integer32):
    """Custom type swhFilterConfigDefaultDHCPInitiatedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_SwhFilterConfigDefaultDHCPInitiatedTime_Type.__name__ = "Integer32"
_SwhFilterConfigDefaultDHCPInitiatedTime_Object = MibScalar
swhFilterConfigDefaultDHCPInitiatedTime = _SwhFilterConfigDefaultDHCPInitiatedTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 2),
    _SwhFilterConfigDefaultDHCPInitiatedTime_Type()
)
swhFilterConfigDefaultDHCPInitiatedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFilterConfigDefaultDHCPInitiatedTime.setStatus("mandatory")


class _SwhFilterConfigDefaultDHCPLeasedTime_Type(Integer32):
    """Custom type swhFilterConfigDefaultDHCPLeasedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 259200),
    )


_SwhFilterConfigDefaultDHCPLeasedTime_Type.__name__ = "Integer32"
_SwhFilterConfigDefaultDHCPLeasedTime_Object = MibScalar
swhFilterConfigDefaultDHCPLeasedTime = _SwhFilterConfigDefaultDHCPLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 3),
    _SwhFilterConfigDefaultDHCPLeasedTime_Type()
)
swhFilterConfigDefaultDHCPLeasedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFilterConfigDefaultDHCPLeasedTime.setStatus("mandatory")
_SwhSecurityDHCPServerTrustPort_ObjectIdentity = ObjectIdentity
swhSecurityDHCPServerTrustPort = _SwhSecurityDHCPServerTrustPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 7)
)
_SwhSecurityDHCPServerTable_Object = MibTable
swhSecurityDHCPServerTable = _SwhSecurityDHCPServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 7, 1)
)
if mibBuilder.loadTexts:
    swhSecurityDHCPServerTable.setStatus("mandatory")
_SwhSecurityDHCPServerTableEntry_Object = MibTableRow
swhSecurityDHCPServerTableEntry = _SwhSecurityDHCPServerTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 7, 1, 1)
)
swhSecurityDHCPServerTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhSecurityDHCPServerTableIndex"),
)
if mibBuilder.loadTexts:
    swhSecurityDHCPServerTableEntry.setStatus("mandatory")


class _SwhSecurityDHCPServerTableIndex_Type(Integer32):
    """Custom type swhSecurityDHCPServerTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhSecurityDHCPServerTableIndex_Type.__name__ = "Integer32"
_SwhSecurityDHCPServerTableIndex_Object = MibTableColumn
swhSecurityDHCPServerTableIndex = _SwhSecurityDHCPServerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 7, 1, 1, 1),
    _SwhSecurityDHCPServerTableIndex_Type()
)
swhSecurityDHCPServerTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhSecurityDHCPServerTableIndex.setStatus("mandatory")


class _SwhSecurityDHCPServerTableState_Type(Integer32):
    """Custom type swhSecurityDHCPServerTableState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhSecurityDHCPServerTableState_Type.__name__ = "Integer32"
_SwhSecurityDHCPServerTableState_Object = MibTableColumn
swhSecurityDHCPServerTableState = _SwhSecurityDHCPServerTableState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 7, 1, 1, 2),
    _SwhSecurityDHCPServerTableState_Type()
)
swhSecurityDHCPServerTableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityDHCPServerTableState.setStatus("mandatory")
_SwhSecurityDHCPServerTrustIP_ObjectIdentity = ObjectIdentity
swhSecurityDHCPServerTrustIP = _SwhSecurityDHCPServerTrustIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 8)
)


class _SwhSecurityDHCPServerIP_Type(Integer32):
    """Custom type swhSecurityDHCPServerIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhSecurityDHCPServerIP_Type.__name__ = "Integer32"
_SwhSecurityDHCPServerIP_Object = MibScalar
swhSecurityDHCPServerIP = _SwhSecurityDHCPServerIP_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 8, 1),
    _SwhSecurityDHCPServerIP_Type()
)
swhSecurityDHCPServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityDHCPServerIP.setStatus("mandatory")
_SwhSecurityDHCPServerIPTable_Object = MibTable
swhSecurityDHCPServerIPTable = _SwhSecurityDHCPServerIPTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 8, 2)
)
if mibBuilder.loadTexts:
    swhSecurityDHCPServerIPTable.setStatus("mandatory")
_SwhSecurityDHCPServerIPEntry_Object = MibTableRow
swhSecurityDHCPServerIPEntry = _SwhSecurityDHCPServerIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 8, 2, 1)
)
swhSecurityDHCPServerIPEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhSecurityDHCPServerIPIndex"),
)
if mibBuilder.loadTexts:
    swhSecurityDHCPServerIPEntry.setStatus("mandatory")


class _SwhSecurityDHCPServerIPIndex_Type(Integer32):
    """Custom type swhSecurityDHCPServerIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhSecurityDHCPServerIPIndex_Type.__name__ = "Integer32"
_SwhSecurityDHCPServerIPIndex_Object = MibTableColumn
swhSecurityDHCPServerIPIndex = _SwhSecurityDHCPServerIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 8, 2, 1, 1),
    _SwhSecurityDHCPServerIPIndex_Type()
)
swhSecurityDHCPServerIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhSecurityDHCPServerIPIndex.setStatus("mandatory")
_SwhSecurityDHCPServerIPIPAddress_Type = DisplayString
_SwhSecurityDHCPServerIPIPAddress_Object = MibTableColumn
swhSecurityDHCPServerIPIPAddress = _SwhSecurityDHCPServerIPIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 8, 2, 1, 4),
    _SwhSecurityDHCPServerIPIPAddress_Type()
)
swhSecurityDHCPServerIPIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityDHCPServerIPIPAddress.setStatus("mandatory")
_SwhSecurityDHCPServerIPIPv6Address_Type = DisplayString
_SwhSecurityDHCPServerIPIPv6Address_Object = MibTableColumn
swhSecurityDHCPServerIPIPv6Address = _SwhSecurityDHCPServerIPIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 8, 2, 1, 5),
    _SwhSecurityDHCPServerIPIPv6Address_Type()
)
swhSecurityDHCPServerIPIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityDHCPServerIPIPv6Address.setStatus("mandatory")


class _SwhSecurityDHCPServerIPDelete_Type(Integer32):
    """Custom type swhSecurityDHCPServerIPDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhSecurityDHCPServerIPDelete_Type.__name__ = "Integer32"
_SwhSecurityDHCPServerIPDelete_Object = MibTableColumn
swhSecurityDHCPServerIPDelete = _SwhSecurityDHCPServerIPDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 3, 8, 2, 1, 10),
    _SwhSecurityDHCPServerIPDelete_Type()
)
swhSecurityDHCPServerIPDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityDHCPServerIPDelete.setStatus("mandatory")
_SwhStaticIPTableConfiguration_ObjectIdentity = ObjectIdentity
swhStaticIPTableConfiguration = _SwhStaticIPTableConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4)
)
_SwhStaticIPTable_Object = MibTable
swhStaticIPTable = _SwhStaticIPTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1)
)
if mibBuilder.loadTexts:
    swhStaticIPTable.setStatus("mandatory")
_SwhStaticIPTableEntry_Object = MibTableRow
swhStaticIPTableEntry = _SwhStaticIPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1, 1)
)
swhStaticIPTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhStaticIPTableIndex"),
)
if mibBuilder.loadTexts:
    swhStaticIPTableEntry.setStatus("mandatory")


class _SwhStaticIPTableIndex_Type(Integer32):
    """Custom type swhStaticIPTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhStaticIPTableIndex_Type.__name__ = "Integer32"
_SwhStaticIPTableIndex_Object = MibTableColumn
swhStaticIPTableIndex = _SwhStaticIPTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1, 1, 1),
    _SwhStaticIPTableIndex_Type()
)
swhStaticIPTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhStaticIPTableIndex.setStatus("mandatory")


class _SwhStaticIPTableValid_Type(Integer32):
    """Custom type swhStaticIPTableValid based on Integer32"""
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


_SwhStaticIPTableValid_Type.__name__ = "Integer32"
_SwhStaticIPTableValid_Object = MibTableColumn
swhStaticIPTableValid = _SwhStaticIPTableValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1, 1, 2),
    _SwhStaticIPTableValid_Type()
)
swhStaticIPTableValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhStaticIPTableValid.setStatus("mandatory")
_SwhStaticIPTableIPAddress_Type = IpAddress
_SwhStaticIPTableIPAddress_Object = MibTableColumn
swhStaticIPTableIPAddress = _SwhStaticIPTableIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1, 1, 3),
    _SwhStaticIPTableIPAddress_Type()
)
swhStaticIPTableIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticIPTableIPAddress.setStatus("mandatory")


class _SwhStaticIPTableVLANID_Type(Integer32):
    """Custom type swhStaticIPTableVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwhStaticIPTableVLANID_Type.__name__ = "Integer32"
_SwhStaticIPTableVLANID_Object = MibTableColumn
swhStaticIPTableVLANID = _SwhStaticIPTableVLANID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1, 1, 5),
    _SwhStaticIPTableVLANID_Type()
)
swhStaticIPTableVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticIPTableVLANID.setStatus("mandatory")


class _SwhStaticIPTablePort_Type(Integer32):
    """Custom type swhStaticIPTablePort based on Integer32"""
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
        *(("port01", 0),
          ("port02", 1),
          ("port03", 2),
          ("port04", 3),
          ("port05", 4),
          ("port06", 5))
    )


_SwhStaticIPTablePort_Type.__name__ = "Integer32"
_SwhStaticIPTablePort_Object = MibTableColumn
swhStaticIPTablePort = _SwhStaticIPTablePort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1, 1, 6),
    _SwhStaticIPTablePort_Type()
)
swhStaticIPTablePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticIPTablePort.setStatus("mandatory")


class _SwhStaticIPTableDelete_Type(Integer32):
    """Custom type swhStaticIPTableDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhStaticIPTableDelete_Type.__name__ = "Integer32"
_SwhStaticIPTableDelete_Object = MibTableColumn
swhStaticIPTableDelete = _SwhStaticIPTableDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1, 1, 7),
    _SwhStaticIPTableDelete_Type()
)
swhStaticIPTableDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticIPTableDelete.setStatus("mandatory")
_SwhStaticIPTableIPv6Address_Type = DisplayString
_SwhStaticIPTableIPv6Address_Object = MibTableColumn
swhStaticIPTableIPv6Address = _SwhStaticIPTableIPv6Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 4, 1, 1, 8),
    _SwhStaticIPTableIPv6Address_Type()
)
swhStaticIPTableIPv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStaticIPTableIPv6Address.setStatus("mandatory")
_SwhDHCPOpt82Configuration_ObjectIdentity = ObjectIdentity
swhDHCPOpt82Configuration = _SwhDHCPOpt82Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7)
)


class _SwhDHCPOpt82CircuitIDPortList_Type(DisplayString):
    """Custom type swhDHCPOpt82CircuitIDPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhDHCPOpt82CircuitIDPortList_Type.__name__ = "DisplayString"
_SwhDHCPOpt82CircuitIDPortList_Object = MibScalar
swhDHCPOpt82CircuitIDPortList = _SwhDHCPOpt82CircuitIDPortList_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 2),
    _SwhDHCPOpt82CircuitIDPortList_Type()
)
swhDHCPOpt82CircuitIDPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82CircuitIDPortList.setStatus("mandatory")
_SwhDHCPOpt82CircuitIDTable_Object = MibTable
swhDHCPOpt82CircuitIDTable = _SwhDHCPOpt82CircuitIDTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 3)
)
if mibBuilder.loadTexts:
    swhDHCPOpt82CircuitIDTable.setStatus("mandatory")
_SwhDHCPOpt82CircuitIDTableEntry_Object = MibTableRow
swhDHCPOpt82CircuitIDTableEntry = _SwhDHCPOpt82CircuitIDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 3, 1)
)
swhDHCPOpt82CircuitIDTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDHCPOpt82CircuitIDTableIndex"),
)
if mibBuilder.loadTexts:
    swhDHCPOpt82CircuitIDTableEntry.setStatus("mandatory")


class _SwhDHCPOpt82CircuitIDTableIndex_Type(Integer32):
    """Custom type swhDHCPOpt82CircuitIDTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDHCPOpt82CircuitIDTableIndex_Type.__name__ = "Integer32"
_SwhDHCPOpt82CircuitIDTableIndex_Object = MibTableColumn
swhDHCPOpt82CircuitIDTableIndex = _SwhDHCPOpt82CircuitIDTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 3, 1, 1),
    _SwhDHCPOpt82CircuitIDTableIndex_Type()
)
swhDHCPOpt82CircuitIDTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDHCPOpt82CircuitIDTableIndex.setStatus("mandatory")
_SwhDHCPOpt82CircuitIDTableCircuitID_Type = DisplayString
_SwhDHCPOpt82CircuitIDTableCircuitID_Object = MibTableColumn
swhDHCPOpt82CircuitIDTableCircuitID = _SwhDHCPOpt82CircuitIDTableCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 3, 1, 3),
    _SwhDHCPOpt82CircuitIDTableCircuitID_Type()
)
swhDHCPOpt82CircuitIDTableCircuitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82CircuitIDTableCircuitID.setStatus("mandatory")


class _SwhDHCPOpt82CircuitIDTableDelete_Type(Integer32):
    """Custom type swhDHCPOpt82CircuitIDTableDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhDHCPOpt82CircuitIDTableDelete_Type.__name__ = "Integer32"
_SwhDHCPOpt82CircuitIDTableDelete_Object = MibTableColumn
swhDHCPOpt82CircuitIDTableDelete = _SwhDHCPOpt82CircuitIDTableDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 3, 1, 5),
    _SwhDHCPOpt82CircuitIDTableDelete_Type()
)
swhDHCPOpt82CircuitIDTableDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82CircuitIDTableDelete.setStatus("mandatory")


class _SwhDHCPOpt82RemoteIDEnable_Type(Integer32):
    """Custom type swhDHCPOpt82RemoteIDEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDHCPOpt82RemoteIDEnable_Type.__name__ = "Integer32"
_SwhDHCPOpt82RemoteIDEnable_Object = MibScalar
swhDHCPOpt82RemoteIDEnable = _SwhDHCPOpt82RemoteIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 4),
    _SwhDHCPOpt82RemoteIDEnable_Type()
)
swhDHCPOpt82RemoteIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82RemoteIDEnable.setStatus("mandatory")
_SwhDHCPOpt82RemoteID_Type = DisplayString
_SwhDHCPOpt82RemoteID_Object = MibScalar
swhDHCPOpt82RemoteID = _SwhDHCPOpt82RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 5),
    _SwhDHCPOpt82RemoteID_Type()
)
swhDHCPOpt82RemoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82RemoteID.setStatus("mandatory")


class _SwhDHCPOpt82CircuitIDFormattedPortList_Type(DisplayString):
    """Custom type swhDHCPOpt82CircuitIDFormattedPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhDHCPOpt82CircuitIDFormattedPortList_Type.__name__ = "DisplayString"
_SwhDHCPOpt82CircuitIDFormattedPortList_Object = MibScalar
swhDHCPOpt82CircuitIDFormattedPortList = _SwhDHCPOpt82CircuitIDFormattedPortList_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 6),
    _SwhDHCPOpt82CircuitIDFormattedPortList_Type()
)
swhDHCPOpt82CircuitIDFormattedPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82CircuitIDFormattedPortList.setStatus("mandatory")


class _SwhDHCPOpt82RemoteIDFormattedEnable_Type(Integer32):
    """Custom type swhDHCPOpt82RemoteIDFormattedEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDHCPOpt82RemoteIDFormattedEnable_Type.__name__ = "Integer32"
_SwhDHCPOpt82RemoteIDFormattedEnable_Object = MibScalar
swhDHCPOpt82RemoteIDFormattedEnable = _SwhDHCPOpt82RemoteIDFormattedEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 7, 7),
    _SwhDHCPOpt82RemoteIDFormattedEnable_Type()
)
swhDHCPOpt82RemoteIDFormattedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDHCPOpt82RemoteIDFormattedEnable.setStatus("mandatory")
_SwhMacLimiters_ObjectIdentity = ObjectIdentity
swhMacLimiters = _SwhMacLimiters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 11)
)


class _SwhMacLimitersEnable_Type(Integer32):
    """Custom type swhMacLimitersEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhMacLimitersEnable_Type.__name__ = "Integer32"
_SwhMacLimitersEnable_Object = MibScalar
swhMacLimitersEnable = _SwhMacLimitersEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 11, 1),
    _SwhMacLimitersEnable_Type()
)
swhMacLimitersEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacLimitersEnable.setStatus("mandatory")


class _SwhMacLimitersThresholdInterval_Type(Integer32):
    """Custom type swhMacLimitersThresholdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 86400),
    )


_SwhMacLimitersThresholdInterval_Type.__name__ = "Integer32"
_SwhMacLimitersThresholdInterval_Object = MibScalar
swhMacLimitersThresholdInterval = _SwhMacLimitersThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 11, 3),
    _SwhMacLimitersThresholdInterval_Type()
)
swhMacLimitersThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacLimitersThresholdInterval.setStatus("mandatory")
_SwhMacLimitersPortTable_Object = MibTable
swhMacLimitersPortTable = _SwhMacLimitersPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 11, 5)
)
if mibBuilder.loadTexts:
    swhMacLimitersPortTable.setStatus("mandatory")
_SwhMacLimitersPortEntry_Object = MibTableRow
swhMacLimitersPortEntry = _SwhMacLimitersPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 11, 5, 1)
)
swhMacLimitersPortEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhMacLimitersPortIndex"),
)
if mibBuilder.loadTexts:
    swhMacLimitersPortEntry.setStatus("mandatory")


class _SwhMacLimitersPortIndex_Type(Integer32):
    """Custom type swhMacLimitersPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacLimitersPortIndex_Type.__name__ = "Integer32"
_SwhMacLimitersPortIndex_Object = MibTableColumn
swhMacLimitersPortIndex = _SwhMacLimitersPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 11, 5, 1, 1),
    _SwhMacLimitersPortIndex_Type()
)
swhMacLimitersPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhMacLimitersPortIndex.setStatus("mandatory")


class _SwhMacLimitersPortEnable_Type(Integer32):
    """Custom type swhMacLimitersPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhMacLimitersPortEnable_Type.__name__ = "Integer32"
_SwhMacLimitersPortEnable_Object = MibTableColumn
swhMacLimitersPortEnable = _SwhMacLimitersPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 11, 5, 1, 2),
    _SwhMacLimitersPortEnable_Type()
)
swhMacLimitersPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacLimitersPortEnable.setStatus("mandatory")
_SwhMacLimitersPortLimit_Type = Integer32
_SwhMacLimitersPortLimit_Object = MibTableColumn
swhMacLimitersPortLimit = _SwhMacLimitersPortLimit_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 11, 5, 1, 3),
    _SwhMacLimitersPortLimit_Type()
)
swhMacLimitersPortLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacLimitersPortLimit.setStatus("mandatory")
_SwhStormControl_ObjectIdentity = ObjectIdentity
swhStormControl = _SwhStormControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12)
)


class _SwhThresholdInterval_Type(Integer32):
    """Custom type swhThresholdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhThresholdInterval_Type.__name__ = "Integer32"
_SwhThresholdInterval_Object = MibScalar
swhThresholdInterval = _SwhThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 3),
    _SwhThresholdInterval_Type()
)
swhThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhThresholdInterval.setStatus("mandatory")
_SwhSecurityStormControlTable_Object = MibTable
swhSecurityStormControlTable = _SwhSecurityStormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 9)
)
if mibBuilder.loadTexts:
    swhSecurityStormControlTable.setStatus("mandatory")
_SwhSecurityStormControlEntry_Object = MibTableRow
swhSecurityStormControlEntry = _SwhSecurityStormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 9, 1)
)
swhSecurityStormControlEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhSecurityStormControlIndex"),
)
if mibBuilder.loadTexts:
    swhSecurityStormControlEntry.setStatus("mandatory")


class _SwhSecurityStormControlIndex_Type(Integer32):
    """Custom type swhSecurityStormControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhSecurityStormControlIndex_Type.__name__ = "Integer32"
_SwhSecurityStormControlIndex_Object = MibTableColumn
swhSecurityStormControlIndex = _SwhSecurityStormControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 9, 1, 1),
    _SwhSecurityStormControlIndex_Type()
)
swhSecurityStormControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSecurityStormControlIndex.setStatus("mandatory")


class _SwhSecurityStormControlBroadcastRate_Type(Integer32):
    """Custom type swhSecurityStormControlBroadcastRate based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("off", 0),
          ("rate-1", 1),
          ("rate-2", 2),
          ("rate-4", 3),
          ("rate-8", 4),
          ("rate-16", 5),
          ("rate-32", 6),
          ("rate-64", 7),
          ("rate-128", 8),
          ("rate-256", 9),
          ("rate-512", 10),
          ("rate-1K", 11),
          ("rate-2K", 12),
          ("rate-4K", 13),
          ("rate-8K", 14),
          ("rate-16K", 15),
          ("rate-32K", 16),
          ("rate-64K", 17),
          ("rate-128K", 18),
          ("rate-256K", 19))
    )


_SwhSecurityStormControlBroadcastRate_Type.__name__ = "Integer32"
_SwhSecurityStormControlBroadcastRate_Object = MibTableColumn
swhSecurityStormControlBroadcastRate = _SwhSecurityStormControlBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 9, 1, 8),
    _SwhSecurityStormControlBroadcastRate_Type()
)
swhSecurityStormControlBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityStormControlBroadcastRate.setStatus("mandatory")


class _SwhSecurityStormControlUnknownMulticastRate_Type(Integer32):
    """Custom type swhSecurityStormControlUnknownMulticastRate based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("off", 0),
          ("rate-1", 1),
          ("rate-2", 2),
          ("rate-4", 3),
          ("rate-8", 4),
          ("rate-16", 5),
          ("rate-32", 6),
          ("rate-64", 7),
          ("rate-128", 8),
          ("rate-256", 9),
          ("rate-512", 10),
          ("rate-1K", 11),
          ("rate-2K", 12),
          ("rate-4K", 13),
          ("rate-8K", 14),
          ("rate-16K", 15),
          ("rate-32K", 16),
          ("rate-64K", 17),
          ("rate-128K", 18),
          ("rate-256K", 19))
    )


_SwhSecurityStormControlUnknownMulticastRate_Type.__name__ = "Integer32"
_SwhSecurityStormControlUnknownMulticastRate_Object = MibTableColumn
swhSecurityStormControlUnknownMulticastRate = _SwhSecurityStormControlUnknownMulticastRate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 9, 1, 10),
    _SwhSecurityStormControlUnknownMulticastRate_Type()
)
swhSecurityStormControlUnknownMulticastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityStormControlUnknownMulticastRate.setStatus("mandatory")


class _SwhSecurityStormControlUnknownUnicastRate_Type(Integer32):
    """Custom type swhSecurityStormControlUnknownUnicastRate based on Integer32"""
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("off", 0),
          ("rate-1", 1),
          ("rate-2", 2),
          ("rate-4", 3),
          ("rate-8", 4),
          ("rate-16", 5),
          ("rate-32", 6),
          ("rate-64", 7),
          ("rate-128", 8),
          ("rate-256", 9),
          ("rate-512", 10),
          ("rate-1K", 11),
          ("rate-2K", 12),
          ("rate-4K", 13),
          ("rate-8K", 14),
          ("rate-16K", 15),
          ("rate-32K", 16),
          ("rate-64K", 17),
          ("rate-128K", 18),
          ("rate-256K", 19))
    )


_SwhSecurityStormControlUnknownUnicastRate_Type.__name__ = "Integer32"
_SwhSecurityStormControlUnknownUnicastRate_Object = MibTableColumn
swhSecurityStormControlUnknownUnicastRate = _SwhSecurityStormControlUnknownUnicastRate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 9, 1, 11),
    _SwhSecurityStormControlUnknownUnicastRate_Type()
)
swhSecurityStormControlUnknownUnicastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSecurityStormControlUnknownUnicastRate.setStatus("mandatory")
_SwhSecurityStormControlPortConfigPort_Type = DisplayString
_SwhSecurityStormControlPortConfigPort_Object = MibTableColumn
swhSecurityStormControlPortConfigPort = _SwhSecurityStormControlPortConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 9, 1, 12),
    _SwhSecurityStormControlPortConfigPort_Type()
)
swhSecurityStormControlPortConfigPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSecurityStormControlPortConfigPort.setStatus("mandatory")


class _SwhStormControlEnable_Type(Integer32):
    """Custom type swhStormControlEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhStormControlEnable_Type.__name__ = "Integer32"
_SwhStormControlEnable_Object = MibScalar
swhStormControlEnable = _SwhStormControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 12, 16),
    _SwhStormControlEnable_Type()
)
swhStormControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStormControlEnable.setStatus("mandatory")
_SwhPortIsolationConfiguration_ObjectIdentity = ObjectIdentity
swhPortIsolationConfiguration = _SwhPortIsolationConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 13)
)


class _SwhPortIsolationConfigPortIsolation_Type(Integer32):
    """Custom type swhPortIsolationConfigPortIsolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhPortIsolationConfigPortIsolation_Type.__name__ = "Integer32"
_SwhPortIsolationConfigPortIsolation_Object = MibScalar
swhPortIsolationConfigPortIsolation = _SwhPortIsolationConfigPortIsolation_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 13, 1),
    _SwhPortIsolationConfigPortIsolation_Type()
)
swhPortIsolationConfigPortIsolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortIsolationConfigPortIsolation.setStatus("mandatory")


class _SwhPortIsolationConfigUplinkPortList_Type(DisplayString):
    """Custom type swhPortIsolationConfigUplinkPortList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPortIsolationConfigUplinkPortList_Type.__name__ = "DisplayString"
_SwhPortIsolationConfigUplinkPortList_Object = MibScalar
swhPortIsolationConfigUplinkPortList = _SwhPortIsolationConfigUplinkPortList_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 80, 13, 2),
    _SwhPortIsolationConfigUplinkPortList_Type()
)
swhPortIsolationConfigUplinkPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhPortIsolationConfigUplinkPortList.setStatus("mandatory")
_SwhPoEManagementAndMonitor_ObjectIdentity = ObjectIdentity
swhPoEManagementAndMonitor = _SwhPoEManagementAndMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 89)
)
_SwhFastRedundancy_ObjectIdentity = ObjectIdentity
swhFastRedundancy = _SwhFastRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91)
)
_SwhFastRedundancyConfigTable_Object = MibTable
swhFastRedundancyConfigTable = _SwhFastRedundancyConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1)
)
if mibBuilder.loadTexts:
    swhFastRedundancyConfigTable.setStatus("mandatory")
_SwhFastRedundancyConfigEntry_Object = MibTableRow
swhFastRedundancyConfigEntry = _SwhFastRedundancyConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1)
)
swhFastRedundancyConfigEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhFastRedundancyConfigIndex"),
)
if mibBuilder.loadTexts:
    swhFastRedundancyConfigEntry.setStatus("mandatory")


class _SwhFastRedundancyConfigIndex_Type(Integer32):
    """Custom type swhFastRedundancyConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhFastRedundancyConfigIndex_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigIndex_Object = MibTableColumn
swhFastRedundancyConfigIndex = _SwhFastRedundancyConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 1),
    _SwhFastRedundancyConfigIndex_Type()
)
swhFastRedundancyConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigIndex.setStatus("mandatory")


class _SwhFastRedundancyConfigValid_Type(Integer32):
    """Custom type swhFastRedundancyConfigValid based on Integer32"""
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


_SwhFastRedundancyConfigValid_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigValid_Object = MibTableColumn
swhFastRedundancyConfigValid = _SwhFastRedundancyConfigValid_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 2),
    _SwhFastRedundancyConfigValid_Type()
)
swhFastRedundancyConfigValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigValid.setStatus("mandatory")


class _SwhFastRedundancyConfigGroupID_Type(Integer32):
    """Custom type swhFastRedundancyConfigGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("id-1", 1),
          ("id-2", 2))
    )


_SwhFastRedundancyConfigGroupID_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigGroupID_Object = MibTableColumn
swhFastRedundancyConfigGroupID = _SwhFastRedundancyConfigGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 3),
    _SwhFastRedundancyConfigGroupID_Type()
)
swhFastRedundancyConfigGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigGroupID.setStatus("mandatory")
_SwhFastRedundancyConfigDescription_Type = DisplayString
_SwhFastRedundancyConfigDescription_Object = MibTableColumn
swhFastRedundancyConfigDescription = _SwhFastRedundancyConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 4),
    _SwhFastRedundancyConfigDescription_Type()
)
swhFastRedundancyConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigDescription.setStatus("mandatory")


class _SwhFastRedundancyConfigProtocol_Type(Integer32):
    """Custom type swhFastRedundancyConfigProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fast-ringv2", 0),
          ("chain", 1))
    )


_SwhFastRedundancyConfigProtocol_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigProtocol_Object = MibTableColumn
swhFastRedundancyConfigProtocol = _SwhFastRedundancyConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 5),
    _SwhFastRedundancyConfigProtocol_Type()
)
swhFastRedundancyConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigProtocol.setStatus("mandatory")


class _SwhFastRedundancyConfigEnable_Type(Integer32):
    """Custom type swhFastRedundancyConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhFastRedundancyConfigEnable_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigEnable_Object = MibTableColumn
swhFastRedundancyConfigEnable = _SwhFastRedundancyConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 6),
    _SwhFastRedundancyConfigEnable_Type()
)
swhFastRedundancyConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigEnable.setStatus("mandatory")


class _SwhFastRedundancyConfigRole_Type(Integer32):
    """Custom type swhFastRedundancyConfigRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", -1),
          ("slave", 0),
          ("master", 1))
    )


_SwhFastRedundancyConfigRole_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigRole_Object = MibTableColumn
swhFastRedundancyConfigRole = _SwhFastRedundancyConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 7),
    _SwhFastRedundancyConfigRole_Type()
)
swhFastRedundancyConfigRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigRole.setStatus("mandatory")


class _SwhFastRedundancyConfigPort1_Type(Integer32):
    """Custom type swhFastRedundancyConfigPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("port01", 1),
          ("port02", 2),
          ("port03", 3),
          ("port04", 4),
          ("port05", 5),
          ("port06", 6))
    )


_SwhFastRedundancyConfigPort1_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigPort1_Object = MibTableColumn
swhFastRedundancyConfigPort1 = _SwhFastRedundancyConfigPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 8),
    _SwhFastRedundancyConfigPort1_Type()
)
swhFastRedundancyConfigPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigPort1.setStatus("mandatory")


class _SwhFastRedundancyConfigPort1Role_Type(Integer32):
    """Custom type swhFastRedundancyConfigPort1Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("member", 0),
          ("head", 1),
          ("tail", 2))
    )


_SwhFastRedundancyConfigPort1Role_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigPort1Role_Object = MibTableColumn
swhFastRedundancyConfigPort1Role = _SwhFastRedundancyConfigPort1Role_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 9),
    _SwhFastRedundancyConfigPort1Role_Type()
)
swhFastRedundancyConfigPort1Role.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigPort1Role.setStatus("mandatory")


class _SwhFastRedundancyConfigPort2_Type(Integer32):
    """Custom type swhFastRedundancyConfigPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("port01", 1),
          ("port02", 2),
          ("port03", 3),
          ("port04", 4),
          ("port05", 5),
          ("port06", 6))
    )


_SwhFastRedundancyConfigPort2_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigPort2_Object = MibTableColumn
swhFastRedundancyConfigPort2 = _SwhFastRedundancyConfigPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 10),
    _SwhFastRedundancyConfigPort2_Type()
)
swhFastRedundancyConfigPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigPort2.setStatus("mandatory")


class _SwhFastRedundancyConfigPort2Role_Type(Integer32):
    """Custom type swhFastRedundancyConfigPort2Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("member", 0)
    )


_SwhFastRedundancyConfigPort2Role_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigPort2Role_Object = MibTableColumn
swhFastRedundancyConfigPort2Role = _SwhFastRedundancyConfigPort2Role_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 11),
    _SwhFastRedundancyConfigPort2Role_Type()
)
swhFastRedundancyConfigPort2Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigPort2Role.setStatus("mandatory")


class _SwhFastRedundancyConfigDelete_Type(Integer32):
    """Custom type swhFastRedundancyConfigDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("delete", 1))
    )


_SwhFastRedundancyConfigDelete_Type.__name__ = "Integer32"
_SwhFastRedundancyConfigDelete_Object = MibTableColumn
swhFastRedundancyConfigDelete = _SwhFastRedundancyConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 4, 91, 1, 1, 13),
    _SwhFastRedundancyConfigDelete_Type()
)
swhFastRedundancyConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyConfigDelete.setStatus("mandatory")
_SwhSwitchMonitor_ObjectIdentity = ObjectIdentity
swhSwitchMonitor = _SwhSwitchMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5)
)
_SwhPortStatus_ObjectIdentity = ObjectIdentity
swhPortStatus = _SwhPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1)
)
_SwhPortStatusTable_Object = MibTable
swhPortStatusTable = _SwhPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1)
)
if mibBuilder.loadTexts:
    swhPortStatusTable.setStatus("mandatory")
_SwhPortStatusEntry_Object = MibTableRow
swhPortStatusEntry = _SwhPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1)
)
swhPortStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhPortStatusIndex"),
)
if mibBuilder.loadTexts:
    swhPortStatusEntry.setStatus("mandatory")


class _SwhPortStatusIndex_Type(Integer32):
    """Custom type swhPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhPortStatusIndex_Type.__name__ = "Integer32"
_SwhPortStatusIndex_Object = MibTableColumn
swhPortStatusIndex = _SwhPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1, 1),
    _SwhPortStatusIndex_Type()
)
swhPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhPortStatusIndex.setStatus("mandatory")
_SwhPortStatusDescription_Type = DisplayString
_SwhPortStatusDescription_Object = MibTableColumn
swhPortStatusDescription = _SwhPortStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1, 2),
    _SwhPortStatusDescription_Type()
)
swhPortStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortStatusDescription.setStatus("mandatory")


class _SwhPortStatusPortMedia_Type(Integer32):
    """Custom type swhPortStatusPortMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("tx", 1),
          ("fx", 2))
    )


_SwhPortStatusPortMedia_Type.__name__ = "Integer32"
_SwhPortStatusPortMedia_Object = MibTableColumn
swhPortStatusPortMedia = _SwhPortStatusPortMedia_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1, 3),
    _SwhPortStatusPortMedia_Type()
)
swhPortStatusPortMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortStatusPortMedia.setStatus("mandatory")


class _SwhPortStatusPortState_Type(Integer32):
    """Custom type swhPortStatusPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("disable", 0),
          ("blocking-listening", 1),
          ("learning", 2),
          ("forwarding", 3))
    )


_SwhPortStatusPortState_Type.__name__ = "Integer32"
_SwhPortStatusPortState_Object = MibTableColumn
swhPortStatusPortState = _SwhPortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1, 4),
    _SwhPortStatusPortState_Type()
)
swhPortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortStatusPortState.setStatus("mandatory")


class _SwhPortStatusPortLink_Type(Integer32):
    """Custom type swhPortStatusPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("up", 1),
          ("down", 2))
    )


_SwhPortStatusPortLink_Type.__name__ = "Integer32"
_SwhPortStatusPortLink_Object = MibTableColumn
swhPortStatusPortLink = _SwhPortStatusPortLink_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1, 5),
    _SwhPortStatusPortLink_Type()
)
swhPortStatusPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortStatusPortLink.setStatus("mandatory")


class _SwhPortStatusPortSpeed_Type(Integer32):
    """Custom type swhPortStatusPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1))
    )


_SwhPortStatusPortSpeed_Type.__name__ = "Integer32"
_SwhPortStatusPortSpeed_Object = MibTableColumn
swhPortStatusPortSpeed = _SwhPortStatusPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1, 6),
    _SwhPortStatusPortSpeed_Type()
)
swhPortStatusPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortStatusPortSpeed.setStatus("mandatory")


class _SwhPortStatusPortDuplex_Type(Integer32):
    """Custom type swhPortStatusPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("full", 1),
          ("half", 2))
    )


_SwhPortStatusPortDuplex_Type.__name__ = "Integer32"
_SwhPortStatusPortDuplex_Object = MibTableColumn
swhPortStatusPortDuplex = _SwhPortStatusPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1, 7),
    _SwhPortStatusPortDuplex_Type()
)
swhPortStatusPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortStatusPortDuplex.setStatus("mandatory")


class _SwhPortStatusPortFlowCtrl_Type(Integer32):
    """Custom type swhPortStatusPortFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("on", 1),
          ("off", 2))
    )


_SwhPortStatusPortFlowCtrl_Type.__name__ = "Integer32"
_SwhPortStatusPortFlowCtrl_Object = MibTableColumn
swhPortStatusPortFlowCtrl = _SwhPortStatusPortFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 1, 1, 1, 8),
    _SwhPortStatusPortFlowCtrl_Type()
)
swhPortStatusPortFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPortStatusPortFlowCtrl.setStatus("mandatory")
_Swh8021QTagVLAN_ObjectIdentity = ObjectIdentity
swh8021QTagVLAN = _Swh8021QTagVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3)
)
_Swh8021QTagVLANTable_Object = MibTable
swh8021QTagVLANTable = _Swh8021QTagVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1)
)
if mibBuilder.loadTexts:
    swh8021QTagVLANTable.setStatus("mandatory")
_Swh8021QTagVLANEntry_Object = MibTableRow
swh8021QTagVLANEntry = _Swh8021QTagVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1)
)
swh8021QTagVLANEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swh8021QTagVLANIndex"),
)
if mibBuilder.loadTexts:
    swh8021QTagVLANEntry.setStatus("mandatory")


class _Swh8021QTagVLANIndex_Type(Integer32):
    """Custom type swh8021QTagVLANIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Swh8021QTagVLANIndex_Type.__name__ = "Integer32"
_Swh8021QTagVLANIndex_Object = MibTableColumn
swh8021QTagVLANIndex = _Swh8021QTagVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 1),
    _Swh8021QTagVLANIndex_Type()
)
swh8021QTagVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swh8021QTagVLANIndex.setStatus("mandatory")


class _Swh8021QTagVLANVID_Type(Integer32):
    """Custom type swh8021QTagVLANVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Swh8021QTagVLANVID_Type.__name__ = "Integer32"
_Swh8021QTagVLANVID_Object = MibTableColumn
swh8021QTagVLANVID = _Swh8021QTagVLANVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 3),
    _Swh8021QTagVLANVID_Type()
)
swh8021QTagVLANVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANVID.setStatus("mandatory")
_Swh8021QTagVLANName_Type = DisplayString
_Swh8021QTagVLANName_Object = MibTableColumn
swh8021QTagVLANName = _Swh8021QTagVLANName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 4),
    _Swh8021QTagVLANName_Type()
)
swh8021QTagVLANName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANName.setStatus("mandatory")


class _Swh8021QTagVLANPort1_Type(Integer32):
    """Custom type swh8021QTagVLANPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("t", 2),
          ("u", 3),
          ("d", 4))
    )


_Swh8021QTagVLANPort1_Type.__name__ = "Integer32"
_Swh8021QTagVLANPort1_Object = MibTableColumn
swh8021QTagVLANPort1 = _Swh8021QTagVLANPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 5),
    _Swh8021QTagVLANPort1_Type()
)
swh8021QTagVLANPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANPort1.setStatus("mandatory")


class _Swh8021QTagVLANPort2_Type(Integer32):
    """Custom type swh8021QTagVLANPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("t", 2),
          ("u", 3),
          ("d", 4))
    )


_Swh8021QTagVLANPort2_Type.__name__ = "Integer32"
_Swh8021QTagVLANPort2_Object = MibTableColumn
swh8021QTagVLANPort2 = _Swh8021QTagVLANPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 6),
    _Swh8021QTagVLANPort2_Type()
)
swh8021QTagVLANPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANPort2.setStatus("mandatory")


class _Swh8021QTagVLANPort3_Type(Integer32):
    """Custom type swh8021QTagVLANPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("t", 2),
          ("u", 3),
          ("d", 4))
    )


_Swh8021QTagVLANPort3_Type.__name__ = "Integer32"
_Swh8021QTagVLANPort3_Object = MibTableColumn
swh8021QTagVLANPort3 = _Swh8021QTagVLANPort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 7),
    _Swh8021QTagVLANPort3_Type()
)
swh8021QTagVLANPort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANPort3.setStatus("mandatory")


class _Swh8021QTagVLANPort4_Type(Integer32):
    """Custom type swh8021QTagVLANPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("t", 2),
          ("u", 3),
          ("d", 4))
    )


_Swh8021QTagVLANPort4_Type.__name__ = "Integer32"
_Swh8021QTagVLANPort4_Object = MibTableColumn
swh8021QTagVLANPort4 = _Swh8021QTagVLANPort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 8),
    _Swh8021QTagVLANPort4_Type()
)
swh8021QTagVLANPort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANPort4.setStatus("mandatory")


class _Swh8021QTagVLANPort5_Type(Integer32):
    """Custom type swh8021QTagVLANPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("t", 2),
          ("u", 3),
          ("d", 4))
    )


_Swh8021QTagVLANPort5_Type.__name__ = "Integer32"
_Swh8021QTagVLANPort5_Object = MibTableColumn
swh8021QTagVLANPort5 = _Swh8021QTagVLANPort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 9),
    _Swh8021QTagVLANPort5_Type()
)
swh8021QTagVLANPort5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANPort5.setStatus("mandatory")


class _Swh8021QTagVLANPort6_Type(Integer32):
    """Custom type swh8021QTagVLANPort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("t", 2),
          ("u", 3),
          ("d", 4))
    )


_Swh8021QTagVLANPort6_Type.__name__ = "Integer32"
_Swh8021QTagVLANPort6_Object = MibTableColumn
swh8021QTagVLANPort6 = _Swh8021QTagVLANPort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 10),
    _Swh8021QTagVLANPort6_Type()
)
swh8021QTagVLANPort6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANPort6.setStatus("mandatory")


class _Swh8021QTagVLANCPU_Type(Integer32):
    """Custom type swh8021QTagVLANCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_Swh8021QTagVLANCPU_Type.__name__ = "Integer32"
_Swh8021QTagVLANCPU_Object = MibTableColumn
swh8021QTagVLANCPU = _Swh8021QTagVLANCPU_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 3, 1, 1, 55),
    _Swh8021QTagVLANCPU_Type()
)
swh8021QTagVLANCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021QTagVLANCPU.setStatus("mandatory")
_SwhPortCountersRates_ObjectIdentity = ObjectIdentity
swhPortCountersRates = _SwhPortCountersRates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5)
)
_SwhCountersRatesTable_Object = MibTable
swhCountersRatesTable = _SwhCountersRatesTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1)
)
if mibBuilder.loadTexts:
    swhCountersRatesTable.setStatus("mandatory")
_SwhCountersRatesEntry_Object = MibTableRow
swhCountersRatesEntry = _SwhCountersRatesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1)
)
swhCountersRatesEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhCountersRatesIndex"),
)
if mibBuilder.loadTexts:
    swhCountersRatesEntry.setStatus("mandatory")


class _SwhCountersRatesIndex_Type(Integer32):
    """Custom type swhCountersRatesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhCountersRatesIndex_Type.__name__ = "Integer32"
_SwhCountersRatesIndex_Object = MibTableColumn
swhCountersRatesIndex = _SwhCountersRatesIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 1),
    _SwhCountersRatesIndex_Type()
)
swhCountersRatesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhCountersRatesIndex.setStatus("mandatory")
_SwhCountersRatesBytesReceived_Type = Counter32
_SwhCountersRatesBytesReceived_Object = MibTableColumn
swhCountersRatesBytesReceived = _SwhCountersRatesBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 2),
    _SwhCountersRatesBytesReceived_Type()
)
swhCountersRatesBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesBytesReceived.setStatus("mandatory")
_SwhCountersRatesFramesReceived_Type = Counter32
_SwhCountersRatesFramesReceived_Object = MibTableColumn
swhCountersRatesFramesReceived = _SwhCountersRatesFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 3),
    _SwhCountersRatesFramesReceived_Type()
)
swhCountersRatesFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesFramesReceived.setStatus("mandatory")
_SwhCountersRatesReceivedUtilization_Type = DisplayString
_SwhCountersRatesReceivedUtilization_Object = MibTableColumn
swhCountersRatesReceivedUtilization = _SwhCountersRatesReceivedUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 4),
    _SwhCountersRatesReceivedUtilization_Type()
)
swhCountersRatesReceivedUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesReceivedUtilization.setStatus("mandatory")
_SwhCountersRatesBytesSent_Type = Counter32
_SwhCountersRatesBytesSent_Object = MibTableColumn
swhCountersRatesBytesSent = _SwhCountersRatesBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 5),
    _SwhCountersRatesBytesSent_Type()
)
swhCountersRatesBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesBytesSent.setStatus("mandatory")
_SwhCountersRatesFramesSent_Type = Counter32
_SwhCountersRatesFramesSent_Object = MibTableColumn
swhCountersRatesFramesSent = _SwhCountersRatesFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 6),
    _SwhCountersRatesFramesSent_Type()
)
swhCountersRatesFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesFramesSent.setStatus("mandatory")
_SwhCountersRatesSentUtilization_Type = DisplayString
_SwhCountersRatesSentUtilization_Object = MibTableColumn
swhCountersRatesSentUtilization = _SwhCountersRatesSentUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 7),
    _SwhCountersRatesSentUtilization_Type()
)
swhCountersRatesSentUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesSentUtilization.setStatus("mandatory")
_SwhCountersRatesTotalBytes_Type = Counter32
_SwhCountersRatesTotalBytes_Object = MibTableColumn
swhCountersRatesTotalBytes = _SwhCountersRatesTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 8),
    _SwhCountersRatesTotalBytes_Type()
)
swhCountersRatesTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesTotalBytes.setStatus("mandatory")
_SwhCountersRatesTotalUtilization_Type = DisplayString
_SwhCountersRatesTotalUtilization_Object = MibTableColumn
swhCountersRatesTotalUtilization = _SwhCountersRatesTotalUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 9),
    _SwhCountersRatesTotalUtilization_Type()
)
swhCountersRatesTotalUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesTotalUtilization.setStatus("mandatory")
_SwhCountersRatesRxCRCError_Type = Counter32
_SwhCountersRatesRxCRCError_Object = MibTableColumn
swhCountersRatesRxCRCError = _SwhCountersRatesRxCRCError_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 10),
    _SwhCountersRatesRxCRCError_Type()
)
swhCountersRatesRxCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxCRCError.setStatus("mandatory")
_SwhCountersRatesRxFragments_Type = Counter32
_SwhCountersRatesRxFragments_Object = MibTableColumn
swhCountersRatesRxFragments = _SwhCountersRatesRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 11),
    _SwhCountersRatesRxFragments_Type()
)
swhCountersRatesRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFragments.setStatus("mandatory")
_SwhCountersRatesRxFilteredFrames_Type = Counter32
_SwhCountersRatesRxFilteredFrames_Object = MibTableColumn
swhCountersRatesRxFilteredFrames = _SwhCountersRatesRxFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 12),
    _SwhCountersRatesRxFilteredFrames_Type()
)
swhCountersRatesRxFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFilteredFrames.setStatus("mandatory")
_SwhCountersRatesRxAlignError_Type = Counter32
_SwhCountersRatesRxAlignError_Object = MibTableColumn
swhCountersRatesRxAlignError = _SwhCountersRatesRxAlignError_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 13),
    _SwhCountersRatesRxAlignError_Type()
)
swhCountersRatesRxAlignError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxAlignError.setStatus("mandatory")
_SwhCountersRatesRxUndersizeFrames_Type = Counter32
_SwhCountersRatesRxUndersizeFrames_Object = MibTableColumn
swhCountersRatesRxUndersizeFrames = _SwhCountersRatesRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 14),
    _SwhCountersRatesRxUndersizeFrames_Type()
)
swhCountersRatesRxUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxUndersizeFrames.setStatus("mandatory")
_SwhCountersRatesRxOversizeFrames_Type = Counter32
_SwhCountersRatesRxOversizeFrames_Object = MibTableColumn
swhCountersRatesRxOversizeFrames = _SwhCountersRatesRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 15),
    _SwhCountersRatesRxOversizeFrames_Type()
)
swhCountersRatesRxOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxOversizeFrames.setStatus("mandatory")
_SwhCountersRatesRxJabbers_Type = Counter32
_SwhCountersRatesRxJabbers_Object = MibTableColumn
swhCountersRatesRxJabbers = _SwhCountersRatesRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 16),
    _SwhCountersRatesRxJabbers_Type()
)
swhCountersRatesRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxJabbers.setStatus("mandatory")
_SwhCountersRatesRxDroppedFrames_Type = Counter32
_SwhCountersRatesRxDroppedFrames_Object = MibTableColumn
swhCountersRatesRxDroppedFrames = _SwhCountersRatesRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 17),
    _SwhCountersRatesRxDroppedFrames_Type()
)
swhCountersRatesRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxDroppedFrames.setStatus("mandatory")
_SwhCountersRatesTxLateCollision_Type = Counter32
_SwhCountersRatesTxLateCollision_Object = MibTableColumn
swhCountersRatesTxLateCollision = _SwhCountersRatesTxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 19),
    _SwhCountersRatesTxLateCollision_Type()
)
swhCountersRatesTxLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesTxLateCollision.setStatus("mandatory")
_SwhCountersRatesTxDeferred_Type = Counter32
_SwhCountersRatesTxDeferred_Object = MibTableColumn
swhCountersRatesTxDeferred = _SwhCountersRatesTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 20),
    _SwhCountersRatesTxDeferred_Type()
)
swhCountersRatesTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesTxDeferred.setStatus("mandatory")
_SwhCountersRatesRxFrames64_Type = Counter32
_SwhCountersRatesRxFrames64_Object = MibTableColumn
swhCountersRatesRxFrames64 = _SwhCountersRatesRxFrames64_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 22),
    _SwhCountersRatesRxFrames64_Type()
)
swhCountersRatesRxFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFrames64.setStatus("mandatory")
_SwhCountersRatesRxFrames65to127_Type = Counter32
_SwhCountersRatesRxFrames65to127_Object = MibTableColumn
swhCountersRatesRxFrames65to127 = _SwhCountersRatesRxFrames65to127_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 23),
    _SwhCountersRatesRxFrames65to127_Type()
)
swhCountersRatesRxFrames65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFrames65to127.setStatus("mandatory")
_SwhCountersRatesRxFrames128to255_Type = Counter32
_SwhCountersRatesRxFrames128to255_Object = MibTableColumn
swhCountersRatesRxFrames128to255 = _SwhCountersRatesRxFrames128to255_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 24),
    _SwhCountersRatesRxFrames128to255_Type()
)
swhCountersRatesRxFrames128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFrames128to255.setStatus("mandatory")
_SwhCountersRatesRxFrames256to511_Type = Counter32
_SwhCountersRatesRxFrames256to511_Object = MibTableColumn
swhCountersRatesRxFrames256to511 = _SwhCountersRatesRxFrames256to511_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 25),
    _SwhCountersRatesRxFrames256to511_Type()
)
swhCountersRatesRxFrames256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFrames256to511.setStatus("mandatory")
_SwhCountersRatesRxFrames512to1023_Type = Counter32
_SwhCountersRatesRxFrames512to1023_Object = MibTableColumn
swhCountersRatesRxFrames512to1023 = _SwhCountersRatesRxFrames512to1023_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 26),
    _SwhCountersRatesRxFrames512to1023_Type()
)
swhCountersRatesRxFrames512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFrames512to1023.setStatus("mandatory")
_SwhCountersRatesRxMulticastFrames_Type = Counter32
_SwhCountersRatesRxMulticastFrames_Object = MibTableColumn
swhCountersRatesRxMulticastFrames = _SwhCountersRatesRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 29),
    _SwhCountersRatesRxMulticastFrames_Type()
)
swhCountersRatesRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxMulticastFrames.setStatus("mandatory")
_SwhCountersRatesRxBroadcastFrames_Type = Counter32
_SwhCountersRatesRxBroadcastFrames_Object = MibTableColumn
swhCountersRatesRxBroadcastFrames = _SwhCountersRatesRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 30),
    _SwhCountersRatesRxBroadcastFrames_Type()
)
swhCountersRatesRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxBroadcastFrames.setStatus("mandatory")
_SwhCountersRatesTxMulticastFrames_Type = Counter32
_SwhCountersRatesTxMulticastFrames_Object = MibTableColumn
swhCountersRatesTxMulticastFrames = _SwhCountersRatesTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 32),
    _SwhCountersRatesTxMulticastFrames_Type()
)
swhCountersRatesTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesTxMulticastFrames.setStatus("mandatory")
_SwhCountersRatesTxBroadcastFrames_Type = Counter32
_SwhCountersRatesTxBroadcastFrames_Object = MibTableColumn
swhCountersRatesTxBroadcastFrames = _SwhCountersRatesTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 33),
    _SwhCountersRatesTxBroadcastFrames_Type()
)
swhCountersRatesTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesTxBroadcastFrames.setStatus("mandatory")
_SwhCountersRatesTxCollision_Type = Counter32
_SwhCountersRatesTxCollision_Object = MibTableColumn
swhCountersRatesTxCollision = _SwhCountersRatesTxCollision_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 38),
    _SwhCountersRatesTxCollision_Type()
)
swhCountersRatesTxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesTxCollision.setStatus("mandatory")
_SwhCountersRatesTotalErrors_Type = Counter32
_SwhCountersRatesTotalErrors_Object = MibTableColumn
swhCountersRatesTotalErrors = _SwhCountersRatesTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 39),
    _SwhCountersRatesTotalErrors_Type()
)
swhCountersRatesTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesTotalErrors.setStatus("mandatory")
_SwhCountersRatesRxFrames1024to1518_Type = Counter32
_SwhCountersRatesRxFrames1024to1518_Object = MibTableColumn
swhCountersRatesRxFrames1024to1518 = _SwhCountersRatesRxFrames1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 40),
    _SwhCountersRatesRxFrames1024to1518_Type()
)
swhCountersRatesRxFrames1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFrames1024to1518.setStatus("mandatory")
_SwhCountersRatesRxFrames1519toMaxSize_Type = Counter32
_SwhCountersRatesRxFrames1519toMaxSize_Object = MibTableColumn
swhCountersRatesRxFrames1519toMaxSize = _SwhCountersRatesRxFrames1519toMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 5, 1, 1, 41),
    _SwhCountersRatesRxFrames1519toMaxSize_Type()
)
swhCountersRatesRxFrames1519toMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersRatesRxFrames1519toMaxSize.setStatus("mandatory")
_SwhPortCountersEvents_ObjectIdentity = ObjectIdentity
swhPortCountersEvents = _SwhPortCountersEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6)
)
_SwhCountersEventsTable_Object = MibTable
swhCountersEventsTable = _SwhCountersEventsTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1)
)
if mibBuilder.loadTexts:
    swhCountersEventsTable.setStatus("mandatory")
_SwhCountersEventsEntry_Object = MibTableRow
swhCountersEventsEntry = _SwhCountersEventsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1)
)
swhCountersEventsEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhCountersEventsIndex"),
)
if mibBuilder.loadTexts:
    swhCountersEventsEntry.setStatus("mandatory")


class _SwhCountersEventsIndex_Type(Integer32):
    """Custom type swhCountersEventsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhCountersEventsIndex_Type.__name__ = "Integer32"
_SwhCountersEventsIndex_Object = MibTableColumn
swhCountersEventsIndex = _SwhCountersEventsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 1),
    _SwhCountersEventsIndex_Type()
)
swhCountersEventsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhCountersEventsIndex.setStatus("mandatory")
_SwhCountersEventsBytesReceived_Type = Counter64
_SwhCountersEventsBytesReceived_Object = MibTableColumn
swhCountersEventsBytesReceived = _SwhCountersEventsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 2),
    _SwhCountersEventsBytesReceived_Type()
)
swhCountersEventsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsBytesReceived.setStatus("mandatory")
_SwhCountersEventsFramesReceived_Type = Counter64
_SwhCountersEventsFramesReceived_Object = MibTableColumn
swhCountersEventsFramesReceived = _SwhCountersEventsFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 3),
    _SwhCountersEventsFramesReceived_Type()
)
swhCountersEventsFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsFramesReceived.setStatus("mandatory")
_SwhCountersEventsBytesSent_Type = Counter64
_SwhCountersEventsBytesSent_Object = MibTableColumn
swhCountersEventsBytesSent = _SwhCountersEventsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 5),
    _SwhCountersEventsBytesSent_Type()
)
swhCountersEventsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsBytesSent.setStatus("mandatory")
_SwhCountersEventsFramesSent_Type = Counter64
_SwhCountersEventsFramesSent_Object = MibTableColumn
swhCountersEventsFramesSent = _SwhCountersEventsFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 6),
    _SwhCountersEventsFramesSent_Type()
)
swhCountersEventsFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsFramesSent.setStatus("mandatory")
_SwhCountersEventsTotalBytes_Type = Counter64
_SwhCountersEventsTotalBytes_Object = MibTableColumn
swhCountersEventsTotalBytes = _SwhCountersEventsTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 8),
    _SwhCountersEventsTotalBytes_Type()
)
swhCountersEventsTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsTotalBytes.setStatus("mandatory")
_SwhCountersEventsRxCRCError_Type = Counter64
_SwhCountersEventsRxCRCError_Object = MibTableColumn
swhCountersEventsRxCRCError = _SwhCountersEventsRxCRCError_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 10),
    _SwhCountersEventsRxCRCError_Type()
)
swhCountersEventsRxCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxCRCError.setStatus("mandatory")
_SwhCountersEventsRxFragments_Type = Counter64
_SwhCountersEventsRxFragments_Object = MibTableColumn
swhCountersEventsRxFragments = _SwhCountersEventsRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 11),
    _SwhCountersEventsRxFragments_Type()
)
swhCountersEventsRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFragments.setStatus("mandatory")
_SwhCountersEventsRxFilteredFrames_Type = Counter64
_SwhCountersEventsRxFilteredFrames_Object = MibTableColumn
swhCountersEventsRxFilteredFrames = _SwhCountersEventsRxFilteredFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 12),
    _SwhCountersEventsRxFilteredFrames_Type()
)
swhCountersEventsRxFilteredFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFilteredFrames.setStatus("mandatory")
_SwhCountersEventsRxAlignError_Type = Counter64
_SwhCountersEventsRxAlignError_Object = MibTableColumn
swhCountersEventsRxAlignError = _SwhCountersEventsRxAlignError_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 13),
    _SwhCountersEventsRxAlignError_Type()
)
swhCountersEventsRxAlignError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxAlignError.setStatus("mandatory")
_SwhCountersEventsRxUndersizeFrames_Type = Counter64
_SwhCountersEventsRxUndersizeFrames_Object = MibTableColumn
swhCountersEventsRxUndersizeFrames = _SwhCountersEventsRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 14),
    _SwhCountersEventsRxUndersizeFrames_Type()
)
swhCountersEventsRxUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxUndersizeFrames.setStatus("mandatory")
_SwhCountersEventsRxOversizeFrames_Type = Counter64
_SwhCountersEventsRxOversizeFrames_Object = MibTableColumn
swhCountersEventsRxOversizeFrames = _SwhCountersEventsRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 15),
    _SwhCountersEventsRxOversizeFrames_Type()
)
swhCountersEventsRxOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxOversizeFrames.setStatus("mandatory")
_SwhCountersEventsRxJabbers_Type = Counter64
_SwhCountersEventsRxJabbers_Object = MibTableColumn
swhCountersEventsRxJabbers = _SwhCountersEventsRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 16),
    _SwhCountersEventsRxJabbers_Type()
)
swhCountersEventsRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxJabbers.setStatus("mandatory")
_SwhCountersEventsRxDroppedFrames_Type = Counter64
_SwhCountersEventsRxDroppedFrames_Object = MibTableColumn
swhCountersEventsRxDroppedFrames = _SwhCountersEventsRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 17),
    _SwhCountersEventsRxDroppedFrames_Type()
)
swhCountersEventsRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxDroppedFrames.setStatus("mandatory")
_SwhCountersEventsTxLateCollision_Type = Counter64
_SwhCountersEventsTxLateCollision_Object = MibTableColumn
swhCountersEventsTxLateCollision = _SwhCountersEventsTxLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 19),
    _SwhCountersEventsTxLateCollision_Type()
)
swhCountersEventsTxLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsTxLateCollision.setStatus("mandatory")
_SwhCountersEventsTxDeferred_Type = Counter64
_SwhCountersEventsTxDeferred_Object = MibTableColumn
swhCountersEventsTxDeferred = _SwhCountersEventsTxDeferred_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 20),
    _SwhCountersEventsTxDeferred_Type()
)
swhCountersEventsTxDeferred.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsTxDeferred.setStatus("mandatory")
_SwhCountersEventsRxFrames64_Type = Counter64
_SwhCountersEventsRxFrames64_Object = MibTableColumn
swhCountersEventsRxFrames64 = _SwhCountersEventsRxFrames64_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 22),
    _SwhCountersEventsRxFrames64_Type()
)
swhCountersEventsRxFrames64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFrames64.setStatus("mandatory")
_SwhCountersEventsRxFrames65to127_Type = Counter64
_SwhCountersEventsRxFrames65to127_Object = MibTableColumn
swhCountersEventsRxFrames65to127 = _SwhCountersEventsRxFrames65to127_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 23),
    _SwhCountersEventsRxFrames65to127_Type()
)
swhCountersEventsRxFrames65to127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFrames65to127.setStatus("mandatory")
_SwhCountersEventsRxFrames128to255_Type = Counter64
_SwhCountersEventsRxFrames128to255_Object = MibTableColumn
swhCountersEventsRxFrames128to255 = _SwhCountersEventsRxFrames128to255_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 24),
    _SwhCountersEventsRxFrames128to255_Type()
)
swhCountersEventsRxFrames128to255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFrames128to255.setStatus("mandatory")
_SwhCountersEventsRxFrames256to511_Type = Counter64
_SwhCountersEventsRxFrames256to511_Object = MibTableColumn
swhCountersEventsRxFrames256to511 = _SwhCountersEventsRxFrames256to511_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 25),
    _SwhCountersEventsRxFrames256to511_Type()
)
swhCountersEventsRxFrames256to511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFrames256to511.setStatus("mandatory")
_SwhCountersEventsRxFrames512to1023_Type = Counter64
_SwhCountersEventsRxFrames512to1023_Object = MibTableColumn
swhCountersEventsRxFrames512to1023 = _SwhCountersEventsRxFrames512to1023_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 26),
    _SwhCountersEventsRxFrames512to1023_Type()
)
swhCountersEventsRxFrames512to1023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFrames512to1023.setStatus("mandatory")
_SwhCountersEventsRxMulticastFrames_Type = Counter64
_SwhCountersEventsRxMulticastFrames_Object = MibTableColumn
swhCountersEventsRxMulticastFrames = _SwhCountersEventsRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 29),
    _SwhCountersEventsRxMulticastFrames_Type()
)
swhCountersEventsRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxMulticastFrames.setStatus("mandatory")
_SwhCountersEventsRxBroadcastFrames_Type = Counter64
_SwhCountersEventsRxBroadcastFrames_Object = MibTableColumn
swhCountersEventsRxBroadcastFrames = _SwhCountersEventsRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 30),
    _SwhCountersEventsRxBroadcastFrames_Type()
)
swhCountersEventsRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxBroadcastFrames.setStatus("mandatory")
_SwhCountersEventsTxMulticastFrames_Type = Counter64
_SwhCountersEventsTxMulticastFrames_Object = MibTableColumn
swhCountersEventsTxMulticastFrames = _SwhCountersEventsTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 32),
    _SwhCountersEventsTxMulticastFrames_Type()
)
swhCountersEventsTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsTxMulticastFrames.setStatus("mandatory")
_SwhCountersEventsTxBroadcastFrames_Type = Counter64
_SwhCountersEventsTxBroadcastFrames_Object = MibTableColumn
swhCountersEventsTxBroadcastFrames = _SwhCountersEventsTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 33),
    _SwhCountersEventsTxBroadcastFrames_Type()
)
swhCountersEventsTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsTxBroadcastFrames.setStatus("mandatory")
_SwhCountersEventsTxCollision_Type = Counter64
_SwhCountersEventsTxCollision_Object = MibTableColumn
swhCountersEventsTxCollision = _SwhCountersEventsTxCollision_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 39),
    _SwhCountersEventsTxCollision_Type()
)
swhCountersEventsTxCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsTxCollision.setStatus("mandatory")
_SwhCountersEventsRxFrames1024to1518_Type = Counter64
_SwhCountersEventsRxFrames1024to1518_Object = MibTableColumn
swhCountersEventsRxFrames1024to1518 = _SwhCountersEventsRxFrames1024to1518_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 40),
    _SwhCountersEventsRxFrames1024to1518_Type()
)
swhCountersEventsRxFrames1024to1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFrames1024to1518.setStatus("mandatory")
_SwhCountersEventsRxFrames1519toMaxSize_Type = Counter64
_SwhCountersEventsRxFrames1519toMaxSize_Object = MibTableColumn
swhCountersEventsRxFrames1519toMaxSize = _SwhCountersEventsRxFrames1519toMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 41),
    _SwhCountersEventsRxFrames1519toMaxSize_Type()
)
swhCountersEventsRxFrames1519toMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsRxFrames1519toMaxSize.setStatus("mandatory")
_SwhCountersEventsTotalErrors_Type = Counter64
_SwhCountersEventsTotalErrors_Object = MibTableColumn
swhCountersEventsTotalErrors = _SwhCountersEventsTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 1, 1, 42),
    _SwhCountersEventsTotalErrors_Type()
)
swhCountersEventsTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCountersEventsTotalErrors.setStatus("mandatory")


class _SwhCountersEventsClearCountersOfAllPort_Type(Integer32):
    """Custom type swhCountersEventsClearCountersOfAllPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhCountersEventsClearCountersOfAllPort_Type.__name__ = "Integer32"
_SwhCountersEventsClearCountersOfAllPort_Object = MibScalar
swhCountersEventsClearCountersOfAllPort = _SwhCountersEventsClearCountersOfAllPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 6, 2),
    _SwhCountersEventsClearCountersOfAllPort_Type()
)
swhCountersEventsClearCountersOfAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhCountersEventsClearCountersOfAllPort.setStatus("mandatory")
_SwhMacAddressTable_ObjectIdentity = ObjectIdentity
swhMacAddressTable = _SwhMacAddressTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7)
)


class _SwhMacAddressPortSelect_Type(Integer32):
    """Custom type swhMacAddressPortSelect based on Integer32"""
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
        *(("all", 0),
          ("port01", 1),
          ("port02", 2),
          ("port03", 3),
          ("port04", 4),
          ("port05", 5),
          ("port06", 6),
          ("cpu", 7))
    )


_SwhMacAddressPortSelect_Type.__name__ = "Integer32"
_SwhMacAddressPortSelect_Object = MibScalar
swhMacAddressPortSelect = _SwhMacAddressPortSelect_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 1),
    _SwhMacAddressPortSelect_Type()
)
swhMacAddressPortSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacAddressPortSelect.setStatus("mandatory")


class _SwhMacAddressClear_Type(Integer32):
    """Custom type swhMacAddressClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhMacAddressClear_Type.__name__ = "Integer32"
_SwhMacAddressClear_Object = MibScalar
swhMacAddressClear = _SwhMacAddressClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 2),
    _SwhMacAddressClear_Type()
)
swhMacAddressClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacAddressClear.setStatus("mandatory")


class _SwhMacAddressUpdate_Type(Integer32):
    """Custom type swhMacAddressUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("update", 1))
    )


_SwhMacAddressUpdate_Type.__name__ = "Integer32"
_SwhMacAddressUpdate_Object = MibScalar
swhMacAddressUpdate = _SwhMacAddressUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 3),
    _SwhMacAddressUpdate_Type()
)
swhMacAddressUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacAddressUpdate.setStatus("mandatory")


class _SwhMacAddressTotal_Type(Integer32):
    """Custom type swhMacAddressTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressTotal_Type.__name__ = "Integer32"
_SwhMacAddressTotal_Object = MibScalar
swhMacAddressTotal = _SwhMacAddressTotal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 4),
    _SwhMacAddressTotal_Type()
)
swhMacAddressTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacAddressTotal.setStatus("mandatory")
_SwhMacAddressState_Type = DisplayString
_SwhMacAddressState_Object = MibScalar
swhMacAddressState = _SwhMacAddressState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 5),
    _SwhMacAddressState_Type()
)
swhMacAddressState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacAddressState.setStatus("mandatory")
_SwhMacTable_Object = MibTable
swhMacTable = _SwhMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 6)
)
if mibBuilder.loadTexts:
    swhMacTable.setStatus("mandatory")
_SwhMacTableEntry_Object = MibTableRow
swhMacTableEntry = _SwhMacTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 6, 1)
)
swhMacTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhMacTableIndex"),
)
if mibBuilder.loadTexts:
    swhMacTableEntry.setStatus("mandatory")


class _SwhMacTableIndex_Type(Integer32):
    """Custom type swhMacTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacTableIndex_Type.__name__ = "Integer32"
_SwhMacTableIndex_Object = MibTableColumn
swhMacTableIndex = _SwhMacTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 6, 1, 1),
    _SwhMacTableIndex_Type()
)
swhMacTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhMacTableIndex.setStatus("mandatory")
_SwhMacTableAddr_Type = MacAddress
_SwhMacTableAddr_Object = MibTableColumn
swhMacTableAddr = _SwhMacTableAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 6, 1, 2),
    _SwhMacTableAddr_Type()
)
swhMacTableAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacTableAddr.setStatus("mandatory")
_SwhMacTableVID_Type = Integer32
_SwhMacTableVID_Object = MibTableColumn
swhMacTableVID = _SwhMacTableVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 6, 1, 3),
    _SwhMacTableVID_Type()
)
swhMacTableVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacTableVID.setStatus("mandatory")
_SwhMacTablePort_Type = DisplayString
_SwhMacTablePort_Object = MibTableColumn
swhMacTablePort = _SwhMacTablePort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 6, 1, 4),
    _SwhMacTablePort_Type()
)
swhMacTablePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacTablePort.setStatus("mandatory")
_SwhMacTableType_Type = DisplayString
_SwhMacTableType_Object = MibTableColumn
swhMacTableType = _SwhMacTableType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 6, 1, 5),
    _SwhMacTableType_Type()
)
swhMacTableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacTableType.setStatus("mandatory")


class _SwhMacAddressPageSelect_Type(Integer32):
    """Custom type swhMacAddressPageSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressPageSelect_Type.__name__ = "Integer32"
_SwhMacAddressPageSelect_Object = MibScalar
swhMacAddressPageSelect = _SwhMacAddressPageSelect_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 9),
    _SwhMacAddressPageSelect_Type()
)
swhMacAddressPageSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacAddressPageSelect.setStatus("mandatory")


class _SwhMacAddressVLANSelect_Type(Integer32):
    """Custom type swhMacAddressVLANSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressVLANSelect_Type.__name__ = "Integer32"
_SwhMacAddressVLANSelect_Object = MibScalar
swhMacAddressVLANSelect = _SwhMacAddressVLANSelect_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 10),
    _SwhMacAddressVLANSelect_Type()
)
swhMacAddressVLANSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacAddressVLANSelect.setStatus("mandatory")
_SwhMacAddressMACSelect_Type = DisplayString
_SwhMacAddressMACSelect_Object = MibScalar
swhMacAddressMACSelect = _SwhMacAddressMACSelect_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 11),
    _SwhMacAddressMACSelect_Type()
)
swhMacAddressMACSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhMacAddressMACSelect.setStatus("mandatory")


class _SwhMacAddressCapacity_Type(Integer32):
    """Custom type swhMacAddressCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressCapacity_Type.__name__ = "Integer32"
_SwhMacAddressCapacity_Object = MibScalar
swhMacAddressCapacity = _SwhMacAddressCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 20),
    _SwhMacAddressCapacity_Type()
)
swhMacAddressCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacAddressCapacity.setStatus("mandatory")


class _SwhMacAddressFree_Type(Integer32):
    """Custom type swhMacAddressFree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressFree_Type.__name__ = "Integer32"
_SwhMacAddressFree_Object = MibScalar
swhMacAddressFree = _SwhMacAddressFree_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 21),
    _SwhMacAddressFree_Type()
)
swhMacAddressFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacAddressFree.setStatus("mandatory")


class _SwhMacAddressUsed_Type(Integer32):
    """Custom type swhMacAddressUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressUsed_Type.__name__ = "Integer32"
_SwhMacAddressUsed_Object = MibScalar
swhMacAddressUsed = _SwhMacAddressUsed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 22),
    _SwhMacAddressUsed_Type()
)
swhMacAddressUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacAddressUsed.setStatus("mandatory")


class _SwhMacAddressDynamic_Type(Integer32):
    """Custom type swhMacAddressDynamic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressDynamic_Type.__name__ = "Integer32"
_SwhMacAddressDynamic_Object = MibScalar
swhMacAddressDynamic = _SwhMacAddressDynamic_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 24),
    _SwhMacAddressDynamic_Type()
)
swhMacAddressDynamic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacAddressDynamic.setStatus("mandatory")


class _SwhMacAddressStatic_Type(Integer32):
    """Custom type swhMacAddressStatic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressStatic_Type.__name__ = "Integer32"
_SwhMacAddressStatic_Object = MibScalar
swhMacAddressStatic = _SwhMacAddressStatic_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 25),
    _SwhMacAddressStatic_Type()
)
swhMacAddressStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacAddressStatic.setStatus("mandatory")


class _SwhMacAddressInternal_Type(Integer32):
    """Custom type swhMacAddressInternal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacAddressInternal_Type.__name__ = "Integer32"
_SwhMacAddressInternal_Object = MibScalar
swhMacAddressInternal = _SwhMacAddressInternal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 7, 26),
    _SwhMacAddressInternal_Type()
)
swhMacAddressInternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacAddressInternal.setStatus("mandatory")
_SwhRSTPBridgeOverview_ObjectIdentity = ObjectIdentity
swhRSTPBridgeOverview = _SwhRSTPBridgeOverview_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10)
)
_SwhRSTPBridgeTable_Object = MibTable
swhRSTPBridgeTable = _SwhRSTPBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7)
)
if mibBuilder.loadTexts:
    swhRSTPBridgeTable.setStatus("mandatory")
_SwhRSTPBridgeEntry_Object = MibTableRow
swhRSTPBridgeEntry = _SwhRSTPBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1)
)
swhRSTPBridgeEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhRSTPBridgeIndex"),
)
if mibBuilder.loadTexts:
    swhRSTPBridgeEntry.setStatus("mandatory")


class _SwhRSTPBridgeIndex_Type(Integer32):
    """Custom type swhRSTPBridgeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRSTPBridgeIndex_Type.__name__ = "Integer32"
_SwhRSTPBridgeIndex_Object = MibTableColumn
swhRSTPBridgeIndex = _SwhRSTPBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1, 1),
    _SwhRSTPBridgeIndex_Type()
)
swhRSTPBridgeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhRSTPBridgeIndex.setStatus("mandatory")
_SwhRSTPBridgeBridgeID_Type = DisplayString
_SwhRSTPBridgeBridgeID_Object = MibTableColumn
swhRSTPBridgeBridgeID = _SwhRSTPBridgeBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1, 3),
    _SwhRSTPBridgeBridgeID_Type()
)
swhRSTPBridgeBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPBridgeBridgeID.setStatus("mandatory")
_SwhRSTPBridgeMaxAge_Type = Integer32
_SwhRSTPBridgeMaxAge_Object = MibTableColumn
swhRSTPBridgeMaxAge = _SwhRSTPBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1, 4),
    _SwhRSTPBridgeMaxAge_Type()
)
swhRSTPBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPBridgeMaxAge.setStatus("mandatory")
_SwhRSTPBridgeHelloTime_Type = Integer32
_SwhRSTPBridgeHelloTime_Object = MibTableColumn
swhRSTPBridgeHelloTime = _SwhRSTPBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1, 5),
    _SwhRSTPBridgeHelloTime_Type()
)
swhRSTPBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPBridgeHelloTime.setStatus("mandatory")
_SwhRSTPBridgeFwdDelay_Type = Integer32
_SwhRSTPBridgeFwdDelay_Object = MibTableColumn
swhRSTPBridgeFwdDelay = _SwhRSTPBridgeFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1, 6),
    _SwhRSTPBridgeFwdDelay_Type()
)
swhRSTPBridgeFwdDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPBridgeFwdDelay.setStatus("mandatory")


class _SwhRSTPBridgeTopology_Type(Integer32):
    """Custom type swhRSTPBridgeTopology based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("steady", 0),
          ("changing", 1))
    )


_SwhRSTPBridgeTopology_Type.__name__ = "Integer32"
_SwhRSTPBridgeTopology_Object = MibTableColumn
swhRSTPBridgeTopology = _SwhRSTPBridgeTopology_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1, 7),
    _SwhRSTPBridgeTopology_Type()
)
swhRSTPBridgeTopology.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPBridgeTopology.setStatus("mandatory")
_SwhRSTPBridgeRootID_Type = DisplayString
_SwhRSTPBridgeRootID_Object = MibTableColumn
swhRSTPBridgeRootID = _SwhRSTPBridgeRootID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1, 10),
    _SwhRSTPBridgeRootID_Type()
)
swhRSTPBridgeRootID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPBridgeRootID.setStatus("mandatory")
_SwhRSTPBridgeRootPort_Type = DisplayString
_SwhRSTPBridgeRootPort_Object = MibTableColumn
swhRSTPBridgeRootPort = _SwhRSTPBridgeRootPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 10, 7, 1, 13),
    _SwhRSTPBridgeRootPort_Type()
)
swhRSTPBridgeRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPBridgeRootPort.setStatus("mandatory")
_SwhLLDPStatus_ObjectIdentity = ObjectIdentity
swhLLDPStatus = _SwhLLDPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11)
)
_SwhLLDPStatusTable_Object = MibTable
swhLLDPStatusTable = _SwhLLDPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4)
)
if mibBuilder.loadTexts:
    swhLLDPStatusTable.setStatus("mandatory")
_SwhLLDPStatusTableEntry_Object = MibTableRow
swhLLDPStatusTableEntry = _SwhLLDPStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1)
)
swhLLDPStatusTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhLLDPStatusTableIndex"),
)
if mibBuilder.loadTexts:
    swhLLDPStatusTableEntry.setStatus("mandatory")


class _SwhLLDPStatusTableIndex_Type(Integer32):
    """Custom type swhLLDPStatusTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhLLDPStatusTableIndex_Type.__name__ = "Integer32"
_SwhLLDPStatusTableIndex_Object = MibTableColumn
swhLLDPStatusTableIndex = _SwhLLDPStatusTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 1),
    _SwhLLDPStatusTableIndex_Type()
)
swhLLDPStatusTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhLLDPStatusTableIndex.setStatus("mandatory")
_SwhLLDPStatusTableChassisID_Type = DisplayString
_SwhLLDPStatusTableChassisID_Object = MibTableColumn
swhLLDPStatusTableChassisID = _SwhLLDPStatusTableChassisID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 3),
    _SwhLLDPStatusTableChassisID_Type()
)
swhLLDPStatusTableChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableChassisID.setStatus("mandatory")
_SwhLLDPStatusTableRemotePort_Type = DisplayString
_SwhLLDPStatusTableRemotePort_Object = MibTableColumn
swhLLDPStatusTableRemotePort = _SwhLLDPStatusTableRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 4),
    _SwhLLDPStatusTableRemotePort_Type()
)
swhLLDPStatusTableRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableRemotePort.setStatus("mandatory")
_SwhLLDPStatusTableSystemName_Type = DisplayString
_SwhLLDPStatusTableSystemName_Object = MibTableColumn
swhLLDPStatusTableSystemName = _SwhLLDPStatusTableSystemName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 5),
    _SwhLLDPStatusTableSystemName_Type()
)
swhLLDPStatusTableSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableSystemName.setStatus("mandatory")
_SwhLLDPStatusTablePortDescription_Type = DisplayString
_SwhLLDPStatusTablePortDescription_Object = MibTableColumn
swhLLDPStatusTablePortDescription = _SwhLLDPStatusTablePortDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 6),
    _SwhLLDPStatusTablePortDescription_Type()
)
swhLLDPStatusTablePortDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTablePortDescription.setStatus("mandatory")
_SwhLLDPStatusTableSystemCapabilities_Type = DisplayString
_SwhLLDPStatusTableSystemCapabilities_Object = MibTableColumn
swhLLDPStatusTableSystemCapabilities = _SwhLLDPStatusTableSystemCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 7),
    _SwhLLDPStatusTableSystemCapabilities_Type()
)
swhLLDPStatusTableSystemCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableSystemCapabilities.setStatus("mandatory")
_SwhLLDPStatusTableManagement1Address_Type = DisplayString
_SwhLLDPStatusTableManagement1Address_Object = MibTableColumn
swhLLDPStatusTableManagement1Address = _SwhLLDPStatusTableManagement1Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 8),
    _SwhLLDPStatusTableManagement1Address_Type()
)
swhLLDPStatusTableManagement1Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableManagement1Address.setStatus("mandatory")
_SwhLLDPStatusTableManagement2Address_Type = DisplayString
_SwhLLDPStatusTableManagement2Address_Object = MibTableColumn
swhLLDPStatusTableManagement2Address = _SwhLLDPStatusTableManagement2Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 9),
    _SwhLLDPStatusTableManagement2Address_Type()
)
swhLLDPStatusTableManagement2Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableManagement2Address.setStatus("mandatory")
_SwhLLDPStatusTableManagement3Address_Type = DisplayString
_SwhLLDPStatusTableManagement3Address_Object = MibTableColumn
swhLLDPStatusTableManagement3Address = _SwhLLDPStatusTableManagement3Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 10),
    _SwhLLDPStatusTableManagement3Address_Type()
)
swhLLDPStatusTableManagement3Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableManagement3Address.setStatus("mandatory")
_SwhLLDPStatusTableManagement4Address_Type = DisplayString
_SwhLLDPStatusTableManagement4Address_Object = MibTableColumn
swhLLDPStatusTableManagement4Address = _SwhLLDPStatusTableManagement4Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 11),
    _SwhLLDPStatusTableManagement4Address_Type()
)
swhLLDPStatusTableManagement4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableManagement4Address.setStatus("mandatory")
_SwhLLDPStatusTableManagement5Address_Type = DisplayString
_SwhLLDPStatusTableManagement5Address_Object = MibTableColumn
swhLLDPStatusTableManagement5Address = _SwhLLDPStatusTableManagement5Address_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 11, 4, 1, 12),
    _SwhLLDPStatusTableManagement5Address_Type()
)
swhLLDPStatusTableManagement5Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLLDPStatusTableManagement5Address.setStatus("mandatory")
_SwhRSTPPortStatus_ObjectIdentity = ObjectIdentity
swhRSTPPortStatus = _SwhRSTPPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14)
)
_SwhRSTPPortStatusTable_Object = MibTable
swhRSTPPortStatusTable = _SwhRSTPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1)
)
if mibBuilder.loadTexts:
    swhRSTPPortStatusTable.setStatus("mandatory")
_SwhRSTPPortStatusEntry_Object = MibTableRow
swhRSTPPortStatusEntry = _SwhRSTPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1)
)
swhRSTPPortStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhRSTPPortStatusIndex"),
)
if mibBuilder.loadTexts:
    swhRSTPPortStatusEntry.setStatus("mandatory")


class _SwhRSTPPortStatusIndex_Type(Integer32):
    """Custom type swhRSTPPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRSTPPortStatusIndex_Type.__name__ = "Integer32"
_SwhRSTPPortStatusIndex_Object = MibTableColumn
swhRSTPPortStatusIndex = _SwhRSTPPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1, 1),
    _SwhRSTPPortStatusIndex_Type()
)
swhRSTPPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhRSTPPortStatusIndex.setStatus("mandatory")
_SwhRSTPPortStatusPathCost_Type = Integer32
_SwhRSTPPortStatusPathCost_Object = MibTableColumn
swhRSTPPortStatusPathCost = _SwhRSTPPortStatusPathCost_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1, 3),
    _SwhRSTPPortStatusPathCost_Type()
)
swhRSTPPortStatusPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPPortStatusPathCost.setStatus("mandatory")


class _SwhRSTPPortStatusEdgePort_Type(Integer32):
    """Custom type swhRSTPPortStatusEdgePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SwhRSTPPortStatusEdgePort_Type.__name__ = "Integer32"
_SwhRSTPPortStatusEdgePort_Object = MibTableColumn
swhRSTPPortStatusEdgePort = _SwhRSTPPortStatusEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1, 4),
    _SwhRSTPPortStatusEdgePort_Type()
)
swhRSTPPortStatusEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPPortStatusEdgePort.setStatus("mandatory")


class _SwhRSTPPortStatusP2pPort_Type(Integer32):
    """Custom type swhRSTPPortStatusP2pPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SwhRSTPPortStatusP2pPort_Type.__name__ = "Integer32"
_SwhRSTPPortStatusP2pPort_Object = MibTableColumn
swhRSTPPortStatusP2pPort = _SwhRSTPPortStatusP2pPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1, 5),
    _SwhRSTPPortStatusP2pPort_Type()
)
swhRSTPPortStatusP2pPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPPortStatusP2pPort.setStatus("mandatory")


class _SwhRSTPPortStatusProtocol_Type(Integer32):
    """Custom type swhRSTPPortStatusProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rstp", 0),
          ("stp", 1))
    )


_SwhRSTPPortStatusProtocol_Type.__name__ = "Integer32"
_SwhRSTPPortStatusProtocol_Object = MibTableColumn
swhRSTPPortStatusProtocol = _SwhRSTPPortStatusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1, 6),
    _SwhRSTPPortStatusProtocol_Type()
)
swhRSTPPortStatusProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPPortStatusProtocol.setStatus("mandatory")


class _SwhRSTPPortStatusRole_Type(Integer32):
    """Custom type swhRSTPPortStatusRole based on Integer32"""
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
        *(("disable", 0),
          ("alternate", 1),
          ("backup", 2),
          ("root", 3),
          ("designated", 4),
          ("non-stp", 5))
    )


_SwhRSTPPortStatusRole_Type.__name__ = "Integer32"
_SwhRSTPPortStatusRole_Object = MibTableColumn
swhRSTPPortStatusRole = _SwhRSTPPortStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1, 7),
    _SwhRSTPPortStatusRole_Type()
)
swhRSTPPortStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPPortStatusRole.setStatus("mandatory")


class _SwhRSTPPortStatusPortState_Type(Integer32):
    """Custom type swhRSTPPortStatusPortState based on Integer32"""
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
        *(("disable", 0),
          ("blocking", 1),
          ("listening", 2),
          ("learning", 3),
          ("forwarding", 4),
          ("non-stp", 5))
    )


_SwhRSTPPortStatusPortState_Type.__name__ = "Integer32"
_SwhRSTPPortStatusPortState_Object = MibTableColumn
swhRSTPPortStatusPortState = _SwhRSTPPortStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1, 8),
    _SwhRSTPPortStatusPortState_Type()
)
swhRSTPPortStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPPortStatusPortState.setStatus("mandatory")
_SwhRSTPPortStatusPort_Type = DisplayString
_SwhRSTPPortStatusPort_Object = MibTableColumn
swhRSTPPortStatusPort = _SwhRSTPPortStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 14, 1, 1, 9),
    _SwhRSTPPortStatusPort_Type()
)
swhRSTPPortStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPPortStatusPort.setStatus("mandatory")
_SwhRSTPStatistics_ObjectIdentity = ObjectIdentity
swhRSTPStatistics = _SwhRSTPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18)
)
_SwhRSTPStatisticsTable_Object = MibTable
swhRSTPStatisticsTable = _SwhRSTPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1)
)
if mibBuilder.loadTexts:
    swhRSTPStatisticsTable.setStatus("mandatory")
_SwhRSTPStatisticsEntry_Object = MibTableRow
swhRSTPStatisticsEntry = _SwhRSTPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1)
)
swhRSTPStatisticsEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhRSTPStatisticsIndex"),
)
if mibBuilder.loadTexts:
    swhRSTPStatisticsEntry.setStatus("mandatory")


class _SwhRSTPStatisticsIndex_Type(Integer32):
    """Custom type swhRSTPStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRSTPStatisticsIndex_Type.__name__ = "Integer32"
_SwhRSTPStatisticsIndex_Object = MibTableColumn
swhRSTPStatisticsIndex = _SwhRSTPStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 1),
    _SwhRSTPStatisticsIndex_Type()
)
swhRSTPStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhRSTPStatisticsIndex.setStatus("mandatory")
_SwhRSTPStatisticsRSTPTransmitted_Type = Counter32
_SwhRSTPStatisticsRSTPTransmitted_Object = MibTableColumn
swhRSTPStatisticsRSTPTransmitted = _SwhRSTPStatisticsRSTPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 3),
    _SwhRSTPStatisticsRSTPTransmitted_Type()
)
swhRSTPStatisticsRSTPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsRSTPTransmitted.setStatus("mandatory")
_SwhRSTPStatisticsSTPTransmitted_Type = Counter32
_SwhRSTPStatisticsSTPTransmitted_Object = MibTableColumn
swhRSTPStatisticsSTPTransmitted = _SwhRSTPStatisticsSTPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 5),
    _SwhRSTPStatisticsSTPTransmitted_Type()
)
swhRSTPStatisticsSTPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsSTPTransmitted.setStatus("mandatory")
_SwhRSTPStatisticsTCNTransmitted_Type = Counter32
_SwhRSTPStatisticsTCNTransmitted_Object = MibTableColumn
swhRSTPStatisticsTCNTransmitted = _SwhRSTPStatisticsTCNTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 7),
    _SwhRSTPStatisticsTCNTransmitted_Type()
)
swhRSTPStatisticsTCNTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsTCNTransmitted.setStatus("mandatory")
_SwhRSTPStatisticsRSTPReceived_Type = Counter32
_SwhRSTPStatisticsRSTPReceived_Object = MibTableColumn
swhRSTPStatisticsRSTPReceived = _SwhRSTPStatisticsRSTPReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 9),
    _SwhRSTPStatisticsRSTPReceived_Type()
)
swhRSTPStatisticsRSTPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsRSTPReceived.setStatus("mandatory")
_SwhRSTPStatisticsSTPReceived_Type = Counter32
_SwhRSTPStatisticsSTPReceived_Object = MibTableColumn
swhRSTPStatisticsSTPReceived = _SwhRSTPStatisticsSTPReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 11),
    _SwhRSTPStatisticsSTPReceived_Type()
)
swhRSTPStatisticsSTPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsSTPReceived.setStatus("mandatory")
_SwhRSTPStatisticsTCNReceived_Type = Counter32
_SwhRSTPStatisticsTCNReceived_Object = MibTableColumn
swhRSTPStatisticsTCNReceived = _SwhRSTPStatisticsTCNReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 13),
    _SwhRSTPStatisticsTCNReceived_Type()
)
swhRSTPStatisticsTCNReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsTCNReceived.setStatus("mandatory")
_SwhRSTPStatisticsIllegalReceived_Type = Counter32
_SwhRSTPStatisticsIllegalReceived_Object = MibTableColumn
swhRSTPStatisticsIllegalReceived = _SwhRSTPStatisticsIllegalReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 15),
    _SwhRSTPStatisticsIllegalReceived_Type()
)
swhRSTPStatisticsIllegalReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsIllegalReceived.setStatus("mandatory")
_SwhRSTPStatisticsUnknownReceived_Type = Counter32
_SwhRSTPStatisticsUnknownReceived_Object = MibTableColumn
swhRSTPStatisticsUnknownReceived = _SwhRSTPStatisticsUnknownReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 17),
    _SwhRSTPStatisticsUnknownReceived_Type()
)
swhRSTPStatisticsUnknownReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsUnknownReceived.setStatus("mandatory")
_SwhRSTPStatisticsPort_Type = DisplayString
_SwhRSTPStatisticsPort_Object = MibTableColumn
swhRSTPStatisticsPort = _SwhRSTPStatisticsPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 18, 1, 1, 18),
    _SwhRSTPStatisticsPort_Type()
)
swhRSTPStatisticsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRSTPStatisticsPort.setStatus("mandatory")
_SwhLACPPortStatus_ObjectIdentity = ObjectIdentity
swhLACPPortStatus = _SwhLACPPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22)
)
_SwhLACPPortStatusTable_Object = MibTable
swhLACPPortStatusTable = _SwhLACPPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22, 1)
)
if mibBuilder.loadTexts:
    swhLACPPortStatusTable.setStatus("mandatory")
_SwhLACPPortStatusEntry_Object = MibTableRow
swhLACPPortStatusEntry = _SwhLACPPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22, 1, 1)
)
swhLACPPortStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhLACPPortStatusIndex"),
)
if mibBuilder.loadTexts:
    swhLACPPortStatusEntry.setStatus("mandatory")


class _SwhLACPPortStatusIndex_Type(Integer32):
    """Custom type swhLACPPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhLACPPortStatusIndex_Type.__name__ = "Integer32"
_SwhLACPPortStatusIndex_Object = MibTableColumn
swhLACPPortStatusIndex = _SwhLACPPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22, 1, 1, 1),
    _SwhLACPPortStatusIndex_Type()
)
swhLACPPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhLACPPortStatusIndex.setStatus("mandatory")
_SwhLACPPortStatusPartnerPort_Type = Integer32
_SwhLACPPortStatusPartnerPort_Object = MibTableColumn
swhLACPPortStatusPartnerPort = _SwhLACPPortStatusPartnerPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22, 1, 1, 3),
    _SwhLACPPortStatusPartnerPort_Type()
)
swhLACPPortStatusPartnerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPPortStatusPartnerPort.setStatus("mandatory")


class _SwhLACPPortStatusLACPOperationalState_Type(Integer32):
    """Custom type swhLACPPortStatusLACPOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SwhLACPPortStatusLACPOperationalState_Type.__name__ = "Integer32"
_SwhLACPPortStatusLACPOperationalState_Object = MibTableColumn
swhLACPPortStatusLACPOperationalState = _SwhLACPPortStatusLACPOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22, 1, 1, 4),
    _SwhLACPPortStatusLACPOperationalState_Type()
)
swhLACPPortStatusLACPOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPPortStatusLACPOperationalState.setStatus("mandatory")
_SwhLACPPortStatusKey_Type = Integer32
_SwhLACPPortStatusKey_Object = MibTableColumn
swhLACPPortStatusKey = _SwhLACPPortStatusKey_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22, 1, 1, 5),
    _SwhLACPPortStatusKey_Type()
)
swhLACPPortStatusKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPPortStatusKey.setStatus("mandatory")
_SwhLACPPortStatusAggrID_Type = Integer32
_SwhLACPPortStatusAggrID_Object = MibTableColumn
swhLACPPortStatusAggrID = _SwhLACPPortStatusAggrID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22, 1, 1, 6),
    _SwhLACPPortStatusAggrID_Type()
)
swhLACPPortStatusAggrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPPortStatusAggrID.setStatus("mandatory")
_SwhLACPPortStatusPartnerID_Type = DisplayString
_SwhLACPPortStatusPartnerID_Object = MibTableColumn
swhLACPPortStatusPartnerID = _SwhLACPPortStatusPartnerID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 22, 1, 1, 7),
    _SwhLACPPortStatusPartnerID_Type()
)
swhLACPPortStatusPartnerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPPortStatusPartnerID.setStatus("mandatory")
_SwhLACPStatistics_ObjectIdentity = ObjectIdentity
swhLACPStatistics = _SwhLACPStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24)
)
_SwhLACPStatisticsTable_Object = MibTable
swhLACPStatisticsTable = _SwhLACPStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 1)
)
if mibBuilder.loadTexts:
    swhLACPStatisticsTable.setStatus("mandatory")
_SwhLACPStatisticsEntry_Object = MibTableRow
swhLACPStatisticsEntry = _SwhLACPStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 1, 1)
)
swhLACPStatisticsEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhLACPStatisticsIndex"),
)
if mibBuilder.loadTexts:
    swhLACPStatisticsEntry.setStatus("mandatory")


class _SwhLACPStatisticsIndex_Type(Integer32):
    """Custom type swhLACPStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhLACPStatisticsIndex_Type.__name__ = "Integer32"
_SwhLACPStatisticsIndex_Object = MibTableColumn
swhLACPStatisticsIndex = _SwhLACPStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 1, 1, 1),
    _SwhLACPStatisticsIndex_Type()
)
swhLACPStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhLACPStatisticsIndex.setStatus("mandatory")
_SwhLACPStatisticsLACPTransmitted_Type = Counter32
_SwhLACPStatisticsLACPTransmitted_Object = MibTableColumn
swhLACPStatisticsLACPTransmitted = _SwhLACPStatisticsLACPTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 1, 1, 3),
    _SwhLACPStatisticsLACPTransmitted_Type()
)
swhLACPStatisticsLACPTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPStatisticsLACPTransmitted.setStatus("mandatory")
_SwhLACPStatisticsLACPReceived_Type = Counter32
_SwhLACPStatisticsLACPReceived_Object = MibTableColumn
swhLACPStatisticsLACPReceived = _SwhLACPStatisticsLACPReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 1, 1, 9),
    _SwhLACPStatisticsLACPReceived_Type()
)
swhLACPStatisticsLACPReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPStatisticsLACPReceived.setStatus("mandatory")
_SwhLACPStatisticsIllegalReceived_Type = Counter32
_SwhLACPStatisticsIllegalReceived_Object = MibTableColumn
swhLACPStatisticsIllegalReceived = _SwhLACPStatisticsIllegalReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 1, 1, 15),
    _SwhLACPStatisticsIllegalReceived_Type()
)
swhLACPStatisticsIllegalReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPStatisticsIllegalReceived.setStatus("mandatory")
_SwhLACPStatisticsUnknownReceived_Type = Counter32
_SwhLACPStatisticsUnknownReceived_Object = MibTableColumn
swhLACPStatisticsUnknownReceived = _SwhLACPStatisticsUnknownReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 1, 1, 17),
    _SwhLACPStatisticsUnknownReceived_Type()
)
swhLACPStatisticsUnknownReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLACPStatisticsUnknownReceived.setStatus("mandatory")


class _SwhLACPStatisticsClear_Type(Integer32):
    """Custom type swhLACPStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhLACPStatisticsClear_Type.__name__ = "Integer32"
_SwhLACPStatisticsClear_Object = MibTableColumn
swhLACPStatisticsClear = _SwhLACPStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 1, 1, 19),
    _SwhLACPStatisticsClear_Type()
)
swhLACPStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLACPStatisticsClear.setStatus("mandatory")


class _SwhLACPStatisticsClearCountersOfAllPort_Type(Integer32):
    """Custom type swhLACPStatisticsClearCountersOfAllPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhLACPStatisticsClearCountersOfAllPort_Type.__name__ = "Integer32"
_SwhLACPStatisticsClearCountersOfAllPort_Object = MibScalar
swhLACPStatisticsClearCountersOfAllPort = _SwhLACPStatisticsClearCountersOfAllPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 24, 2),
    _SwhLACPStatisticsClearCountersOfAllPort_Type()
)
swhLACPStatisticsClearCountersOfAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLACPStatisticsClearCountersOfAllPort.setStatus("mandatory")
_SwhLayer2ProtocolTunnelStatus_ObjectIdentity = ObjectIdentity
swhLayer2ProtocolTunnelStatus = _SwhLayer2ProtocolTunnelStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25)
)


class _SwhL2PTStatusClearCountersOfAllPort_Type(Integer32):
    """Custom type swhL2PTStatusClearCountersOfAllPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhL2PTStatusClearCountersOfAllPort_Type.__name__ = "Integer32"
_SwhL2PTStatusClearCountersOfAllPort_Object = MibScalar
swhL2PTStatusClearCountersOfAllPort = _SwhL2PTStatusClearCountersOfAllPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 2),
    _SwhL2PTStatusClearCountersOfAllPort_Type()
)
swhL2PTStatusClearCountersOfAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTStatusClearCountersOfAllPort.setStatus("mandatory")


class _SwhL2PTStatusPortSelect_Type(Integer32):
    """Custom type swhL2PTStatusPortSelect based on Integer32"""
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
        *(("port01", 0),
          ("port02", 1),
          ("port03", 2),
          ("port04", 3),
          ("port05", 4),
          ("port06", 5))
    )


_SwhL2PTStatusPortSelect_Type.__name__ = "Integer32"
_SwhL2PTStatusPortSelect_Object = MibScalar
swhL2PTStatusPortSelect = _SwhL2PTStatusPortSelect_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 3),
    _SwhL2PTStatusPortSelect_Type()
)
swhL2PTStatusPortSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTStatusPortSelect.setStatus("mandatory")


class _SwhL2PTStatusPortClear_Type(Integer32):
    """Custom type swhL2PTStatusPortClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhL2PTStatusPortClear_Type.__name__ = "Integer32"
_SwhL2PTStatusPortClear_Object = MibScalar
swhL2PTStatusPortClear = _SwhL2PTStatusPortClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 4),
    _SwhL2PTStatusPortClear_Type()
)
swhL2PTStatusPortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhL2PTStatusPortClear.setStatus("mandatory")
_SwhL2PTStatusTable_Object = MibTable
swhL2PTStatusTable = _SwhL2PTStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 5)
)
if mibBuilder.loadTexts:
    swhL2PTStatusTable.setStatus("mandatory")
_SwhL2PTStatusEntry_Object = MibTableRow
swhL2PTStatusEntry = _SwhL2PTStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 5, 1)
)
swhL2PTStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhL2PTStatusIndex"),
)
if mibBuilder.loadTexts:
    swhL2PTStatusEntry.setStatus("mandatory")


class _SwhL2PTStatusIndex_Type(Integer32):
    """Custom type swhL2PTStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhL2PTStatusIndex_Type.__name__ = "Integer32"
_SwhL2PTStatusIndex_Object = MibTableColumn
swhL2PTStatusIndex = _SwhL2PTStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 5, 1, 1),
    _SwhL2PTStatusIndex_Type()
)
swhL2PTStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhL2PTStatusIndex.setStatus("mandatory")
_SwhL2PTStatusCounterName_Type = DisplayString
_SwhL2PTStatusCounterName_Object = MibTableColumn
swhL2PTStatusCounterName = _SwhL2PTStatusCounterName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 5, 1, 2),
    _SwhL2PTStatusCounterName_Type()
)
swhL2PTStatusCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhL2PTStatusCounterName.setStatus("mandatory")


class _SwhL2PTStatusState_Type(Integer32):
    """Custom type swhL2PTStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhL2PTStatusState_Type.__name__ = "Integer32"
_SwhL2PTStatusState_Object = MibTableColumn
swhL2PTStatusState = _SwhL2PTStatusState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 5, 1, 3),
    _SwhL2PTStatusState_Type()
)
swhL2PTStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhL2PTStatusState.setStatus("mandatory")
_SwhL2PTStatusEncapsulationCounters_Type = Counter32
_SwhL2PTStatusEncapsulationCounters_Object = MibTableColumn
swhL2PTStatusEncapsulationCounters = _SwhL2PTStatusEncapsulationCounters_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 5, 1, 4),
    _SwhL2PTStatusEncapsulationCounters_Type()
)
swhL2PTStatusEncapsulationCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhL2PTStatusEncapsulationCounters.setStatus("mandatory")
_SwhL2PTStatusDecapsulationCounters_Type = Counter32
_SwhL2PTStatusDecapsulationCounters_Object = MibTableColumn
swhL2PTStatusDecapsulationCounters = _SwhL2PTStatusDecapsulationCounters_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 25, 5, 1, 5),
    _SwhL2PTStatusDecapsulationCounters_Type()
)
swhL2PTStatusDecapsulationCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhL2PTStatusDecapsulationCounters.setStatus("mandatory")
_SwhIGMPStatus_ObjectIdentity = ObjectIdentity
swhIGMPStatus = _SwhIGMPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26)
)
_SwhIGMPStatusTable_Object = MibTable
swhIGMPStatusTable = _SwhIGMPStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2)
)
if mibBuilder.loadTexts:
    swhIGMPStatusTable.setStatus("mandatory")
_SwhIGMPStatusEntry_Object = MibTableRow
swhIGMPStatusEntry = _SwhIGMPStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1)
)
swhIGMPStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhIGMPStatusIndex"),
)
if mibBuilder.loadTexts:
    swhIGMPStatusEntry.setStatus("mandatory")


class _SwhIGMPStatusIndex_Type(Integer32):
    """Custom type swhIGMPStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhIGMPStatusIndex_Type.__name__ = "Integer32"
_SwhIGMPStatusIndex_Object = MibTableColumn
swhIGMPStatusIndex = _SwhIGMPStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 1),
    _SwhIGMPStatusIndex_Type()
)
swhIGMPStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhIGMPStatusIndex.setStatus("mandatory")
_SwhIGMPStatusVLANID_Type = Integer32
_SwhIGMPStatusVLANID_Object = MibTableColumn
swhIGMPStatusVLANID = _SwhIGMPStatusVLANID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 3),
    _SwhIGMPStatusVLANID_Type()
)
swhIGMPStatusVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPStatusVLANID.setStatus("mandatory")


class _SwhIGMPStatusQuerier_Type(Integer32):
    """Custom type swhIGMPStatusQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("active", 1))
    )


_SwhIGMPStatusQuerier_Type.__name__ = "Integer32"
_SwhIGMPStatusQuerier_Object = MibTableColumn
swhIGMPStatusQuerier = _SwhIGMPStatusQuerier_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 5),
    _SwhIGMPStatusQuerier_Type()
)
swhIGMPStatusQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPStatusQuerier.setStatus("mandatory")
_SwhIGMPStatusQueriesTransmitted_Type = Integer32
_SwhIGMPStatusQueriesTransmitted_Object = MibTableColumn
swhIGMPStatusQueriesTransmitted = _SwhIGMPStatusQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 7),
    _SwhIGMPStatusQueriesTransmitted_Type()
)
swhIGMPStatusQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPStatusQueriesTransmitted.setStatus("mandatory")
_SwhIGMPStatusQueriesReceived_Type = Integer32
_SwhIGMPStatusQueriesReceived_Object = MibTableColumn
swhIGMPStatusQueriesReceived = _SwhIGMPStatusQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 9),
    _SwhIGMPStatusQueriesReceived_Type()
)
swhIGMPStatusQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPStatusQueriesReceived.setStatus("mandatory")
_SwhIGMPStatusV1Reports_Type = Integer32
_SwhIGMPStatusV1Reports_Object = MibTableColumn
swhIGMPStatusV1Reports = _SwhIGMPStatusV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 11),
    _SwhIGMPStatusV1Reports_Type()
)
swhIGMPStatusV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPStatusV1Reports.setStatus("mandatory")
_SwhIGMPStatusV2Reports_Type = Integer32
_SwhIGMPStatusV2Reports_Object = MibTableColumn
swhIGMPStatusV2Reports = _SwhIGMPStatusV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 13),
    _SwhIGMPStatusV2Reports_Type()
)
swhIGMPStatusV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPStatusV2Reports.setStatus("mandatory")
_SwhIGMPStatusV3Reports_Type = Integer32
_SwhIGMPStatusV3Reports_Object = MibTableColumn
swhIGMPStatusV3Reports = _SwhIGMPStatusV3Reports_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 15),
    _SwhIGMPStatusV3Reports_Type()
)
swhIGMPStatusV3Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPStatusV3Reports.setStatus("mandatory")
_SwhIGMPStatusV2Leaves_Type = Integer32
_SwhIGMPStatusV2Leaves_Object = MibTableColumn
swhIGMPStatusV2Leaves = _SwhIGMPStatusV2Leaves_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 26, 2, 1, 17),
    _SwhIGMPStatusV2Leaves_Type()
)
swhIGMPStatusV2Leaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPStatusV2Leaves.setStatus("mandatory")
_SwhMLDStatus_ObjectIdentity = ObjectIdentity
swhMLDStatus = _SwhMLDStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27)
)
_SwhMLDStatusTable_Object = MibTable
swhMLDStatusTable = _SwhMLDStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2)
)
if mibBuilder.loadTexts:
    swhMLDStatusTable.setStatus("mandatory")
_SwhMLDStatusEntry_Object = MibTableRow
swhMLDStatusEntry = _SwhMLDStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1)
)
swhMLDStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhMLDStatusIndex"),
)
if mibBuilder.loadTexts:
    swhMLDStatusEntry.setStatus("mandatory")


class _SwhMLDStatusIndex_Type(Integer32):
    """Custom type swhMLDStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMLDStatusIndex_Type.__name__ = "Integer32"
_SwhMLDStatusIndex_Object = MibTableColumn
swhMLDStatusIndex = _SwhMLDStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1, 1),
    _SwhMLDStatusIndex_Type()
)
swhMLDStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhMLDStatusIndex.setStatus("mandatory")
_SwhMLDStatusVLANID_Type = Integer32
_SwhMLDStatusVLANID_Object = MibTableColumn
swhMLDStatusVLANID = _SwhMLDStatusVLANID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1, 3),
    _SwhMLDStatusVLANID_Type()
)
swhMLDStatusVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDStatusVLANID.setStatus("mandatory")


class _SwhMLDStatusQuerier_Type(Integer32):
    """Custom type swhMLDStatusQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("active", 1))
    )


_SwhMLDStatusQuerier_Type.__name__ = "Integer32"
_SwhMLDStatusQuerier_Object = MibTableColumn
swhMLDStatusQuerier = _SwhMLDStatusQuerier_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1, 5),
    _SwhMLDStatusQuerier_Type()
)
swhMLDStatusQuerier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDStatusQuerier.setStatus("mandatory")
_SwhMLDStatusQueriesTransmitted_Type = Integer32
_SwhMLDStatusQueriesTransmitted_Object = MibTableColumn
swhMLDStatusQueriesTransmitted = _SwhMLDStatusQueriesTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1, 7),
    _SwhMLDStatusQueriesTransmitted_Type()
)
swhMLDStatusQueriesTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDStatusQueriesTransmitted.setStatus("mandatory")
_SwhMLDStatusQueriesReceived_Type = Integer32
_SwhMLDStatusQueriesReceived_Object = MibTableColumn
swhMLDStatusQueriesReceived = _SwhMLDStatusQueriesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1, 9),
    _SwhMLDStatusQueriesReceived_Type()
)
swhMLDStatusQueriesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDStatusQueriesReceived.setStatus("mandatory")
_SwhMLDStatusV1Reports_Type = Integer32
_SwhMLDStatusV1Reports_Object = MibTableColumn
swhMLDStatusV1Reports = _SwhMLDStatusV1Reports_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1, 11),
    _SwhMLDStatusV1Reports_Type()
)
swhMLDStatusV1Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDStatusV1Reports.setStatus("mandatory")
_SwhMLDStatusV2Reports_Type = Integer32
_SwhMLDStatusV2Reports_Object = MibTableColumn
swhMLDStatusV2Reports = _SwhMLDStatusV2Reports_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1, 13),
    _SwhMLDStatusV2Reports_Type()
)
swhMLDStatusV2Reports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDStatusV2Reports.setStatus("mandatory")
_SwhMLDStatusDone_Type = Integer32
_SwhMLDStatusDone_Object = MibTableColumn
swhMLDStatusDone = _SwhMLDStatusDone_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 27, 2, 1, 15),
    _SwhMLDStatusDone_Type()
)
swhMLDStatusDone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDStatusDone.setStatus("mandatory")
_SwhIGMPGroupTable_ObjectIdentity = ObjectIdentity
swhIGMPGroupTable = _SwhIGMPGroupTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28)
)


class _SwhIGMPState_Type(Integer32):
    """Custom type swhIGMPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhIGMPState_Type.__name__ = "Integer32"
_SwhIGMPState_Object = MibScalar
swhIGMPState = _SwhIGMPState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 1),
    _SwhIGMPState_Type()
)
swhIGMPState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPState.setStatus("mandatory")
_SwhIGMPTable_Object = MibTable
swhIGMPTable = _SwhIGMPTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2)
)
if mibBuilder.loadTexts:
    swhIGMPTable.setStatus("mandatory")
_SwhIGMPTableEntry_Object = MibTableRow
swhIGMPTableEntry = _SwhIGMPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1)
)
swhIGMPTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhIGMPGroupTableIndex"),
)
if mibBuilder.loadTexts:
    swhIGMPTableEntry.setStatus("mandatory")


class _SwhIGMPGroupTableIndex_Type(Integer32):
    """Custom type swhIGMPGroupTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhIGMPGroupTableIndex_Type.__name__ = "Integer32"
_SwhIGMPGroupTableIndex_Object = MibTableColumn
swhIGMPGroupTableIndex = _SwhIGMPGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 1),
    _SwhIGMPGroupTableIndex_Type()
)
swhIGMPGroupTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhIGMPGroupTableIndex.setStatus("mandatory")


class _SwhIGMPGroupTableGroup_Type(DisplayString):
    """Custom type swhIGMPGroupTableGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhIGMPGroupTableGroup_Type.__name__ = "DisplayString"
_SwhIGMPGroupTableGroup_Object = MibTableColumn
swhIGMPGroupTableGroup = _SwhIGMPGroupTableGroup_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 3),
    _SwhIGMPGroupTableGroup_Type()
)
swhIGMPGroupTableGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPGroupTableGroup.setStatus("mandatory")


class _SwhIGMPGroupTablePort1_Type(Integer32):
    """Custom type swhIGMPGroupTablePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPGroupTablePort1_Type.__name__ = "Integer32"
_SwhIGMPGroupTablePort1_Object = MibTableColumn
swhIGMPGroupTablePort1 = _SwhIGMPGroupTablePort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 5),
    _SwhIGMPGroupTablePort1_Type()
)
swhIGMPGroupTablePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPGroupTablePort1.setStatus("mandatory")


class _SwhIGMPGroupTablePort2_Type(Integer32):
    """Custom type swhIGMPGroupTablePort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPGroupTablePort2_Type.__name__ = "Integer32"
_SwhIGMPGroupTablePort2_Object = MibTableColumn
swhIGMPGroupTablePort2 = _SwhIGMPGroupTablePort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 6),
    _SwhIGMPGroupTablePort2_Type()
)
swhIGMPGroupTablePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPGroupTablePort2.setStatus("mandatory")


class _SwhIGMPGroupTablePort3_Type(Integer32):
    """Custom type swhIGMPGroupTablePort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPGroupTablePort3_Type.__name__ = "Integer32"
_SwhIGMPGroupTablePort3_Object = MibTableColumn
swhIGMPGroupTablePort3 = _SwhIGMPGroupTablePort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 7),
    _SwhIGMPGroupTablePort3_Type()
)
swhIGMPGroupTablePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPGroupTablePort3.setStatus("mandatory")


class _SwhIGMPGroupTablePort4_Type(Integer32):
    """Custom type swhIGMPGroupTablePort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPGroupTablePort4_Type.__name__ = "Integer32"
_SwhIGMPGroupTablePort4_Object = MibTableColumn
swhIGMPGroupTablePort4 = _SwhIGMPGroupTablePort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 8),
    _SwhIGMPGroupTablePort4_Type()
)
swhIGMPGroupTablePort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPGroupTablePort4.setStatus("mandatory")


class _SwhIGMPGroupTablePort5_Type(Integer32):
    """Custom type swhIGMPGroupTablePort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPGroupTablePort5_Type.__name__ = "Integer32"
_SwhIGMPGroupTablePort5_Object = MibTableColumn
swhIGMPGroupTablePort5 = _SwhIGMPGroupTablePort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 9),
    _SwhIGMPGroupTablePort5_Type()
)
swhIGMPGroupTablePort5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPGroupTablePort5.setStatus("mandatory")


class _SwhIGMPGroupTablePort6_Type(Integer32):
    """Custom type swhIGMPGroupTablePort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhIGMPGroupTablePort6_Type.__name__ = "Integer32"
_SwhIGMPGroupTablePort6_Object = MibTableColumn
swhIGMPGroupTablePort6 = _SwhIGMPGroupTablePort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 10),
    _SwhIGMPGroupTablePort6_Type()
)
swhIGMPGroupTablePort6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPGroupTablePort6.setStatus("mandatory")
_SwhIGMPGroupTableVID_Type = Integer32
_SwhIGMPGroupTableVID_Object = MibTableColumn
swhIGMPGroupTableVID = _SwhIGMPGroupTableVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 28, 2, 1, 60),
    _SwhIGMPGroupTableVID_Type()
)
swhIGMPGroupTableVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhIGMPGroupTableVID.setStatus("mandatory")
_SwhMLDGroupTable_ObjectIdentity = ObjectIdentity
swhMLDGroupTable = _SwhMLDGroupTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29)
)


class _SwhMLDState_Type(Integer32):
    """Custom type swhMLDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhMLDState_Type.__name__ = "Integer32"
_SwhMLDState_Object = MibScalar
swhMLDState = _SwhMLDState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 1),
    _SwhMLDState_Type()
)
swhMLDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDState.setStatus("mandatory")
_SwhMLDTable_Object = MibTable
swhMLDTable = _SwhMLDTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2)
)
if mibBuilder.loadTexts:
    swhMLDTable.setStatus("mandatory")
_SwhMLDTableEntry_Object = MibTableRow
swhMLDTableEntry = _SwhMLDTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1)
)
swhMLDTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhMLDGroupTableIndex"),
)
if mibBuilder.loadTexts:
    swhMLDTableEntry.setStatus("mandatory")


class _SwhMLDGroupTableIndex_Type(Integer32):
    """Custom type swhMLDGroupTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMLDGroupTableIndex_Type.__name__ = "Integer32"
_SwhMLDGroupTableIndex_Object = MibTableColumn
swhMLDGroupTableIndex = _SwhMLDGroupTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 1),
    _SwhMLDGroupTableIndex_Type()
)
swhMLDGroupTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhMLDGroupTableIndex.setStatus("mandatory")


class _SwhMLDGroupTableGroup_Type(DisplayString):
    """Custom type swhMLDGroupTableGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhMLDGroupTableGroup_Type.__name__ = "DisplayString"
_SwhMLDGroupTableGroup_Object = MibTableColumn
swhMLDGroupTableGroup = _SwhMLDGroupTableGroup_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 3),
    _SwhMLDGroupTableGroup_Type()
)
swhMLDGroupTableGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDGroupTableGroup.setStatus("mandatory")


class _SwhMLDGroupTablePort1_Type(Integer32):
    """Custom type swhMLDGroupTablePort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhMLDGroupTablePort1_Type.__name__ = "Integer32"
_SwhMLDGroupTablePort1_Object = MibTableColumn
swhMLDGroupTablePort1 = _SwhMLDGroupTablePort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 5),
    _SwhMLDGroupTablePort1_Type()
)
swhMLDGroupTablePort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDGroupTablePort1.setStatus("mandatory")


class _SwhMLDGroupTablePort2_Type(Integer32):
    """Custom type swhMLDGroupTablePort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhMLDGroupTablePort2_Type.__name__ = "Integer32"
_SwhMLDGroupTablePort2_Object = MibTableColumn
swhMLDGroupTablePort2 = _SwhMLDGroupTablePort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 6),
    _SwhMLDGroupTablePort2_Type()
)
swhMLDGroupTablePort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDGroupTablePort2.setStatus("mandatory")


class _SwhMLDGroupTablePort3_Type(Integer32):
    """Custom type swhMLDGroupTablePort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhMLDGroupTablePort3_Type.__name__ = "Integer32"
_SwhMLDGroupTablePort3_Object = MibTableColumn
swhMLDGroupTablePort3 = _SwhMLDGroupTablePort3_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 7),
    _SwhMLDGroupTablePort3_Type()
)
swhMLDGroupTablePort3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDGroupTablePort3.setStatus("mandatory")


class _SwhMLDGroupTablePort4_Type(Integer32):
    """Custom type swhMLDGroupTablePort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhMLDGroupTablePort4_Type.__name__ = "Integer32"
_SwhMLDGroupTablePort4_Object = MibTableColumn
swhMLDGroupTablePort4 = _SwhMLDGroupTablePort4_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 8),
    _SwhMLDGroupTablePort4_Type()
)
swhMLDGroupTablePort4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDGroupTablePort4.setStatus("mandatory")


class _SwhMLDGroupTablePort5_Type(Integer32):
    """Custom type swhMLDGroupTablePort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhMLDGroupTablePort5_Type.__name__ = "Integer32"
_SwhMLDGroupTablePort5_Object = MibTableColumn
swhMLDGroupTablePort5 = _SwhMLDGroupTablePort5_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 9),
    _SwhMLDGroupTablePort5_Type()
)
swhMLDGroupTablePort5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDGroupTablePort5.setStatus("mandatory")


class _SwhMLDGroupTablePort6_Type(Integer32):
    """Custom type swhMLDGroupTablePort6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("b", 0),
          ("v", 1))
    )


_SwhMLDGroupTablePort6_Type.__name__ = "Integer32"
_SwhMLDGroupTablePort6_Object = MibTableColumn
swhMLDGroupTablePort6 = _SwhMLDGroupTablePort6_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 10),
    _SwhMLDGroupTablePort6_Type()
)
swhMLDGroupTablePort6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDGroupTablePort6.setStatus("mandatory")
_SwhMLDGroupTableVID_Type = Integer32
_SwhMLDGroupTableVID_Object = MibTableColumn
swhMLDGroupTableVID = _SwhMLDGroupTableVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 29, 2, 1, 60),
    _SwhMLDGroupTableVID_Type()
)
swhMLDGroupTableVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMLDGroupTableVID.setStatus("mandatory")
_Swh8021XPortStatus_ObjectIdentity = ObjectIdentity
swh8021XPortStatus = _Swh8021XPortStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 32)
)
_Swh8021XPortStatusTable_Object = MibTable
swh8021XPortStatusTable = _Swh8021XPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 32, 1)
)
if mibBuilder.loadTexts:
    swh8021XPortStatusTable.setStatus("mandatory")
_Swh8021XPortStatusEntry_Object = MibTableRow
swh8021XPortStatusEntry = _Swh8021XPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 32, 1, 1)
)
swh8021XPortStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swh8021XPortStatusIndex"),
)
if mibBuilder.loadTexts:
    swh8021XPortStatusEntry.setStatus("mandatory")


class _Swh8021XPortStatusIndex_Type(Integer32):
    """Custom type swh8021XPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Swh8021XPortStatusIndex_Type.__name__ = "Integer32"
_Swh8021XPortStatusIndex_Object = MibTableColumn
swh8021XPortStatusIndex = _Swh8021XPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 32, 1, 1, 1),
    _Swh8021XPortStatusIndex_Type()
)
swh8021XPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swh8021XPortStatusIndex.setStatus("mandatory")


class _Swh8021XPortStatusState_Type(Integer32):
    """Custom type swh8021XPortStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkdown", 0),
          ("authorized", 1),
          ("unauthorized", 2),
          ("disabled", 3))
    )


_Swh8021XPortStatusState_Type.__name__ = "Integer32"
_Swh8021XPortStatusState_Object = MibTableColumn
swh8021XPortStatusState = _Swh8021XPortStatusState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 32, 1, 1, 3),
    _Swh8021XPortStatusState_Type()
)
swh8021XPortStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XPortStatusState.setStatus("mandatory")
_Swh8021XPortStatusLastSource_Type = DisplayString
_Swh8021XPortStatusLastSource_Object = MibTableColumn
swh8021XPortStatusLastSource = _Swh8021XPortStatusLastSource_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 32, 1, 1, 5),
    _Swh8021XPortStatusLastSource_Type()
)
swh8021XPortStatusLastSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XPortStatusLastSource.setStatus("mandatory")
_Swh8021XPortStatusLastID_Type = DisplayString
_Swh8021XPortStatusLastID_Object = MibTableColumn
swh8021XPortStatusLastID = _Swh8021XPortStatusLastID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 32, 1, 1, 7),
    _Swh8021XPortStatusLastID_Type()
)
swh8021XPortStatusLastID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XPortStatusLastID.setStatus("mandatory")
_Swh8021XPortStatusAssignedVLAN_Type = DisplayString
_Swh8021XPortStatusAssignedVLAN_Object = MibTableColumn
swh8021XPortStatusAssignedVLAN = _Swh8021XPortStatusAssignedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 32, 1, 1, 9),
    _Swh8021XPortStatusAssignedVLAN_Type()
)
swh8021XPortStatusAssignedVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XPortStatusAssignedVLAN.setStatus("mandatory")
_Swh8021XStatistics_ObjectIdentity = ObjectIdentity
swh8021XStatistics = _Swh8021XStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33)
)
_Swh8021XStatisticsTable_Object = MibTable
swh8021XStatisticsTable = _Swh8021XStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1)
)
if mibBuilder.loadTexts:
    swh8021XStatisticsTable.setStatus("mandatory")
_Swh8021XStatisticsEntry_Object = MibTableRow
swh8021XStatisticsEntry = _Swh8021XStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1)
)
swh8021XStatisticsEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swh8021XStatisticsIndex"),
)
if mibBuilder.loadTexts:
    swh8021XStatisticsEntry.setStatus("mandatory")


class _Swh8021XStatisticsIndex_Type(Integer32):
    """Custom type swh8021XStatisticsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Swh8021XStatisticsIndex_Type.__name__ = "Integer32"
_Swh8021XStatisticsIndex_Object = MibTableColumn
swh8021XStatisticsIndex = _Swh8021XStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 1),
    _Swh8021XStatisticsIndex_Type()
)
swh8021XStatisticsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swh8021XStatisticsIndex.setStatus("mandatory")
_Swh8021XStatisticsRxTotal_Type = Counter32
_Swh8021XStatisticsRxTotal_Object = MibTableColumn
swh8021XStatisticsRxTotal = _Swh8021XStatisticsRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 2),
    _Swh8021XStatisticsRxTotal_Type()
)
swh8021XStatisticsRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxTotal.setStatus("mandatory")
_Swh8021XStatisticsRxResponseID_Type = Counter32
_Swh8021XStatisticsRxResponseID_Object = MibTableColumn
swh8021XStatisticsRxResponseID = _Swh8021XStatisticsRxResponseID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 3),
    _Swh8021XStatisticsRxResponseID_Type()
)
swh8021XStatisticsRxResponseID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxResponseID.setStatus("mandatory")
_Swh8021XStatisticsRxResponse_Type = Counter32
_Swh8021XStatisticsRxResponse_Object = MibTableColumn
swh8021XStatisticsRxResponse = _Swh8021XStatisticsRxResponse_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 4),
    _Swh8021XStatisticsRxResponse_Type()
)
swh8021XStatisticsRxResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxResponse.setStatus("mandatory")
_Swh8021XStatisticsRxStart_Type = Counter32
_Swh8021XStatisticsRxStart_Object = MibTableColumn
swh8021XStatisticsRxStart = _Swh8021XStatisticsRxStart_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 5),
    _Swh8021XStatisticsRxStart_Type()
)
swh8021XStatisticsRxStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxStart.setStatus("mandatory")
_Swh8021XStatisticsRxLogoff_Type = Counter32
_Swh8021XStatisticsRxLogoff_Object = MibTableColumn
swh8021XStatisticsRxLogoff = _Swh8021XStatisticsRxLogoff_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 6),
    _Swh8021XStatisticsRxLogoff_Type()
)
swh8021XStatisticsRxLogoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxLogoff.setStatus("mandatory")
_Swh8021XStatisticsRxInvalidType_Type = Counter32
_Swh8021XStatisticsRxInvalidType_Object = MibTableColumn
swh8021XStatisticsRxInvalidType = _Swh8021XStatisticsRxInvalidType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 7),
    _Swh8021XStatisticsRxInvalidType_Type()
)
swh8021XStatisticsRxInvalidType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxInvalidType.setStatus("mandatory")
_Swh8021XStatisticsRxInvalidLength_Type = Counter32
_Swh8021XStatisticsRxInvalidLength_Object = MibTableColumn
swh8021XStatisticsRxInvalidLength = _Swh8021XStatisticsRxInvalidLength_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 8),
    _Swh8021XStatisticsRxInvalidLength_Type()
)
swh8021XStatisticsRxInvalidLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxInvalidLength.setStatus("mandatory")
_Swh8021XStatisticsRxAccessChallenges_Type = Counter32
_Swh8021XStatisticsRxAccessChallenges_Object = MibTableColumn
swh8021XStatisticsRxAccessChallenges = _Swh8021XStatisticsRxAccessChallenges_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 9),
    _Swh8021XStatisticsRxAccessChallenges_Type()
)
swh8021XStatisticsRxAccessChallenges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxAccessChallenges.setStatus("mandatory")
_Swh8021XStatisticsRxOtherRequests_Type = Counter32
_Swh8021XStatisticsRxOtherRequests_Object = MibTableColumn
swh8021XStatisticsRxOtherRequests = _Swh8021XStatisticsRxOtherRequests_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 10),
    _Swh8021XStatisticsRxOtherRequests_Type()
)
swh8021XStatisticsRxOtherRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxOtherRequests.setStatus("mandatory")
_Swh8021XStatisticsRxAuthSuccesses_Type = Counter32
_Swh8021XStatisticsRxAuthSuccesses_Object = MibTableColumn
swh8021XStatisticsRxAuthSuccesses = _Swh8021XStatisticsRxAuthSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 11),
    _Swh8021XStatisticsRxAuthSuccesses_Type()
)
swh8021XStatisticsRxAuthSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxAuthSuccesses.setStatus("mandatory")
_Swh8021XStatisticsRxAuthFailures_Type = Counter32
_Swh8021XStatisticsRxAuthFailures_Object = MibTableColumn
swh8021XStatisticsRxAuthFailures = _Swh8021XStatisticsRxAuthFailures_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 12),
    _Swh8021XStatisticsRxAuthFailures_Type()
)
swh8021XStatisticsRxAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsRxAuthFailures.setStatus("mandatory")
_Swh8021XStatisticsTxTotal_Type = Counter32
_Swh8021XStatisticsTxTotal_Object = MibTableColumn
swh8021XStatisticsTxTotal = _Swh8021XStatisticsTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 13),
    _Swh8021XStatisticsTxTotal_Type()
)
swh8021XStatisticsTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsTxTotal.setStatus("mandatory")
_Swh8021XStatisticsTxRequestID_Type = Counter32
_Swh8021XStatisticsTxRequestID_Object = MibTableColumn
swh8021XStatisticsTxRequestID = _Swh8021XStatisticsTxRequestID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 14),
    _Swh8021XStatisticsTxRequestID_Type()
)
swh8021XStatisticsTxRequestID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsTxRequestID.setStatus("mandatory")
_Swh8021XStatisticsTxRequest_Type = Counter32
_Swh8021XStatisticsTxRequest_Object = MibTableColumn
swh8021XStatisticsTxRequest = _Swh8021XStatisticsTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 15),
    _Swh8021XStatisticsTxRequest_Type()
)
swh8021XStatisticsTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsTxRequest.setStatus("mandatory")
_Swh8021XStatisticsTxResponses_Type = Counter32
_Swh8021XStatisticsTxResponses_Object = MibTableColumn
swh8021XStatisticsTxResponses = _Swh8021XStatisticsTxResponses_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 16),
    _Swh8021XStatisticsTxResponses_Type()
)
swh8021XStatisticsTxResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swh8021XStatisticsTxResponses.setStatus("mandatory")


class _Swh8021XStatisticsClear_Type(Integer32):
    """Custom type swh8021XStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_Swh8021XStatisticsClear_Type.__name__ = "Integer32"
_Swh8021XStatisticsClear_Object = MibTableColumn
swh8021XStatisticsClear = _Swh8021XStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 1, 1, 17),
    _Swh8021XStatisticsClear_Type()
)
swh8021XStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XStatisticsClear.setStatus("mandatory")


class _Swh8021XStatisticsClearCountersOfAllPort_Type(Integer32):
    """Custom type swh8021XStatisticsClearCountersOfAllPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_Swh8021XStatisticsClearCountersOfAllPort_Type.__name__ = "Integer32"
_Swh8021XStatisticsClearCountersOfAllPort_Object = MibScalar
swh8021XStatisticsClearCountersOfAllPort = _Swh8021XStatisticsClearCountersOfAllPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 33, 2),
    _Swh8021XStatisticsClearCountersOfAllPort_Type()
)
swh8021XStatisticsClearCountersOfAllPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swh8021XStatisticsClearCountersOfAllPort.setStatus("mandatory")
_SwhSFPInformation_ObjectIdentity = ObjectIdentity
swhSFPInformation = _SwhSFPInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34)
)
_SwhSFPPortInfo_ObjectIdentity = ObjectIdentity
swhSFPPortInfo = _SwhSFPPortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1)
)
_SwhSFPPortInfoTable_Object = MibTable
swhSFPPortInfoTable = _SwhSFPPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1)
)
if mibBuilder.loadTexts:
    swhSFPPortInfoTable.setStatus("mandatory")
_SwhSFPPortInfoEntry_Object = MibTableRow
swhSFPPortInfoEntry = _SwhSFPPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1, 1)
)
swhSFPPortInfoEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhSFPPortInfoIndex"),
)
if mibBuilder.loadTexts:
    swhSFPPortInfoEntry.setStatus("mandatory")


class _SwhSFPPortInfoIndex_Type(Integer32):
    """Custom type swhSFPPortInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhSFPPortInfoIndex_Type.__name__ = "Integer32"
_SwhSFPPortInfoIndex_Object = MibTableColumn
swhSFPPortInfoIndex = _SwhSFPPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1, 1, 1),
    _SwhSFPPortInfoIndex_Type()
)
swhSFPPortInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhSFPPortInfoIndex.setStatus("mandatory")
_SwhSFPPortInfoPortName_Type = DisplayString
_SwhSFPPortInfoPortName_Object = MibTableColumn
swhSFPPortInfoPortName = _SwhSFPPortInfoPortName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1, 1, 3),
    _SwhSFPPortInfoPortName_Type()
)
swhSFPPortInfoPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortInfoPortName.setStatus("mandatory")
_SwhSFPPortInfoSpeed_Type = DisplayString
_SwhSFPPortInfoSpeed_Object = MibTableColumn
swhSFPPortInfoSpeed = _SwhSFPPortInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1, 1, 5),
    _SwhSFPPortInfoSpeed_Type()
)
swhSFPPortInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortInfoSpeed.setStatus("mandatory")
_SwhSFPPortInfoDistance_Type = DisplayString
_SwhSFPPortInfoDistance_Object = MibTableColumn
swhSFPPortInfoDistance = _SwhSFPPortInfoDistance_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1, 1, 7),
    _SwhSFPPortInfoDistance_Type()
)
swhSFPPortInfoDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortInfoDistance.setStatus("mandatory")
_SwhSFPPortInfoVendorName_Type = DisplayString
_SwhSFPPortInfoVendorName_Object = MibTableColumn
swhSFPPortInfoVendorName = _SwhSFPPortInfoVendorName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1, 1, 9),
    _SwhSFPPortInfoVendorName_Type()
)
swhSFPPortInfoVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortInfoVendorName.setStatus("mandatory")
_SwhSFPPortInfoVendorPN_Type = DisplayString
_SwhSFPPortInfoVendorPN_Object = MibTableColumn
swhSFPPortInfoVendorPN = _SwhSFPPortInfoVendorPN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1, 1, 11),
    _SwhSFPPortInfoVendorPN_Type()
)
swhSFPPortInfoVendorPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortInfoVendorPN.setStatus("mandatory")
_SwhSFPPortInfoVendorSN_Type = DisplayString
_SwhSFPPortInfoVendorSN_Object = MibTableColumn
swhSFPPortInfoVendorSN = _SwhSFPPortInfoVendorSN_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 1, 1, 1, 13),
    _SwhSFPPortInfoVendorSN_Type()
)
swhSFPPortInfoVendorSN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortInfoVendorSN.setStatus("mandatory")
_SwhSFPPortState_ObjectIdentity = ObjectIdentity
swhSFPPortState = _SwhSFPPortState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2)
)
_SwhSFPPortStateTable_Object = MibTable
swhSFPPortStateTable = _SwhSFPPortStateTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1)
)
if mibBuilder.loadTexts:
    swhSFPPortStateTable.setStatus("mandatory")
_SwhSFPPortStateEntry_Object = MibTableRow
swhSFPPortStateEntry = _SwhSFPPortStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1, 1)
)
swhSFPPortStateEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhSFPPortStateIndex"),
)
if mibBuilder.loadTexts:
    swhSFPPortStateEntry.setStatus("mandatory")


class _SwhSFPPortStateIndex_Type(Integer32):
    """Custom type swhSFPPortStateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhSFPPortStateIndex_Type.__name__ = "Integer32"
_SwhSFPPortStateIndex_Object = MibTableColumn
swhSFPPortStateIndex = _SwhSFPPortStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1, 1, 1),
    _SwhSFPPortStateIndex_Type()
)
swhSFPPortStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhSFPPortStateIndex.setStatus("mandatory")
_SwhSFPPortStatePortName_Type = DisplayString
_SwhSFPPortStatePortName_Object = MibTableColumn
swhSFPPortStatePortName = _SwhSFPPortStatePortName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1, 1, 3),
    _SwhSFPPortStatePortName_Type()
)
swhSFPPortStatePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortStatePortName.setStatus("mandatory")
_SwhSFPPortStateTemperature_Type = DisplayString
_SwhSFPPortStateTemperature_Object = MibTableColumn
swhSFPPortStateTemperature = _SwhSFPPortStateTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1, 1, 5),
    _SwhSFPPortStateTemperature_Type()
)
swhSFPPortStateTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortStateTemperature.setStatus("mandatory")
_SwhSFPPortStateVoltage_Type = DisplayString
_SwhSFPPortStateVoltage_Object = MibTableColumn
swhSFPPortStateVoltage = _SwhSFPPortStateVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1, 1, 7),
    _SwhSFPPortStateVoltage_Type()
)
swhSFPPortStateVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortStateVoltage.setStatus("mandatory")
_SwhSFPPortStateTXBias_Type = DisplayString
_SwhSFPPortStateTXBias_Object = MibTableColumn
swhSFPPortStateTXBias = _SwhSFPPortStateTXBias_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1, 1, 9),
    _SwhSFPPortStateTXBias_Type()
)
swhSFPPortStateTXBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortStateTXBias.setStatus("mandatory")
_SwhSFPPortStateTXPower_Type = DisplayString
_SwhSFPPortStateTXPower_Object = MibTableColumn
swhSFPPortStateTXPower = _SwhSFPPortStateTXPower_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1, 1, 11),
    _SwhSFPPortStateTXPower_Type()
)
swhSFPPortStateTXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortStateTXPower.setStatus("mandatory")
_SwhSFPPortStateRXPower_Type = DisplayString
_SwhSFPPortStateRXPower_Object = MibTableColumn
swhSFPPortStateRXPower = _SwhSFPPortStateRXPower_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 34, 2, 1, 1, 13),
    _SwhSFPPortStateRXPower_Type()
)
swhSFPPortStateRXPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhSFPPortStateRXPower.setStatus("mandatory")
_SwhDHCPSnoopingTable_ObjectIdentity = ObjectIdentity
swhDHCPSnoopingTable = _SwhDHCPSnoopingTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35)
)
_SwhDHCPSnoopingTableTable_Object = MibTable
swhDHCPSnoopingTableTable = _SwhDHCPSnoopingTableTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7)
)
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableTable.setStatus("mandatory")
_SwhDHCPSnoopingTableEntry_Object = MibTableRow
swhDHCPSnoopingTableEntry = _SwhDHCPSnoopingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1)
)
swhDHCPSnoopingTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDHCPSnoopingTableIndex"),
)
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableEntry.setStatus("mandatory")


class _SwhDHCPSnoopingTableIndex_Type(Integer32):
    """Custom type swhDHCPSnoopingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDHCPSnoopingTableIndex_Type.__name__ = "Integer32"
_SwhDHCPSnoopingTableIndex_Object = MibTableColumn
swhDHCPSnoopingTableIndex = _SwhDHCPSnoopingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1, 1),
    _SwhDHCPSnoopingTableIndex_Type()
)
swhDHCPSnoopingTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableIndex.setStatus("mandatory")
_SwhDHCPSnoopingTableCliPort_Type = Integer32
_SwhDHCPSnoopingTableCliPort_Object = MibTableColumn
swhDHCPSnoopingTableCliPort = _SwhDHCPSnoopingTableCliPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1, 2),
    _SwhDHCPSnoopingTableCliPort_Type()
)
swhDHCPSnoopingTableCliPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableCliPort.setStatus("mandatory")
_SwhDHCPSnoopingTableSrvPort_Type = Integer32
_SwhDHCPSnoopingTableSrvPort_Object = MibTableColumn
swhDHCPSnoopingTableSrvPort = _SwhDHCPSnoopingTableSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1, 3),
    _SwhDHCPSnoopingTableSrvPort_Type()
)
swhDHCPSnoopingTableSrvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableSrvPort.setStatus("mandatory")
_SwhDHCPSnoopingTableVID_Type = Integer32
_SwhDHCPSnoopingTableVID_Object = MibTableColumn
swhDHCPSnoopingTableVID = _SwhDHCPSnoopingTableVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1, 4),
    _SwhDHCPSnoopingTableVID_Type()
)
swhDHCPSnoopingTableVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableVID.setStatus("mandatory")
_SwhDHCPSnoopingTableCliIPAddr_Type = IpAddress
_SwhDHCPSnoopingTableCliIPAddr_Object = MibTableColumn
swhDHCPSnoopingTableCliIPAddr = _SwhDHCPSnoopingTableCliIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1, 5),
    _SwhDHCPSnoopingTableCliIPAddr_Type()
)
swhDHCPSnoopingTableCliIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableCliIPAddr.setStatus("mandatory")
_SwhDHCPSnoopingTableCliMacAddr_Type = MacAddress
_SwhDHCPSnoopingTableCliMacAddr_Object = MibTableColumn
swhDHCPSnoopingTableCliMacAddr = _SwhDHCPSnoopingTableCliMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1, 6),
    _SwhDHCPSnoopingTableCliMacAddr_Type()
)
swhDHCPSnoopingTableCliMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableCliMacAddr.setStatus("mandatory")
_SwhDHCPSnoopingTableSrvIPAddr_Type = IpAddress
_SwhDHCPSnoopingTableSrvIPAddr_Object = MibTableColumn
swhDHCPSnoopingTableSrvIPAddr = _SwhDHCPSnoopingTableSrvIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1, 7),
    _SwhDHCPSnoopingTableSrvIPAddr_Type()
)
swhDHCPSnoopingTableSrvIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableSrvIPAddr.setStatus("mandatory")
_SwhDHCPSnoopingTableTimeLeft_Type = DisplayString
_SwhDHCPSnoopingTableTimeLeft_Object = MibTableColumn
swhDHCPSnoopingTableTimeLeft = _SwhDHCPSnoopingTableTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 7, 1, 8),
    _SwhDHCPSnoopingTableTimeLeft_Type()
)
swhDHCPSnoopingTableTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPSnoopingTableTimeLeft.setStatus("mandatory")
_SwhDHCPv6SnoopingTableTable_Object = MibTable
swhDHCPv6SnoopingTableTable = _SwhDHCPv6SnoopingTableTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8)
)
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableTable.setStatus("mandatory")
_SwhDHCPv6SnoopingTableEntry_Object = MibTableRow
swhDHCPv6SnoopingTableEntry = _SwhDHCPv6SnoopingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1)
)
swhDHCPv6SnoopingTableEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDHCPv6SnoopingTableIndex"),
)
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableEntry.setStatus("mandatory")


class _SwhDHCPv6SnoopingTableIndex_Type(Integer32):
    """Custom type swhDHCPv6SnoopingTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDHCPv6SnoopingTableIndex_Type.__name__ = "Integer32"
_SwhDHCPv6SnoopingTableIndex_Object = MibTableColumn
swhDHCPv6SnoopingTableIndex = _SwhDHCPv6SnoopingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1, 1),
    _SwhDHCPv6SnoopingTableIndex_Type()
)
swhDHCPv6SnoopingTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableIndex.setStatus("mandatory")
_SwhDHCPv6SnoopingTableCliPort_Type = Integer32
_SwhDHCPv6SnoopingTableCliPort_Object = MibTableColumn
swhDHCPv6SnoopingTableCliPort = _SwhDHCPv6SnoopingTableCliPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1, 2),
    _SwhDHCPv6SnoopingTableCliPort_Type()
)
swhDHCPv6SnoopingTableCliPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableCliPort.setStatus("mandatory")
_SwhDHCPv6SnoopingTableSrvPort_Type = Integer32
_SwhDHCPv6SnoopingTableSrvPort_Object = MibTableColumn
swhDHCPv6SnoopingTableSrvPort = _SwhDHCPv6SnoopingTableSrvPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1, 3),
    _SwhDHCPv6SnoopingTableSrvPort_Type()
)
swhDHCPv6SnoopingTableSrvPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableSrvPort.setStatus("mandatory")
_SwhDHCPv6SnoopingTableVID_Type = Integer32
_SwhDHCPv6SnoopingTableVID_Object = MibTableColumn
swhDHCPv6SnoopingTableVID = _SwhDHCPv6SnoopingTableVID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1, 4),
    _SwhDHCPv6SnoopingTableVID_Type()
)
swhDHCPv6SnoopingTableVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableVID.setStatus("mandatory")
_SwhDHCPv6SnoopingTableCliIPAddr_Type = DisplayString
_SwhDHCPv6SnoopingTableCliIPAddr_Object = MibTableColumn
swhDHCPv6SnoopingTableCliIPAddr = _SwhDHCPv6SnoopingTableCliIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1, 5),
    _SwhDHCPv6SnoopingTableCliIPAddr_Type()
)
swhDHCPv6SnoopingTableCliIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableCliIPAddr.setStatus("mandatory")
_SwhDHCPv6SnoopingTableCliMacAddr_Type = MacAddress
_SwhDHCPv6SnoopingTableCliMacAddr_Object = MibTableColumn
swhDHCPv6SnoopingTableCliMacAddr = _SwhDHCPv6SnoopingTableCliMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1, 6),
    _SwhDHCPv6SnoopingTableCliMacAddr_Type()
)
swhDHCPv6SnoopingTableCliMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableCliMacAddr.setStatus("mandatory")
_SwhDHCPv6SnoopingTableSrvIPAddr_Type = DisplayString
_SwhDHCPv6SnoopingTableSrvIPAddr_Object = MibTableColumn
swhDHCPv6SnoopingTableSrvIPAddr = _SwhDHCPv6SnoopingTableSrvIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1, 7),
    _SwhDHCPv6SnoopingTableSrvIPAddr_Type()
)
swhDHCPv6SnoopingTableSrvIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableSrvIPAddr.setStatus("mandatory")
_SwhDHCPv6SnoopingTableTimeLeft_Type = DisplayString
_SwhDHCPv6SnoopingTableTimeLeft_Object = MibTableColumn
swhDHCPv6SnoopingTableTimeLeft = _SwhDHCPv6SnoopingTableTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 35, 8, 1, 8),
    _SwhDHCPv6SnoopingTableTimeLeft_Type()
)
swhDHCPv6SnoopingTableTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDHCPv6SnoopingTableTimeLeft.setStatus("mandatory")
_SwhLoopDetectionStatus_ObjectIdentity = ObjectIdentity
swhLoopDetectionStatus = _SwhLoopDetectionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 36)
)


class _SwhLoopDetectionStatusUpdate_Type(Integer32):
    """Custom type swhLoopDetectionStatusUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("update", 1))
    )


_SwhLoopDetectionStatusUpdate_Type.__name__ = "Integer32"
_SwhLoopDetectionStatusUpdate_Object = MibScalar
swhLoopDetectionStatusUpdate = _SwhLoopDetectionStatusUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 36, 2),
    _SwhLoopDetectionStatusUpdate_Type()
)
swhLoopDetectionStatusUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoopDetectionStatusUpdate.setStatus("mandatory")
_SwhLoopDetectionStatusTable_Object = MibTable
swhLoopDetectionStatusTable = _SwhLoopDetectionStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 36, 4)
)
if mibBuilder.loadTexts:
    swhLoopDetectionStatusTable.setStatus("mandatory")
_SwhLoopDetectionStatusEntry_Object = MibTableRow
swhLoopDetectionStatusEntry = _SwhLoopDetectionStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 36, 4, 1)
)
swhLoopDetectionStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhLoopDetectionStatusPort"),
)
if mibBuilder.loadTexts:
    swhLoopDetectionStatusEntry.setStatus("mandatory")


class _SwhLoopDetectionStatusPort_Type(Integer32):
    """Custom type swhLoopDetectionStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhLoopDetectionStatusPort_Type.__name__ = "Integer32"
_SwhLoopDetectionStatusPort_Object = MibTableColumn
swhLoopDetectionStatusPort = _SwhLoopDetectionStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 36, 4, 1, 1),
    _SwhLoopDetectionStatusPort_Type()
)
swhLoopDetectionStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhLoopDetectionStatusPort.setStatus("mandatory")
_SwhLoopDetectionStatusLockCause_Type = DisplayString
_SwhLoopDetectionStatusLockCause_Object = MibTableColumn
swhLoopDetectionStatusLockCause = _SwhLoopDetectionStatusLockCause_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 36, 4, 1, 3),
    _SwhLoopDetectionStatusLockCause_Type()
)
swhLoopDetectionStatusLockCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLoopDetectionStatusLockCause.setStatus("mandatory")


class _SwhLoopDetectionStatusStatus_Type(Integer32):
    """Custom type swhLoopDetectionStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("un-lock", 0),
          ("lock", 1))
    )


_SwhLoopDetectionStatusStatus_Type.__name__ = "Integer32"
_SwhLoopDetectionStatusStatus_Object = MibTableColumn
swhLoopDetectionStatusStatus = _SwhLoopDetectionStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 36, 4, 1, 4),
    _SwhLoopDetectionStatusStatus_Type()
)
swhLoopDetectionStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhLoopDetectionStatusStatus.setStatus("mandatory")
_SwhMacLimitersStatus_ObjectIdentity = ObjectIdentity
swhMacLimitersStatus = _SwhMacLimitersStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 39)
)
_SwhMacLimitersStatusTable_Object = MibTable
swhMacLimitersStatusTable = _SwhMacLimitersStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 39, 1)
)
if mibBuilder.loadTexts:
    swhMacLimitersStatusTable.setStatus("mandatory")
_SwhMacLimitersStatusEntry_Object = MibTableRow
swhMacLimitersStatusEntry = _SwhMacLimitersStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 39, 1, 1)
)
swhMacLimitersStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhMacLimitersStatusPort"),
)
if mibBuilder.loadTexts:
    swhMacLimitersStatusEntry.setStatus("mandatory")


class _SwhMacLimitersStatusPort_Type(Integer32):
    """Custom type swhMacLimitersStatusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhMacLimitersStatusPort_Type.__name__ = "Integer32"
_SwhMacLimitersStatusPort_Object = MibTableColumn
swhMacLimitersStatusPort = _SwhMacLimitersStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 39, 1, 1, 1),
    _SwhMacLimitersStatusPort_Type()
)
swhMacLimitersStatusPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhMacLimitersStatusPort.setStatus("mandatory")


class _SwhMacLimitersStatusLimit_Type(Integer32):
    """Custom type swhMacLimitersStatusLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("na", -1)
    )


_SwhMacLimitersStatusLimit_Type.__name__ = "Integer32"
_SwhMacLimitersStatusLimit_Object = MibTableColumn
swhMacLimitersStatusLimit = _SwhMacLimitersStatusLimit_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 39, 1, 1, 2),
    _SwhMacLimitersStatusLimit_Type()
)
swhMacLimitersStatusLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacLimitersStatusLimit.setStatus("mandatory")


class _SwhMacLimitersStatusCurrent_Type(Integer32):
    """Custom type swhMacLimitersStatusCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            -1
        )
    )
    namedValues = NamedValues(
        ("na", -1)
    )


_SwhMacLimitersStatusCurrent_Type.__name__ = "Integer32"
_SwhMacLimitersStatusCurrent_Object = MibTableColumn
swhMacLimitersStatusCurrent = _SwhMacLimitersStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 39, 1, 1, 3),
    _SwhMacLimitersStatusCurrent_Type()
)
swhMacLimitersStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhMacLimitersStatusCurrent.setStatus("mandatory")
_SwhDIDOStatus_ObjectIdentity = ObjectIdentity
swhDIDOStatus = _SwhDIDOStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41)
)
_SwhDIStatusTable_Object = MibTable
swhDIStatusTable = _SwhDIStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 1)
)
if mibBuilder.loadTexts:
    swhDIStatusTable.setStatus("mandatory")
_SwhDIStatusEntry_Object = MibTableRow
swhDIStatusEntry = _SwhDIStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 1, 1)
)
swhDIStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDIStatusIndex"),
)
if mibBuilder.loadTexts:
    swhDIStatusEntry.setStatus("mandatory")


class _SwhDIStatusIndex_Type(Integer32):
    """Custom type swhDIStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDIStatusIndex_Type.__name__ = "Integer32"
_SwhDIStatusIndex_Object = MibTableColumn
swhDIStatusIndex = _SwhDIStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 1, 1, 1),
    _SwhDIStatusIndex_Type()
)
swhDIStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDIStatusIndex.setStatus("mandatory")


class _SwhDIStatusStatus_Type(Integer32):
    """Custom type swhDIStatusStatus based on Integer32"""
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


_SwhDIStatusStatus_Type.__name__ = "Integer32"
_SwhDIStatusStatus_Object = MibTableColumn
swhDIStatusStatus = _SwhDIStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 1, 1, 3),
    _SwhDIStatusStatus_Type()
)
swhDIStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDIStatusStatus.setStatus("mandatory")


class _SwhDIStatusAlarm_Type(Integer32):
    """Custom type swhDIStatusAlarm based on Integer32"""
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


_SwhDIStatusAlarm_Type.__name__ = "Integer32"
_SwhDIStatusAlarm_Object = MibTableColumn
swhDIStatusAlarm = _SwhDIStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 1, 1, 4),
    _SwhDIStatusAlarm_Type()
)
swhDIStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDIStatusAlarm.setStatus("mandatory")
_SwhDOStatusTable_Object = MibTable
swhDOStatusTable = _SwhDOStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2)
)
if mibBuilder.loadTexts:
    swhDOStatusTable.setStatus("mandatory")
_SwhDOStatusEntry_Object = MibTableRow
swhDOStatusEntry = _SwhDOStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2, 1)
)
swhDOStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDOStatusIndex"),
)
if mibBuilder.loadTexts:
    swhDOStatusEntry.setStatus("mandatory")


class _SwhDOStatusIndex_Type(Integer32):
    """Custom type swhDOStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDOStatusIndex_Type.__name__ = "Integer32"
_SwhDOStatusIndex_Object = MibTableColumn
swhDOStatusIndex = _SwhDOStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2, 1, 1),
    _SwhDOStatusIndex_Type()
)
swhDOStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDOStatusIndex.setStatus("mandatory")


class _SwhDOStatusStatus_Type(Integer32):
    """Custom type swhDOStatusStatus based on Integer32"""
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


_SwhDOStatusStatus_Type.__name__ = "Integer32"
_SwhDOStatusStatus_Object = MibTableColumn
swhDOStatusStatus = _SwhDOStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2, 1, 3),
    _SwhDOStatusStatus_Type()
)
swhDOStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDOStatusStatus.setStatus("mandatory")


class _SwhDOStatusAlarm_Type(Integer32):
    """Custom type swhDOStatusAlarm based on Integer32"""
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


_SwhDOStatusAlarm_Type.__name__ = "Integer32"
_SwhDOStatusAlarm_Object = MibTableColumn
swhDOStatusAlarm = _SwhDOStatusAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2, 1, 4),
    _SwhDOStatusAlarm_Type()
)
swhDOStatusAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDOStatusAlarm.setStatus("mandatory")


class _SwhDOStatusTrigger_Type(Integer32):
    """Custom type swhDOStatusTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhDOStatusTrigger_Type.__name__ = "Integer32"
_SwhDOStatusTrigger_Object = MibTableColumn
swhDOStatusTrigger = _SwhDOStatusTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2, 1, 5),
    _SwhDOStatusTrigger_Type()
)
swhDOStatusTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDOStatusTrigger.setStatus("mandatory")


class _SwhDOStatusDigitalInput1_Type(Integer32):
    """Custom type swhDOStatusDigitalInput1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("off", 0),
          ("on", 1))
    )


_SwhDOStatusDigitalInput1_Type.__name__ = "Integer32"
_SwhDOStatusDigitalInput1_Object = MibTableColumn
swhDOStatusDigitalInput1 = _SwhDOStatusDigitalInput1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2, 1, 6),
    _SwhDOStatusDigitalInput1_Type()
)
swhDOStatusDigitalInput1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDOStatusDigitalInput1.setStatus("mandatory")


class _SwhDOStatusPower1_Type(Integer32):
    """Custom type swhDOStatusPower1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("off", 0),
          ("on", 1))
    )


_SwhDOStatusPower1_Type.__name__ = "Integer32"
_SwhDOStatusPower1_Object = MibTableColumn
swhDOStatusPower1 = _SwhDOStatusPower1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2, 1, 8),
    _SwhDOStatusPower1_Type()
)
swhDOStatusPower1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDOStatusPower1.setStatus("mandatory")


class _SwhDOStatusPower2_Type(Integer32):
    """Custom type swhDOStatusPower2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("off", 0),
          ("on", 1))
    )


_SwhDOStatusPower2_Type.__name__ = "Integer32"
_SwhDOStatusPower2_Object = MibTableColumn
swhDOStatusPower2 = _SwhDOStatusPower2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 2, 1, 9),
    _SwhDOStatusPower2_Type()
)
swhDOStatusPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDOStatusPower2.setStatus("mandatory")
_SwhDOPortStatusTable_Object = MibTable
swhDOPortStatusTable = _SwhDOPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 3)
)
if mibBuilder.loadTexts:
    swhDOPortStatusTable.setStatus("mandatory")
_SwhDOPortStatusEntry_Object = MibTableRow
swhDOPortStatusEntry = _SwhDOPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 3, 1)
)
swhDOPortStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhDOPortStatusIndex"),
)
if mibBuilder.loadTexts:
    swhDOPortStatusEntry.setStatus("mandatory")


class _SwhDOPortStatusIndex_Type(Integer32):
    """Custom type swhDOPortStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhDOPortStatusIndex_Type.__name__ = "Integer32"
_SwhDOPortStatusIndex_Object = MibTableColumn
swhDOPortStatusIndex = _SwhDOPortStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 3, 1, 1),
    _SwhDOPortStatusIndex_Type()
)
swhDOPortStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhDOPortStatusIndex.setStatus("mandatory")


class _SwhDOPortStatusDigitalOutput1Status_Type(Integer32):
    """Custom type swhDOPortStatusDigitalOutput1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("off", 0),
          ("on", 1))
    )


_SwhDOPortStatusDigitalOutput1Status_Type.__name__ = "Integer32"
_SwhDOPortStatusDigitalOutput1Status_Object = MibTableColumn
swhDOPortStatusDigitalOutput1Status = _SwhDOPortStatusDigitalOutput1Status_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 41, 3, 1, 2),
    _SwhDOPortStatusDigitalOutput1Status_Type()
)
swhDOPortStatusDigitalOutput1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhDOPortStatusDigitalOutput1Status.setStatus("mandatory")
_SwhRingStatus_ObjectIdentity = ObjectIdentity
swhRingStatus = _SwhRingStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43)
)


class _SwhRingState_Type(Integer32):
    """Custom type swhRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhRingState_Type.__name__ = "Integer32"
_SwhRingState_Object = MibScalar
swhRingState = _SwhRingState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43, 1),
    _SwhRingState_Type()
)
swhRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRingState.setStatus("mandatory")
_SwhRingStatusTable_Object = MibTable
swhRingStatusTable = _SwhRingStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43, 2)
)
if mibBuilder.loadTexts:
    swhRingStatusTable.setStatus("mandatory")
_SwhRingStatusEntry_Object = MibTableRow
swhRingStatusEntry = _SwhRingStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43, 2, 1)
)
swhRingStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhRingStatusIndex"),
)
if mibBuilder.loadTexts:
    swhRingStatusEntry.setStatus("mandatory")


class _SwhRingStatusIndex_Type(Integer32):
    """Custom type swhRingStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRingStatusIndex_Type.__name__ = "Integer32"
_SwhRingStatusIndex_Object = MibTableColumn
swhRingStatusIndex = _SwhRingStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43, 2, 1, 1),
    _SwhRingStatusIndex_Type()
)
swhRingStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhRingStatusIndex.setStatus("mandatory")


class _SwhRingStatusEnable_Type(Integer32):
    """Custom type swhRingStatusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhRingStatusEnable_Type.__name__ = "Integer32"
_SwhRingStatusEnable_Object = MibTableColumn
swhRingStatusEnable = _SwhRingStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43, 2, 1, 2),
    _SwhRingStatusEnable_Type()
)
swhRingStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRingStatusEnable.setStatus("mandatory")


class _SwhRingStatusState_Type(Integer32):
    """Custom type swhRingStatusState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("blocking", 0),
          ("forwarding", 1))
    )


_SwhRingStatusState_Type.__name__ = "Integer32"
_SwhRingStatusState_Object = MibTableColumn
swhRingStatusState = _SwhRingStatusState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43, 2, 1, 3),
    _SwhRingStatusState_Type()
)
swhRingStatusState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRingStatusState.setStatus("mandatory")


class _SwhRingStateAccording_Type(Integer32):
    """Custom type swhRingStateAccording based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("software", 0),
          ("hardware", 1))
    )


_SwhRingStateAccording_Type.__name__ = "Integer32"
_SwhRingStateAccording_Object = MibScalar
swhRingStateAccording = _SwhRingStateAccording_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43, 3),
    _SwhRingStateAccording_Type()
)
swhRingStateAccording.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRingStateAccording.setStatus("mandatory")


class _SwhRingStateRole_Type(Integer32):
    """Custom type swhRingStateRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("slave", 0),
          ("master", 1))
    )


_SwhRingStateRole_Type.__name__ = "Integer32"
_SwhRingStateRole_Object = MibScalar
swhRingStateRole = _SwhRingStateRole_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 43, 4),
    _SwhRingStateRole_Type()
)
swhRingStateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRingStateRole.setStatus("mandatory")
_SwhPOEStatus_ObjectIdentity = ObjectIdentity
swhPOEStatus = _SwhPOEStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48)
)
_SwhPOETotalPower_Type = DisplayString
_SwhPOETotalPower_Object = MibScalar
swhPOETotalPower = _SwhPOETotalPower_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 1),
    _SwhPOETotalPower_Type()
)
swhPOETotalPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOETotalPower.setStatus("mandatory")
_SwhPOEStatusTable_Object = MibTable
swhPOEStatusTable = _SwhPOEStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2)
)
if mibBuilder.loadTexts:
    swhPOEStatusTable.setStatus("mandatory")
_SwhPOEStatusEntry_Object = MibTableRow
swhPOEStatusEntry = _SwhPOEStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1)
)
swhPOEStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhPOEStatusIndex"),
)
if mibBuilder.loadTexts:
    swhPOEStatusEntry.setStatus("mandatory")


class _SwhPOEStatusIndex_Type(Integer32):
    """Custom type swhPOEStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhPOEStatusIndex_Type.__name__ = "Integer32"
_SwhPOEStatusIndex_Object = MibTableColumn
swhPOEStatusIndex = _SwhPOEStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 1),
    _SwhPOEStatusIndex_Type()
)
swhPOEStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhPOEStatusIndex.setStatus("mandatory")


class _SwhPOEStatusPort_Type(Integer32):
    """Custom type swhPOEStatusPort based on Integer32"""
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
        *(("port01", 0),
          ("port02", 1),
          ("port03", 2),
          ("port04", 3),
          ("port05", 4),
          ("port06", 5))
    )


_SwhPOEStatusPort_Type.__name__ = "Integer32"
_SwhPOEStatusPort_Object = MibTableColumn
swhPOEStatusPort = _SwhPOEStatusPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 2),
    _SwhPOEStatusPort_Type()
)
swhPOEStatusPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEStatusPort.setStatus("mandatory")


class _SwhPOEStatusName_Type(DisplayString):
    """Custom type swhPOEStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPOEStatusName_Type.__name__ = "DisplayString"
_SwhPOEStatusName_Object = MibTableColumn
swhPOEStatusName = _SwhPOEStatusName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 3),
    _SwhPOEStatusName_Type()
)
swhPOEStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEStatusName.setStatus("mandatory")


class _SwhPOEStatusPower_Type(DisplayString):
    """Custom type swhPOEStatusPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPOEStatusPower_Type.__name__ = "DisplayString"
_SwhPOEStatusPower_Object = MibTableColumn
swhPOEStatusPower = _SwhPOEStatusPower_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 4),
    _SwhPOEStatusPower_Type()
)
swhPOEStatusPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEStatusPower.setStatus("mandatory")


class _SwhPOEStatusVoltage_Type(DisplayString):
    """Custom type swhPOEStatusVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPOEStatusVoltage_Type.__name__ = "DisplayString"
_SwhPOEStatusVoltage_Object = MibTableColumn
swhPOEStatusVoltage = _SwhPOEStatusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 5),
    _SwhPOEStatusVoltage_Type()
)
swhPOEStatusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEStatusVoltage.setStatus("mandatory")


class _SwhPOEStatusCurrent_Type(DisplayString):
    """Custom type swhPOEStatusCurrent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPOEStatusCurrent_Type.__name__ = "DisplayString"
_SwhPOEStatusCurrent_Object = MibTableColumn
swhPOEStatusCurrent = _SwhPOEStatusCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 6),
    _SwhPOEStatusCurrent_Type()
)
swhPOEStatusCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEStatusCurrent.setStatus("mandatory")


class _SwhPOEStatusPDClass_Type(DisplayString):
    """Custom type swhPOEStatusPDClass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPOEStatusPDClass_Type.__name__ = "DisplayString"
_SwhPOEStatusPDClass_Object = MibTableColumn
swhPOEStatusPDClass = _SwhPOEStatusPDClass_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 7),
    _SwhPOEStatusPDClass_Type()
)
swhPOEStatusPDClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEStatusPDClass.setStatus("mandatory")


class _SwhPOEStatusPoEDetection_Type(DisplayString):
    """Custom type swhPOEStatusPoEDetection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhPOEStatusPoEDetection_Type.__name__ = "DisplayString"
_SwhPOEStatusPoEDetection_Object = MibTableColumn
swhPOEStatusPoEDetection = _SwhPOEStatusPoEDetection_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 8),
    _SwhPOEStatusPoEDetection_Type()
)
swhPOEStatusPoEDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEStatusPoEDetection.setStatus("mandatory")


class _SwhPOEStatusOperationMode_Type(Integer32):
    """Custom type swhPOEStatusOperationMode based on Integer32"""
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
        *(("shutdown", 0),
          ("injector-30watt", 1),
          ("auto-afat", 2),
          ("auto", 3),
          ("injector-60watt", 4))
    )


_SwhPOEStatusOperationMode_Type.__name__ = "Integer32"
_SwhPOEStatusOperationMode_Object = MibTableColumn
swhPOEStatusOperationMode = _SwhPOEStatusOperationMode_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 48, 2, 1, 9),
    _SwhPOEStatusOperationMode_Type()
)
swhPOEStatusOperationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhPOEStatusOperationMode.setStatus("mandatory")
_SwhCPUTemperatureStatus_ObjectIdentity = ObjectIdentity
swhCPUTemperatureStatus = _SwhCPUTemperatureStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51)
)


class _SwhCPUHighTemperatureThreshold_Type(Integer32):
    """Custom type swhCPUHighTemperatureThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhCPUHighTemperatureThreshold_Type.__name__ = "Integer32"
_SwhCPUHighTemperatureThreshold_Object = MibScalar
swhCPUHighTemperatureThreshold = _SwhCPUHighTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51, 1),
    _SwhCPUHighTemperatureThreshold_Type()
)
swhCPUHighTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhCPUHighTemperatureThreshold.setStatus("mandatory")


class _SwhCPUThresholdInterval_Type(Integer32):
    """Custom type swhCPUThresholdInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhCPUThresholdInterval_Type.__name__ = "Integer32"
_SwhCPUThresholdInterval_Object = MibScalar
swhCPUThresholdInterval = _SwhCPUThresholdInterval_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51, 2),
    _SwhCPUThresholdInterval_Type()
)
swhCPUThresholdInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhCPUThresholdInterval.setStatus("mandatory")


class _SwhCPUContinuousAlarm_Type(Integer32):
    """Custom type swhCPUContinuousAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhCPUContinuousAlarm_Type.__name__ = "Integer32"
_SwhCPUContinuousAlarm_Object = MibScalar
swhCPUContinuousAlarm = _SwhCPUContinuousAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51, 3),
    _SwhCPUContinuousAlarm_Type()
)
swhCPUContinuousAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhCPUContinuousAlarm.setStatus("mandatory")


class _SwhCPUCurrentCPUTemperature_Type(Integer32):
    """Custom type swhCPUCurrentCPUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SwhCPUCurrentCPUTemperature_Type.__name__ = "Integer32"
_SwhCPUCurrentCPUTemperature_Object = MibScalar
swhCPUCurrentCPUTemperature = _SwhCPUCurrentCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51, 5),
    _SwhCPUCurrentCPUTemperature_Type()
)
swhCPUCurrentCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCPUCurrentCPUTemperature.setStatus("mandatory")


class _SwhCPUHistoricalHighCPUTemperature_Type(Integer32):
    """Custom type swhCPUHistoricalHighCPUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SwhCPUHistoricalHighCPUTemperature_Type.__name__ = "Integer32"
_SwhCPUHistoricalHighCPUTemperature_Object = MibScalar
swhCPUHistoricalHighCPUTemperature = _SwhCPUHistoricalHighCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51, 6),
    _SwhCPUHistoricalHighCPUTemperature_Type()
)
swhCPUHistoricalHighCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCPUHistoricalHighCPUTemperature.setStatus("mandatory")


class _SwhCPUHistoricalHighElapsedTime_Type(DisplayString):
    """Custom type swhCPUHistoricalHighElapsedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhCPUHistoricalHighElapsedTime_Type.__name__ = "DisplayString"
_SwhCPUHistoricalHighElapsedTime_Object = MibScalar
swhCPUHistoricalHighElapsedTime = _SwhCPUHistoricalHighElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51, 7),
    _SwhCPUHistoricalHighElapsedTime_Type()
)
swhCPUHistoricalHighElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCPUHistoricalHighElapsedTime.setStatus("mandatory")


class _SwhCPUHistoricalLowCPUTemperature_Type(Integer32):
    """Custom type swhCPUHistoricalLowCPUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_SwhCPUHistoricalLowCPUTemperature_Type.__name__ = "Integer32"
_SwhCPUHistoricalLowCPUTemperature_Object = MibScalar
swhCPUHistoricalLowCPUTemperature = _SwhCPUHistoricalLowCPUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51, 8),
    _SwhCPUHistoricalLowCPUTemperature_Type()
)
swhCPUHistoricalLowCPUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCPUHistoricalLowCPUTemperature.setStatus("mandatory")


class _SwhCPUHistoricalLowElapsedTime_Type(DisplayString):
    """Custom type swhCPUHistoricalLowElapsedTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhCPUHistoricalLowElapsedTime_Type.__name__ = "DisplayString"
_SwhCPUHistoricalLowElapsedTime_Object = MibScalar
swhCPUHistoricalLowElapsedTime = _SwhCPUHistoricalLowElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 51, 9),
    _SwhCPUHistoricalLowElapsedTime_Type()
)
swhCPUHistoricalLowElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhCPUHistoricalLowElapsedTime.setStatus("mandatory")
_SwhFastRedundancyStatus_ObjectIdentity = ObjectIdentity
swhFastRedundancyStatus = _SwhFastRedundancyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52)
)
_SwhFastRedundancyStatusTable_Object = MibTable
swhFastRedundancyStatusTable = _SwhFastRedundancyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1)
)
if mibBuilder.loadTexts:
    swhFastRedundancyStatusTable.setStatus("mandatory")
_SwhFastRedundancyStatusEntry_Object = MibTableRow
swhFastRedundancyStatusEntry = _SwhFastRedundancyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1)
)
swhFastRedundancyStatusEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhFastRedundancyStatusIndex"),
)
if mibBuilder.loadTexts:
    swhFastRedundancyStatusEntry.setStatus("mandatory")


class _SwhFastRedundancyStatusIndex_Type(Integer32):
    """Custom type swhFastRedundancyStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhFastRedundancyStatusIndex_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusIndex_Object = MibTableColumn
swhFastRedundancyStatusIndex = _SwhFastRedundancyStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 1),
    _SwhFastRedundancyStatusIndex_Type()
)
swhFastRedundancyStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusIndex.setStatus("mandatory")


class _SwhFastRedundancyStatusGroupID_Type(Integer32):
    """Custom type swhFastRedundancyStatusGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("id-1", 1),
          ("id-2", 2))
    )


_SwhFastRedundancyStatusGroupID_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusGroupID_Object = MibTableColumn
swhFastRedundancyStatusGroupID = _SwhFastRedundancyStatusGroupID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 2),
    _SwhFastRedundancyStatusGroupID_Type()
)
swhFastRedundancyStatusGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusGroupID.setStatus("mandatory")
_SwhFastRedundancyStatusDescription_Type = DisplayString
_SwhFastRedundancyStatusDescription_Object = MibTableColumn
swhFastRedundancyStatusDescription = _SwhFastRedundancyStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 3),
    _SwhFastRedundancyStatusDescription_Type()
)
swhFastRedundancyStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusDescription.setStatus("mandatory")


class _SwhFastRedundancyStatusEnable_Type(Integer32):
    """Custom type swhFastRedundancyStatusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("disable", 0),
          ("enable", 1))
    )


_SwhFastRedundancyStatusEnable_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusEnable_Object = MibTableColumn
swhFastRedundancyStatusEnable = _SwhFastRedundancyStatusEnable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 4),
    _SwhFastRedundancyStatusEnable_Type()
)
swhFastRedundancyStatusEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusEnable.setStatus("mandatory")


class _SwhFastRedundancyStatusProtocol_Type(Integer32):
    """Custom type swhFastRedundancyStatusProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("fast-ringv2", 0),
          ("chain", 1))
    )


_SwhFastRedundancyStatusProtocol_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusProtocol_Object = MibTableColumn
swhFastRedundancyStatusProtocol = _SwhFastRedundancyStatusProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 5),
    _SwhFastRedundancyStatusProtocol_Type()
)
swhFastRedundancyStatusProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusProtocol.setStatus("mandatory")


class _SwhFastRedundancyStatusRole_Type(Integer32):
    """Custom type swhFastRedundancyStatusRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("slave", 0),
          ("master", 1))
    )


_SwhFastRedundancyStatusRole_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusRole_Object = MibTableColumn
swhFastRedundancyStatusRole = _SwhFastRedundancyStatusRole_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 6),
    _SwhFastRedundancyStatusRole_Type()
)
swhFastRedundancyStatusRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusRole.setStatus("mandatory")


class _SwhFastRedundancyStatusStatus_Type(Integer32):
    """Custom type swhFastRedundancyStatusStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("signal-fail", -2),
          ("na", -1),
          ("healthy", 0),
          ("break", 1))
    )


_SwhFastRedundancyStatusStatus_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusStatus_Object = MibTableColumn
swhFastRedundancyStatusStatus = _SwhFastRedundancyStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 7),
    _SwhFastRedundancyStatusStatus_Type()
)
swhFastRedundancyStatusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusStatus.setStatus("mandatory")


class _SwhFastRedundancyStatusPort1_Type(Integer32):
    """Custom type swhFastRedundancyStatusPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("port01", 1),
          ("port02", 2),
          ("port03", 3),
          ("port04", 4),
          ("port05", 5),
          ("port06", 6))
    )


_SwhFastRedundancyStatusPort1_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusPort1_Object = MibTableColumn
swhFastRedundancyStatusPort1 = _SwhFastRedundancyStatusPort1_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 8),
    _SwhFastRedundancyStatusPort1_Type()
)
swhFastRedundancyStatusPort1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusPort1.setStatus("mandatory")


class _SwhFastRedundancyStatusPort1Role_Type(Integer32):
    """Custom type swhFastRedundancyStatusPort1Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("member", 0),
          ("head", 1),
          ("tail", 2))
    )


_SwhFastRedundancyStatusPort1Role_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusPort1Role_Object = MibTableColumn
swhFastRedundancyStatusPort1Role = _SwhFastRedundancyStatusPort1Role_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 9),
    _SwhFastRedundancyStatusPort1Role_Type()
)
swhFastRedundancyStatusPort1Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusPort1Role.setStatus("mandatory")


class _SwhFastRedundancyStatusPort1Statue_Type(Integer32):
    """Custom type swhFastRedundancyStatusPort1Statue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("blocked", 1),
          ("forwarding", 4),
          ("link-down", 5))
    )


_SwhFastRedundancyStatusPort1Statue_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusPort1Statue_Object = MibTableColumn
swhFastRedundancyStatusPort1Statue = _SwhFastRedundancyStatusPort1Statue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 10),
    _SwhFastRedundancyStatusPort1Statue_Type()
)
swhFastRedundancyStatusPort1Statue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusPort1Statue.setStatus("mandatory")


class _SwhFastRedundancyStatusPort2_Type(Integer32):
    """Custom type swhFastRedundancyStatusPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("port01", 1),
          ("port02", 2),
          ("port03", 3),
          ("port04", 4),
          ("port05", 5),
          ("port06", 6))
    )


_SwhFastRedundancyStatusPort2_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusPort2_Object = MibTableColumn
swhFastRedundancyStatusPort2 = _SwhFastRedundancyStatusPort2_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 11),
    _SwhFastRedundancyStatusPort2_Type()
)
swhFastRedundancyStatusPort2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusPort2.setStatus("mandatory")


class _SwhFastRedundancyStatusPort2Role_Type(Integer32):
    """Custom type swhFastRedundancyStatusPort2Role based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("member", 0),
          ("head", 1),
          ("tail", 2))
    )


_SwhFastRedundancyStatusPort2Role_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusPort2Role_Object = MibTableColumn
swhFastRedundancyStatusPort2Role = _SwhFastRedundancyStatusPort2Role_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 12),
    _SwhFastRedundancyStatusPort2Role_Type()
)
swhFastRedundancyStatusPort2Role.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusPort2Role.setStatus("mandatory")


class _SwhFastRedundancyStatusPort2Statue_Type(Integer32):
    """Custom type swhFastRedundancyStatusPort2Statue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("na2", -2),
          ("na", -1),
          ("blocked", 1),
          ("forwarding", 4),
          ("link-down", 5))
    )


_SwhFastRedundancyStatusPort2Statue_Type.__name__ = "Integer32"
_SwhFastRedundancyStatusPort2Statue_Object = MibTableColumn
swhFastRedundancyStatusPort2Statue = _SwhFastRedundancyStatusPort2Statue_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 1, 1, 13),
    _SwhFastRedundancyStatusPort2Statue_Type()
)
swhFastRedundancyStatusPort2Statue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyStatusPort2Statue.setStatus("mandatory")


class _SwhRingStatusTimes_Type(Integer32):
    """Custom type swhRingStatusTimes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhRingStatusTimes_Type.__name__ = "Integer32"
_SwhRingStatusTimes_Object = MibScalar
swhRingStatusTimes = _SwhRingStatusTimes_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 2),
    _SwhRingStatusTimes_Type()
)
swhRingStatusTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRingStatusTimes.setStatus("mandatory")
_SwhRingStatusLastChangeTime_Type = DisplayString
_SwhRingStatusLastChangeTime_Object = MibScalar
swhRingStatusLastChangeTime = _SwhRingStatusLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 3),
    _SwhRingStatusLastChangeTime_Type()
)
swhRingStatusLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRingStatusLastChangeTime.setStatus("mandatory")
_SwhRingStatusElapsedTime_Type = DisplayString
_SwhRingStatusElapsedTime_Object = MibScalar
swhRingStatusElapsedTime = _SwhRingStatusElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 4),
    _SwhRingStatusElapsedTime_Type()
)
swhRingStatusElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhRingStatusElapsedTime.setStatus("mandatory")


class _SwhRingStatusTopologyClear_Type(Integer32):
    """Custom type swhRingStatusTopologyClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhRingStatusTopologyClear_Type.__name__ = "Integer32"
_SwhRingStatusTopologyClear_Object = MibScalar
swhRingStatusTopologyClear = _SwhRingStatusTopologyClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 5),
    _SwhRingStatusTopologyClear_Type()
)
swhRingStatusTopologyClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhRingStatusTopologyClear.setStatus("mandatory")
_SwhFastRedundancyStatisticsTable_Object = MibTable
swhFastRedundancyStatisticsTable = _SwhFastRedundancyStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 6)
)
if mibBuilder.loadTexts:
    swhFastRedundancyStatisticsTable.setStatus("mandatory")
_SwhFastRedundancyStatisticsEntry_Object = MibTableRow
swhFastRedundancyStatisticsEntry = _SwhFastRedundancyStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 6, 1)
)
swhFastRedundancyStatisticsEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhFastRedundancyEntry"),
)
if mibBuilder.loadTexts:
    swhFastRedundancyStatisticsEntry.setStatus("mandatory")


class _SwhFastRedundancyEntry_Type(Integer32):
    """Custom type swhFastRedundancyEntry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhFastRedundancyEntry_Type.__name__ = "Integer32"
_SwhFastRedundancyEntry_Object = MibTableColumn
swhFastRedundancyEntry = _SwhFastRedundancyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 6, 1, 1),
    _SwhFastRedundancyEntry_Type()
)
swhFastRedundancyEntry.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhFastRedundancyEntry.setStatus("mandatory")
_SwhFastRedundancyTxNormal_Type = Counter32
_SwhFastRedundancyTxNormal_Object = MibTableColumn
swhFastRedundancyTxNormal = _SwhFastRedundancyTxNormal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 6, 1, 2),
    _SwhFastRedundancyTxNormal_Type()
)
swhFastRedundancyTxNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyTxNormal.setStatus("mandatory")
_SwhFastRedundancyTxFailure_Type = Counter32
_SwhFastRedundancyTxFailure_Object = MibTableColumn
swhFastRedundancyTxFailure = _SwhFastRedundancyTxFailure_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 6, 1, 3),
    _SwhFastRedundancyTxFailure_Type()
)
swhFastRedundancyTxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyTxFailure.setStatus("mandatory")
_SwhFastRedundancyRxNormal_Type = Counter32
_SwhFastRedundancyRxNormal_Object = MibTableColumn
swhFastRedundancyRxNormal = _SwhFastRedundancyRxNormal_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 6, 1, 4),
    _SwhFastRedundancyRxNormal_Type()
)
swhFastRedundancyRxNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyRxNormal.setStatus("mandatory")
_SwhFastRedundancyRxFailure_Type = Counter32
_SwhFastRedundancyRxFailure_Object = MibTableColumn
swhFastRedundancyRxFailure = _SwhFastRedundancyRxFailure_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 6, 1, 5),
    _SwhFastRedundancyRxFailure_Type()
)
swhFastRedundancyRxFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhFastRedundancyRxFailure.setStatus("mandatory")


class _SwhFastRedundancyCountersClear_Type(Integer32):
    """Custom type swhFastRedundancyCountersClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhFastRedundancyCountersClear_Type.__name__ = "Integer32"
_SwhFastRedundancyCountersClear_Object = MibTableColumn
swhFastRedundancyCountersClear = _SwhFastRedundancyCountersClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 5, 52, 6, 1, 6),
    _SwhFastRedundancyCountersClear_Type()
)
swhFastRedundancyCountersClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhFastRedundancyCountersClear.setStatus("mandatory")
_SwhSystemUtility_ObjectIdentity = ObjectIdentity
swhSystemUtility = _SwhSystemUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6)
)


class _SwhLoadFactorySetting_Type(Integer32):
    """Custom type swhLoadFactorySetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("load", 1))
    )


_SwhLoadFactorySetting_Type.__name__ = "Integer32"
_SwhLoadFactorySetting_Object = MibScalar
swhLoadFactorySetting = _SwhLoadFactorySetting_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 1),
    _SwhLoadFactorySetting_Type()
)
swhLoadFactorySetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoadFactorySetting.setStatus("mandatory")


class _SwhLoadFactorySettingExceptNetworkConfiguration_Type(Integer32):
    """Custom type swhLoadFactorySettingExceptNetworkConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("load", 1))
    )


_SwhLoadFactorySettingExceptNetworkConfiguration_Type.__name__ = "Integer32"
_SwhLoadFactorySettingExceptNetworkConfiguration_Object = MibScalar
swhLoadFactorySettingExceptNetworkConfiguration = _SwhLoadFactorySettingExceptNetworkConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 2),
    _SwhLoadFactorySettingExceptNetworkConfiguration_Type()
)
swhLoadFactorySettingExceptNetworkConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhLoadFactorySettingExceptNetworkConfiguration.setStatus("mandatory")
_SwhEventLog_ObjectIdentity = ObjectIdentity
swhEventLog = _SwhEventLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3)
)
_SwhEventLogTable_Object = MibTable
swhEventLogTable = _SwhEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1)
)
if mibBuilder.loadTexts:
    swhEventLogTable.setStatus("mandatory")
_SwhEventLogEntry_Object = MibTableRow
swhEventLogEntry = _SwhEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1)
)
swhEventLogEntry.setIndexNames(
    (0, "IPS-3106-SE-PB-MIB", "swhEventLogIndex"),
)
if mibBuilder.loadTexts:
    swhEventLogEntry.setStatus("mandatory")


class _SwhEventLogIndex_Type(Integer32):
    """Custom type swhEventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SwhEventLogIndex_Type.__name__ = "Integer32"
_SwhEventLogIndex_Object = MibTableColumn
swhEventLogIndex = _SwhEventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 1),
    _SwhEventLogIndex_Type()
)
swhEventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swhEventLogIndex.setStatus("mandatory")


class _SwhEventLogType_Type(Integer32):
    """Custom type swhEventLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1000,
              2000,
              3000)
        )
    )
    namedValues = NamedValues(
        *(("error", 1000),
          ("warning", 2000),
          ("information", 3000))
    )


_SwhEventLogType_Type.__name__ = "Integer32"
_SwhEventLogType_Object = MibTableColumn
swhEventLogType = _SwhEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 2),
    _SwhEventLogType_Type()
)
swhEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhEventLogType.setStatus("mandatory")
_SwhEventLogTime_Type = DisplayString
_SwhEventLogTime_Object = MibTableColumn
swhEventLogTime = _SwhEventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 3),
    _SwhEventLogTime_Type()
)
swhEventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhEventLogTime.setStatus("mandatory")
_SwhEventLogUpTime_Type = DisplayString
_SwhEventLogUpTime_Object = MibTableColumn
swhEventLogUpTime = _SwhEventLogUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 4),
    _SwhEventLogUpTime_Type()
)
swhEventLogUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhEventLogUpTime.setStatus("mandatory")
_SwhEventLogDescription_Type = DisplayString
_SwhEventLogDescription_Object = MibTableColumn
swhEventLogDescription = _SwhEventLogDescription_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 5),
    _SwhEventLogDescription_Type()
)
swhEventLogDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhEventLogDescription.setStatus("mandatory")


class _SwhEventLogSource_Type(Integer32):
    """Custom type swhEventLogSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4000,
              4001,
              4002,
              4003,
              4004,
              4005,
              4006,
              4007,
              4008,
              4009,
              4010,
              4011,
              4012,
              4013,
              4014,
              4015,
              4016,
              4020)
        )
    )
    namedValues = NamedValues(
        *(("local-machine", 4000),
          ("rs232d", 4001),
          ("rs232", 4002),
          ("telnetd", 4003),
          ("telnet", 4004),
          ("tftpd", 4005),
          ("tftp", 4006),
          ("ftpd", 4007),
          ("ftp", 4008),
          ("snmpd", 4009),
          ("snmp", 4010),
          ("webd", 4011),
          ("web", 4012),
          ("ping", 4013),
          ("watch-dog", 4014),
          ("remote-machine", 4015),
          ("catv-module", 4016),
          ("ssh", 4020))
    )


_SwhEventLogSource_Type.__name__ = "Integer32"
_SwhEventLogSource_Object = MibTableColumn
swhEventLogSource = _SwhEventLogSource_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 6),
    _SwhEventLogSource_Type()
)
swhEventLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhEventLogSource.setStatus("mandatory")


class _SwhEventLogEvent_Type(Integer32):
    """Custom type swhEventLogEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1001,
              1002,
              1003,
              1004,
              1005,
              2001,
              2002,
              2003,
              2004,
              2005,
              2006,
              2007,
              2008,
              2009,
              2010,
              2011,
              2012,
              2013,
              2021,
              2025,
              2026,
              2027,
              2028,
              3001,
              3002,
              3003,
              3004,
              3005,
              3006,
              3007,
              3008,
              3011,
              3020,
              3022,
              3023,
              3026,
              3027,
              3038)
        )
    )
    namedValues = NamedValues(
        *(("boot-failed", 1001),
          ("load-config-failed", 1002),
          ("load-default-config-failed", 1003),
          ("save-config-failed", 1004),
          ("save-default-config-failed", 1005),
          ("login-failed", 2001),
          ("module-down", 2002),
          ("module-power-down", 2003),
          ("power-module-down", 2004),
          ("power-fan-failed", 2005),
          ("backup-config-failed", 2006),
          ("auto-provision", 2007),
          ("fan-failed", 2008),
          ("temperature-abnormality", 2009),
          ("voltage-abnormality", 2010),
          ("tx-bias-abnormality", 2011),
          ("loop", 2012),
          ("upgrade", 2013),
          ("missing", 2021),
          ("mac-limiters", 2025),
          ("storm-control", 2026),
          ("cpu-temperature-overheat", 2027),
          ("cpu-temperature-failed", 2028),
          ("cold-start", 3001),
          ("warm-start", 3002),
          ("login", 3003),
          ("logout", 3004),
          ("timeout", 3005),
          ("disconnected", 3006),
          ("link-up", 3007),
          ("link-down", 3008),
          ("power-supply-up", 3011),
          ("backup-config-succeeded", 3020),
          ("fan-ok", 3022),
          ("temperature-normality", 3023),
          ("digital-input", 3026),
          ("digital-output", 3027),
          ("cpu-temperature-normal", 3038))
    )


_SwhEventLogEvent_Type.__name__ = "Integer32"
_SwhEventLogEvent_Object = MibTableColumn
swhEventLogEvent = _SwhEventLogEvent_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 7),
    _SwhEventLogEvent_Type()
)
swhEventLogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhEventLogEvent.setStatus("mandatory")
_SwhEventLogNameCommunity_Type = DisplayString
_SwhEventLogNameCommunity_Object = MibTableColumn
swhEventLogNameCommunity = _SwhEventLogNameCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 8),
    _SwhEventLogNameCommunity_Type()
)
swhEventLogNameCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhEventLogNameCommunity.setStatus("mandatory")
_SwhEventLogIPAddr_Type = DisplayString
_SwhEventLogIPAddr_Object = MibTableColumn
swhEventLogIPAddr = _SwhEventLogIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 1, 1, 9),
    _SwhEventLogIPAddr_Type()
)
swhEventLogIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhEventLogIPAddr.setStatus("mandatory")


class _SwhEventLogClear_Type(Integer32):
    """Custom type swhEventLogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("clear", 1))
    )


_SwhEventLogClear_Type.__name__ = "Integer32"
_SwhEventLogClear_Object = MibScalar
swhEventLogClear = _SwhEventLogClear_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 3, 2),
    _SwhEventLogClear_Type()
)
swhEventLogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhEventLogClear.setStatus("mandatory")
_SwhUpdateFirmware_ObjectIdentity = ObjectIdentity
swhUpdateFirmware = _SwhUpdateFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4)
)


class _SwhUpdateProtocol_Type(Integer32):
    """Custom type swhUpdateProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 0),
          ("ftp", 1))
    )


_SwhUpdateProtocol_Type.__name__ = "Integer32"
_SwhUpdateProtocol_Object = MibScalar
swhUpdateProtocol = _SwhUpdateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 1),
    _SwhUpdateProtocol_Type()
)
swhUpdateProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateProtocol.setStatus("mandatory")


class _SwhUpdateFileType_Type(Integer32):
    """Custom type swhUpdateFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("firmware", 0),
          ("configuration", 1))
    )


_SwhUpdateFileType_Type.__name__ = "Integer32"
_SwhUpdateFileType_Object = MibScalar
swhUpdateFileType = _SwhUpdateFileType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 2),
    _SwhUpdateFileType_Type()
)
swhUpdateFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateFileType.setStatus("mandatory")
_SwhUpdateServerIPAddr_Type = IpAddress
_SwhUpdateServerIPAddr_Object = MibScalar
swhUpdateServerIPAddr = _SwhUpdateServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 3),
    _SwhUpdateServerIPAddr_Type()
)
swhUpdateServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateServerIPAddr.setStatus("mandatory")


class _SwhUpdateUserName_Type(DisplayString):
    """Custom type swhUpdateUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhUpdateUserName_Type.__name__ = "DisplayString"
_SwhUpdateUserName_Object = MibScalar
swhUpdateUserName = _SwhUpdateUserName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 4),
    _SwhUpdateUserName_Type()
)
swhUpdateUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateUserName.setStatus("mandatory")


class _SwhUpdatePassword_Type(DisplayString):
    """Custom type swhUpdatePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhUpdatePassword_Type.__name__ = "DisplayString"
_SwhUpdatePassword_Object = MibScalar
swhUpdatePassword = _SwhUpdatePassword_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 5),
    _SwhUpdatePassword_Type()
)
swhUpdatePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdatePassword.setStatus("mandatory")


class _SwhUpdateFileLocation_Type(DisplayString):
    """Custom type swhUpdateFileLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhUpdateFileLocation_Type.__name__ = "DisplayString"
_SwhUpdateFileLocation_Object = MibScalar
swhUpdateFileLocation = _SwhUpdateFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 6),
    _SwhUpdateFileLocation_Type()
)
swhUpdateFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateFileLocation.setStatus("mandatory")


class _SwhUpdatePut_Type(Integer32):
    """Custom type swhUpdatePut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("put", 1))
    )


_SwhUpdatePut_Type.__name__ = "Integer32"
_SwhUpdatePut_Object = MibScalar
swhUpdatePut = _SwhUpdatePut_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 8),
    _SwhUpdatePut_Type()
)
swhUpdatePut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdatePut.setStatus("mandatory")


class _SwhUpdateUpdate_Type(Integer32):
    """Custom type swhUpdateUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("update", 1))
    )


_SwhUpdateUpdate_Type.__name__ = "Integer32"
_SwhUpdateUpdate_Object = MibScalar
swhUpdateUpdate = _SwhUpdateUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 10),
    _SwhUpdateUpdate_Type()
)
swhUpdateUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateUpdate.setStatus("mandatory")


class _SwhUpdateState_Type(DisplayString):
    """Custom type swhUpdateState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhUpdateState_Type.__name__ = "DisplayString"
_SwhUpdateState_Object = MibScalar
swhUpdateState = _SwhUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 12),
    _SwhUpdateState_Type()
)
swhUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhUpdateState.setStatus("mandatory")


class _SwhUpdateServerIPv6Addr_Type(DisplayString):
    """Custom type swhUpdateServerIPv6Addr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhUpdateServerIPv6Addr_Type.__name__ = "DisplayString"
_SwhUpdateServerIPv6Addr_Object = MibScalar
swhUpdateServerIPv6Addr = _SwhUpdateServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 13),
    _SwhUpdateServerIPv6Addr_Type()
)
swhUpdateServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateServerIPv6Addr.setStatus("mandatory")


class _SwhUpdateConfigeType_Type(Integer32):
    """Custom type swhUpdateConfigeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 0),
          ("default", 1),
          ("startup", 2))
    )


_SwhUpdateConfigeType_Type.__name__ = "Integer32"
_SwhUpdateConfigeType_Object = MibScalar
swhUpdateConfigeType = _SwhUpdateConfigeType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 15),
    _SwhUpdateConfigeType_Type()
)
swhUpdateConfigeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateConfigeType.setStatus("mandatory")


class _SwhUpdateImageOption_Type(Integer32):
    """Custom type swhUpdateImageOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_SwhUpdateImageOption_Type.__name__ = "Integer32"
_SwhUpdateImageOption_Object = MibScalar
swhUpdateImageOption = _SwhUpdateImageOption_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 4, 16),
    _SwhUpdateImageOption_Type()
)
swhUpdateImageOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhUpdateImageOption.setStatus("mandatory")
_SwhAutoBackupConfiguration_ObjectIdentity = ObjectIdentity
swhAutoBackupConfiguration = _SwhAutoBackupConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5)
)


class _SwhBackupAuto_Type(Integer32):
    """Custom type swhBackupAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SwhBackupAuto_Type.__name__ = "Integer32"
_SwhBackupAuto_Object = MibScalar
swhBackupAuto = _SwhBackupAuto_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 2),
    _SwhBackupAuto_Type()
)
swhBackupAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhBackupAuto.setStatus("mandatory")


class _SwhBackupTime_Type(Integer32):
    """Custom type swhBackupTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_SwhBackupTime_Type.__name__ = "Integer32"
_SwhBackupTime_Object = MibScalar
swhBackupTime = _SwhBackupTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 3),
    _SwhBackupTime_Type()
)
swhBackupTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhBackupTime.setStatus("mandatory")


class _SwhBackupProtocol_Type(Integer32):
    """Custom type swhBackupProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 0),
          ("ftp", 1))
    )


_SwhBackupProtocol_Type.__name__ = "Integer32"
_SwhBackupProtocol_Object = MibScalar
swhBackupProtocol = _SwhBackupProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 4),
    _SwhBackupProtocol_Type()
)
swhBackupProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhBackupProtocol.setStatus("mandatory")


class _SwhBackupFileType_Type(Integer32):
    """Custom type swhBackupFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("configuration", 1)
    )


_SwhBackupFileType_Type.__name__ = "Integer32"
_SwhBackupFileType_Object = MibScalar
swhBackupFileType = _SwhBackupFileType_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 5),
    _SwhBackupFileType_Type()
)
swhBackupFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhBackupFileType.setStatus("mandatory")


class _SwhBackupServerIPAddr_Type(DisplayString):
    """Custom type swhBackupServerIPAddr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhBackupServerIPAddr_Type.__name__ = "DisplayString"
_SwhBackupServerIPAddr_Object = MibScalar
swhBackupServerIPAddr = _SwhBackupServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 6),
    _SwhBackupServerIPAddr_Type()
)
swhBackupServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhBackupServerIPAddr.setStatus("mandatory")


class _SwhBackupUserName_Type(DisplayString):
    """Custom type swhBackupUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhBackupUserName_Type.__name__ = "DisplayString"
_SwhBackupUserName_Object = MibScalar
swhBackupUserName = _SwhBackupUserName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 7),
    _SwhBackupUserName_Type()
)
swhBackupUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhBackupUserName.setStatus("mandatory")


class _SwhBackupPassword_Type(DisplayString):
    """Custom type swhBackupPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhBackupPassword_Type.__name__ = "DisplayString"
_SwhBackupPassword_Object = MibScalar
swhBackupPassword = _SwhBackupPassword_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 8),
    _SwhBackupPassword_Type()
)
swhBackupPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhBackupPassword.setStatus("mandatory")


class _SwhBackupFileDirectory_Type(DisplayString):
    """Custom type swhBackupFileDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhBackupFileDirectory_Type.__name__ = "DisplayString"
_SwhBackupFileDirectory_Object = MibScalar
swhBackupFileDirectory = _SwhBackupFileDirectory_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 9),
    _SwhBackupFileDirectory_Type()
)
swhBackupFileDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhBackupFileDirectory.setStatus("mandatory")


class _SwhBackupFileName_Type(DisplayString):
    """Custom type swhBackupFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhBackupFileName_Type.__name__ = "DisplayString"
_SwhBackupFileName_Object = MibScalar
swhBackupFileName = _SwhBackupFileName_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 10),
    _SwhBackupFileName_Type()
)
swhBackupFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhBackupFileName.setStatus("mandatory")


class _SwhBackupState_Type(DisplayString):
    """Custom type swhBackupState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhBackupState_Type.__name__ = "DisplayString"
_SwhBackupState_Object = MibScalar
swhBackupState = _SwhBackupState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 12),
    _SwhBackupState_Type()
)
swhBackupState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhBackupState.setStatus("mandatory")


class _SwhBackupTrigger_Type(Integer32):
    """Custom type swhBackupTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ntp-time", 0),
          ("save-configuration", 1))
    )


_SwhBackupTrigger_Type.__name__ = "Integer32"
_SwhBackupTrigger_Object = MibScalar
swhBackupTrigger = _SwhBackupTrigger_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 13),
    _SwhBackupTrigger_Type()
)
swhBackupTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhBackupTrigger.setStatus("mandatory")


class _SwhBackupNTPStatus_Type(DisplayString):
    """Custom type swhBackupNTPStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhBackupNTPStatus_Type.__name__ = "DisplayString"
_SwhBackupNTPStatus_Object = MibScalar
swhBackupNTPStatus = _SwhBackupNTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 5, 14),
    _SwhBackupNTPStatus_Type()
)
swhBackupNTPStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhBackupNTPStatus.setStatus("mandatory")
_SwhLoopbackTest_ObjectIdentity = ObjectIdentity
swhLoopbackTest = _SwhLoopbackTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 6)
)


class _SwhDiagnosticPort_Type(Integer32):
    """Custom type swhDiagnosticPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("select", 0),
          ("port01", 1),
          ("port02", 2),
          ("port03", 3),
          ("port04", 4),
          ("port05", 5),
          ("port06", 6))
    )


_SwhDiagnosticPort_Type.__name__ = "Integer32"
_SwhDiagnosticPort_Object = MibScalar
swhDiagnosticPort = _SwhDiagnosticPort_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 6, 1),
    _SwhDiagnosticPort_Type()
)
swhDiagnosticPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhDiagnosticPort.setStatus("mandatory")


class _SwhVlanID_Type(Integer32):
    """Custom type swhVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwhVlanID_Type.__name__ = "Integer32"
_SwhVlanID_Object = MibScalar
swhVlanID = _SwhVlanID_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 6, 3),
    _SwhVlanID_Type()
)
swhVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhVlanID.setStatus("mandatory")


class _SwhTestTime_Type(Integer32):
    """Custom type swhTestTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SwhTestTime_Type.__name__ = "Integer32"
_SwhTestTime_Object = MibScalar
swhTestTime = _SwhTestTime_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 6, 4),
    _SwhTestTime_Type()
)
swhTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhTestTime.setStatus("mandatory")


class _SwhState_Type(Integer32):
    """Custom type swhState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("active", 1))
    )


_SwhState_Type.__name__ = "Integer32"
_SwhState_Object = MibScalar
swhState = _SwhState_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 6, 5),
    _SwhState_Type()
)
swhState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhState.setStatus("mandatory")


class _SwhTimeRemaining_Type(DisplayString):
    """Custom type swhTimeRemaining based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwhTimeRemaining_Type.__name__ = "DisplayString"
_SwhTimeRemaining_Object = MibScalar
swhTimeRemaining = _SwhTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 6, 6),
    _SwhTimeRemaining_Type()
)
swhTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swhTimeRemaining.setStatus("mandatory")
_SwhLoopbackStop_ObjectIdentity = ObjectIdentity
swhLoopbackStop = _SwhLoopbackStop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 6, 7)
)


class _SwhStop_Type(Integer32):
    """Custom type swhStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("stop", 0)
    )


_SwhStop_Type.__name__ = "Integer32"
_SwhStop_Object = MibScalar
swhStop = _SwhStop_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 6, 6, 7, 1),
    _SwhStop_Type()
)
swhStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhStop.setStatus("mandatory")


class _SwhSaveConfiguration_Type(Integer32):
    """Custom type swhSaveConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("save", 1))
    )


_SwhSaveConfiguration_Type.__name__ = "Integer32"
_SwhSaveConfiguration_Object = MibScalar
swhSaveConfiguration = _SwhSaveConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 7),
    _SwhSaveConfiguration_Type()
)
swhSaveConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhSaveConfiguration.setStatus("mandatory")


class _SwhResetSystem_Type(Integer32):
    """Custom type swhResetSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("reset", 1))
    )


_SwhResetSystem_Type.__name__ = "Integer32"
_SwhResetSystem_Object = MibScalar
swhResetSystem = _SwhResetSystem_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 8),
    _SwhResetSystem_Type()
)
swhResetSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhResetSystem.setStatus("mandatory")
_SwitchTraps_ObjectIdentity = ObjectIdentity
switchTraps = _SwitchTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9)
)


class _SwhNewBootUpImage_Type(Integer32):
    """Custom type swhNewBootUpImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_SwhNewBootUpImage_Type.__name__ = "Integer32"
_SwhNewBootUpImage_Object = MibScalar
swhNewBootUpImage = _SwhNewBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 15),
    _SwhNewBootUpImage_Type()
)
swhNewBootUpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swhNewBootUpImage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

swhSystemPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 1)
)
if mibBuilder.loadTexts:
    swhSystemPowerDown.setStatus(
        ""
    )

swhFaultAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 8)
)
swhFaultAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    swhFaultAlarm.setStatus(
        ""
    )

swhWarningAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 9)
)
swhWarningAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    swhWarningAlarm.setStatus(
        ""
    )

swhMinorAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 10)
)
swhMinorAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    swhMinorAlarm.setStatus(
        ""
    )

swhCriticalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 12)
)
swhCriticalAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    swhCriticalAlarm.setStatus(
        ""
    )

swhLoopBack = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 13)
)
swhLoopBack.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    swhLoopBack.setStatus(
        ""
    )

swhNormalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 16)
)
swhNormalAlarm.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    swhNormalAlarm.setStatus(
        ""
    )

swhCaseFanState = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 19)
)
swhCaseFanState.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    swhCaseFanState.setStatus(
        ""
    )

swhSystemPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 20)
)
swhSystemPowerOn.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("SNMPv2-MIB", "sysLocation"))
)
if mibBuilder.loadTexts:
    swhSystemPowerOn.setStatus(
        ""
    )

swhSystemPowerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9304, 100, 31064, 9, 0, 21)
)
if mibBuilder.loadTexts:
    swhSystemPowerUp.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPS-3106-SE-PB-MIB",
    **{"PhysAddress": PhysAddress,
       "MacAddress": MacAddress,
       "VLANPortMember": VLANPortMember,
       "cts": cts,
       "swh": swh,
       "ips3106se": ips3106se,
       "swhSystemInformation": swhSystemInformation,
       "swhCompanyInfo": swhCompanyInfo,
       "swhCompanyName": swhCompanyName,
       "swhCLIHostname": swhCLIHostname,
       "swhDHCPVendorID": swhDHCPVendorID,
       "swhHardwareInfo": swhHardwareInfo,
       "swhModelName": swhModelName,
       "swhMBVersion": swhMBVersion,
       "swhSerialNumber": swhSerialNumber,
       "swhDateCode": swhDateCode,
       "swhCPUTemperature": swhCPUTemperature,
       "swhPowerSupply1": swhPowerSupply1,
       "swhPowerSupply2": swhPowerSupply2,
       "swhBootUpImage": swhBootUpImage,
       "swhNextBootUpImage": swhNextBootUpImage,
       "swhImage1FirmwareVersion": swhImage1FirmwareVersion,
       "swhImage2FirmwareVersion": swhImage2FirmwareVersion,
       "swhUserAuthentication": swhUserAuthentication,
       "swhUserTable": swhUserTable,
       "swhUserEntry": swhUserEntry,
       "swhUserIndex": swhUserIndex,
       "swhUserEnable": swhUserEnable,
       "swhUserName": swhUserName,
       "swhUserPassword": swhUserPassword,
       "swhUserDescription": swhUserDescription,
       "swhUserConsoleLevel": swhUserConsoleLevel,
       "swhRADIUSConfiguration": swhRADIUSConfiguration,
       "swhRADIUSEn": swhRADIUSEn,
       "swhRADIUSSecretKey": swhRADIUSSecretKey,
       "swhRADIUSPort": swhRADIUSPort,
       "swhRADIUSRetry": swhRADIUSRetry,
       "swhRADIUSIPAddr": swhRADIUSIPAddr,
       "swhRADIUSIPAddr2": swhRADIUSIPAddr2,
       "swhRADIUSIPv6Addr": swhRADIUSIPv6Addr,
       "swhRADIUSIPv6Addr2": swhRADIUSIPv6Addr2,
       "swhTACACSConfiguration": swhTACACSConfiguration,
       "swhTACACSEn": swhTACACSEn,
       "swhTACACSSecretKey": swhTACACSSecretKey,
       "swhTACACSPort": swhTACACSPort,
       "swhTACACSRetry": swhTACACSRetry,
       "swhTACACSIPAddr": swhTACACSIPAddr,
       "swhTACACSIPAddr2": swhTACACSIPAddr2,
       "swhTACACSIPv6Addr": swhTACACSIPv6Addr,
       "swhTACACSIPv6Addr2": swhTACACSIPv6Addr2,
       "swhUserPasswordEncryption": swhUserPasswordEncryption,
       "swhNetworkManagement": swhNetworkManagement,
       "swhNetworkConfiguration": swhNetworkConfiguration,
       "swhNetMacAddr": swhNetMacAddr,
       "swhNetType": swhNetType,
       "swhNetIPAddr": swhNetIPAddr,
       "swhNetIPMask": swhNetIPMask,
       "swhNetGateway": swhNetGateway,
       "swhNetIPv4En": swhNetIPv4En,
       "swhNetCurrentIPAddr": swhNetCurrentIPAddr,
       "swhNetCurrentIPMask": swhNetCurrentIPMask,
       "swhNetCurrentGateway": swhNetCurrentGateway,
       "swhNetIPSourceBinding": swhNetIPSourceBinding,
       "swhNetIPSourceBindingTable": swhNetIPSourceBindingTable,
       "swhNetIPSourceBindingEntry": swhNetIPSourceBindingEntry,
       "swhNetIPSourceBindingIndex": swhNetIPSourceBindingIndex,
       "swhNetIPSourceBindingState": swhNetIPSourceBindingState,
       "swhNetIPSourceBindingIPAddress": swhNetIPSourceBindingIPAddress,
       "swhNetIPSourceBindingIPv6Address": swhNetIPSourceBindingIPv6Address,
       "swhNetIPSourceBindingDelete": swhNetIPSourceBindingDelete,
       "swhNetIPv6En": swhNetIPv6En,
       "swhNetIPv6AutoConfig": swhNetIPv6AutoConfig,
       "swhNetIPv6LinkLocalAddr": swhNetIPv6LinkLocalAddr,
       "swhNetIPv6GlobalAddr": swhNetIPv6GlobalAddr,
       "swhNetIPv6Gateway": swhNetIPv6Gateway,
       "swhNetDHCPv6": swhNetDHCPv6,
       "swhNetRapidCommit": swhNetRapidCommit,
       "swhNetCurrentIPv6LinklocalAddr": swhNetCurrentIPv6LinklocalAddr,
       "swhNetCurrentIPv6GatewayAddr": swhNetCurrentIPv6GatewayAddr,
       "swhNetCurrentDHCPv6DUID": swhNetCurrentDHCPv6DUID,
       "swhSystemServiceConfiguration": swhSystemServiceConfiguration,
       "swhServiceTelnetThreadEn": swhServiceTelnetThreadEn,
       "swhServiceSNMPThreadEn": swhServiceSNMPThreadEn,
       "swhServiceWebThreadEn": swhServiceWebThreadEn,
       "swhServiceSSHThreadEn": swhServiceSSHThreadEn,
       "swhServiceConsolePortThreadEn": swhServiceConsolePortThreadEn,
       "swhRS232TelnetConsoleConfiguration": swhRS232TelnetConsoleConfiguration,
       "swhRS232BaudRate": swhRS232BaudRate,
       "swhRS232StopBits": swhRS232StopBits,
       "swhRS232ParityCheck": swhRS232ParityCheck,
       "swhRS232WordLength": swhRS232WordLength,
       "swhRS232FlowControl": swhRS232FlowControl,
       "swhTelnetPort": swhTelnetPort,
       "swhTimeOutTime": swhTimeOutTime,
       "swhTimeOutTimeUnit": swhTimeOutTimeUnit,
       "swhWebTimeOutTime": swhWebTimeOutTime,
       "swhConsolePortFailRetry": swhConsolePortFailRetry,
       "swhConsolePortFailBlockTime": swhConsolePortFailBlockTime,
       "swhDeviceCommunity": swhDeviceCommunity,
       "swhAgentTable": swhAgentTable,
       "swhAgentEntry": swhAgentEntry,
       "swhAgentIndex": swhAgentIndex,
       "swhAgentValid": swhAgentValid,
       "swhAgentEnable": swhAgentEnable,
       "swhAgentCommunity": swhAgentCommunity,
       "swhAgentDescription": swhAgentDescription,
       "swhAgentSNMPLevel": swhAgentSNMPLevel,
       "swhAgentDelete": swhAgentDelete,
       "swhSNMPv3AgentTable": swhSNMPv3AgentTable,
       "swhSNMPv3AgentEntry": swhSNMPv3AgentEntry,
       "swhSNMPv3AgentIndex": swhSNMPv3AgentIndex,
       "swhSNMPv3AgentValid": swhSNMPv3AgentValid,
       "swhSNMPv3AgentUserName": swhSNMPv3AgentUserName,
       "swhSNMPv3AgentAuthentication": swhSNMPv3AgentAuthentication,
       "swhSNMPv3AgentAuthPassword": swhSNMPv3AgentAuthPassword,
       "swhSNMPv3AgentPrivate": swhSNMPv3AgentPrivate,
       "swhSNMPv3AgentPrivPassword": swhSNMPv3AgentPrivPassword,
       "swhTrapDestination": swhTrapDestination,
       "swhTrapDestTable": swhTrapDestTable,
       "swhTrapDestEntry": swhTrapDestEntry,
       "swhTrapDestIndex": swhTrapDestIndex,
       "swhTrapDestEnable": swhTrapDestEnable,
       "swhTrapDestCommunity": swhTrapDestCommunity,
       "swhTrapDestIPAddr": swhTrapDestIPAddr,
       "swhTrapDestIPv6Addr": swhTrapDestIPv6Addr,
       "swhTrapConfiguration": swhTrapConfiguration,
       "swhTrapColdStart": swhTrapColdStart,
       "swhTrapWarmStart": swhTrapWarmStart,
       "swhTrapAuthenticationFailure": swhTrapAuthenticationFailure,
       "swhTrapPortLink": swhTrapPortLink,
       "swhTrapPowerFailure": swhTrapPowerFailure,
       "swhTrapCPULoading": swhTrapCPULoading,
       "swhTrapAutoBackup": swhTrapAutoBackup,
       "swhTrapMACLimiter": swhTrapMACLimiter,
       "swhTrapStormControl": swhTrapStormControl,
       "swhTrapDigitalState": swhTrapDigitalState,
       "swhTrapConsolePortLink": swhTrapConsolePortLink,
       "swhTrapCPUTemperature": swhTrapCPUTemperature,
       "swhTrapFastRedundancy": swhTrapFastRedundancy,
       "swhTimeServerConfiguration": swhTimeServerConfiguration,
       "swhTimeSync": swhTimeSync,
       "swhTimeServerIPAddr": swhTimeServerIPAddr,
       "swhTimeServerIPAddr2": swhTimeServerIPAddr2,
       "swhTimeSyncInterval": swhTimeSyncInterval,
       "swhTimeZoneIndex": swhTimeZoneIndex,
       "swhTimeZone": swhTimeZone,
       "swhTimeDST": swhTimeDST,
       "swhTimeDSTRange": swhTimeDSTRange,
       "swhTimeServerIPv6Addr": swhTimeServerIPv6Addr,
       "swhTimeServerIPv6Addr2": swhTimeServerIPv6Addr2,
       "swhSyslogConfiguration": swhSyslogConfiguration,
       "swhLogServer": swhLogServer,
       "swhLogSNTPStatus": swhLogSNTPStatus,
       "swhLogServerIPAddr1": swhLogServerIPAddr1,
       "swhLogServerIPAddr2": swhLogServerIPAddr2,
       "swhLogServerIPAddr3": swhLogServerIPAddr3,
       "swhLogServerIPv6Addr1": swhLogServerIPv6Addr1,
       "swhLogServerIPv6Addr2": swhLogServerIPv6Addr2,
       "swhLogServerIPv6Addr3": swhLogServerIPv6Addr3,
       "swhLoggingType": swhLoggingType,
       "swhLoggingTypeTerminalHistory": swhLoggingTypeTerminalHistory,
       "swhTimeRange": swhTimeRange,
       "swhTimeRangeTable": swhTimeRangeTable,
       "swhTimeRangeEntry": swhTimeRangeEntry,
       "swhTimeRangeIndex": swhTimeRangeIndex,
       "swhTimeRangeName": swhTimeRangeName,
       "swhTimeRangeAbsoluteStartHour": swhTimeRangeAbsoluteStartHour,
       "swhTimeRangeAbsoluteStartMinute": swhTimeRangeAbsoluteStartMinute,
       "swhTimeRangeAbsoluteStartDate": swhTimeRangeAbsoluteStartDate,
       "swhTimeRangeAbsoluteStartMonth": swhTimeRangeAbsoluteStartMonth,
       "swhTimeRangeAbsoluteStartYear": swhTimeRangeAbsoluteStartYear,
       "swhTimeRangeAbsoluteStartReset": swhTimeRangeAbsoluteStartReset,
       "swhTimeRangeAbsoluteEndHour": swhTimeRangeAbsoluteEndHour,
       "swhTimeRangeAbsoluteEndMinute": swhTimeRangeAbsoluteEndMinute,
       "swhTimeRangeAbsoluteEndDate": swhTimeRangeAbsoluteEndDate,
       "swhTimeRangeAbsoluteEndMonth": swhTimeRangeAbsoluteEndMonth,
       "swhTimeRangeAbsoluteEndYear": swhTimeRangeAbsoluteEndYear,
       "swhTimeRangeAbsoluteEndReset": swhTimeRangeAbsoluteEndReset,
       "swhTimeRangePeriodic1StartHour": swhTimeRangePeriodic1StartHour,
       "swhTimeRangePeriodic1StartMinute": swhTimeRangePeriodic1StartMinute,
       "swhTimeRangePeriodic1StartDay": swhTimeRangePeriodic1StartDay,
       "swhTimeRangePeriodic1EndHour": swhTimeRangePeriodic1EndHour,
       "swhTimeRangePeriodic1EndMinute": swhTimeRangePeriodic1EndMinute,
       "swhTimeRangePeriodic1EndDay": swhTimeRangePeriodic1EndDay,
       "swhTimeRangePeriodic1Delete": swhTimeRangePeriodic1Delete,
       "swhTimeRangePeriodic2StartHour": swhTimeRangePeriodic2StartHour,
       "swhTimeRangePeriodic2StartMinute": swhTimeRangePeriodic2StartMinute,
       "swhTimeRangePeriodic2StartDay": swhTimeRangePeriodic2StartDay,
       "swhTimeRangePeriodic2EndHour": swhTimeRangePeriodic2EndHour,
       "swhTimeRangePeriodic2EndMinute": swhTimeRangePeriodic2EndMinute,
       "swhTimeRangePeriodic2EndDay": swhTimeRangePeriodic2EndDay,
       "swhTimeRangePeriodic2Delete": swhTimeRangePeriodic2Delete,
       "swhTimeRangePeriodicList1StartHour": swhTimeRangePeriodicList1StartHour,
       "swhTimeRangePeriodicList1StartMinute": swhTimeRangePeriodicList1StartMinute,
       "swhTimeRangePeriodicList1EndHour": swhTimeRangePeriodicList1EndHour,
       "swhTimeRangePeriodicList1EndMinute": swhTimeRangePeriodicList1EndMinute,
       "swhTimeRangePeriodicList1Sun": swhTimeRangePeriodicList1Sun,
       "swhTimeRangePeriodicList1Mon": swhTimeRangePeriodicList1Mon,
       "swhTimeRangePeriodicList1Tue": swhTimeRangePeriodicList1Tue,
       "swhTimeRangePeriodicList1Wed": swhTimeRangePeriodicList1Wed,
       "swhTimeRangePeriodicList1Thr": swhTimeRangePeriodicList1Thr,
       "swhTimeRangePeriodicList1Fri": swhTimeRangePeriodicList1Fri,
       "swhTimeRangePeriodicList1Sat": swhTimeRangePeriodicList1Sat,
       "swhTimeRangePeriodicList1Delete": swhTimeRangePeriodicList1Delete,
       "swhTimeRangePeriodicList2StartHour": swhTimeRangePeriodicList2StartHour,
       "swhTimeRangePeriodicList2StartMinute": swhTimeRangePeriodicList2StartMinute,
       "swhTimeRangePeriodicList2EndHour": swhTimeRangePeriodicList2EndHour,
       "swhTimeRangePeriodicList2EndMinute": swhTimeRangePeriodicList2EndMinute,
       "swhTimeRangePeriodicList2Sun": swhTimeRangePeriodicList2Sun,
       "swhTimeRangePeriodicList2Mon": swhTimeRangePeriodicList2Mon,
       "swhTimeRangePeriodicList2Tue": swhTimeRangePeriodicList2Tue,
       "swhTimeRangePeriodicList2Wed": swhTimeRangePeriodicList2Wed,
       "swhTimeRangePeriodicList2Thr": swhTimeRangePeriodicList2Thr,
       "swhTimeRangePeriodicList2Fri": swhTimeRangePeriodicList2Fri,
       "swhTimeRangePeriodicList2Sat": swhTimeRangePeriodicList2Sat,
       "swhTimeRangePeriodicList2Delete": swhTimeRangePeriodicList2Delete,
       "swhTimeRangeDelete": swhTimeRangeDelete,
       "swhSwitchManagement": swhSwitchManagement,
       "swhSwitchConfiguration": swhSwitchConfiguration,
       "swhSwitchMaxFrameSize": swhSwitchMaxFrameSize,
       "swhSwitchAgingTime": swhSwitchAgingTime,
       "swhSwitch0180C2000000to0F": swhSwitch0180C2000000to0F,
       "swhSwitch0180C2000020to2F": swhSwitch0180C2000020to2F,
       "swhSwitch0180C2000010": swhSwitch0180C2000010,
       "swhSwitchStatisticsPollingPort": swhSwitchStatisticsPollingPort,
       "swhSwitchStatisticsPollingInterval": swhSwitchStatisticsPollingInterval,
       "swhPortConfiguration": swhPortConfiguration,
       "swhPortConfigTable": swhPortConfigTable,
       "swhPortConfigEntry": swhPortConfigEntry,
       "swhPortConfigIndex": swhPortConfigIndex,
       "swhPortConfigState": swhPortConfigState,
       "swhPortConfigType": swhPortConfigType,
       "swhPortConfigSpeed": swhPortConfigSpeed,
       "swhPortConfigDuplex": swhPortConfigDuplex,
       "swhPortConfigFlowControl": swhPortConfigFlowControl,
       "swhPortConfigDescription": swhPortConfigDescription,
       "swhPortConfigMediaType": swhPortConfigMediaType,
       "swhVLANConfiguration": swhVLANConfiguration,
       "swhPortVLANConfiguration": swhPortVLANConfiguration,
       "swhPortVLANConfigTable": swhPortVLANConfigTable,
       "swhPortVLANConfigEntry": swhPortVLANConfigEntry,
       "swhPortVLANConfigIndex": swhPortVLANConfigIndex,
       "swhPortVLANConfigValid": swhPortVLANConfigValid,
       "swhPortVLANConfigName": swhPortVLANConfigName,
       "swhPortVLANConfigPort1": swhPortVLANConfigPort1,
       "swhPortVLANConfigPort2": swhPortVLANConfigPort2,
       "swhPortVLANConfigPort3": swhPortVLANConfigPort3,
       "swhPortVLANConfigPort4": swhPortVLANConfigPort4,
       "swhPortVLANConfigPort5": swhPortVLANConfigPort5,
       "swhPortVLANConfigPort6": swhPortVLANConfigPort6,
       "swhPortVLANConfigCPU": swhPortVLANConfigCPU,
       "swhPortVLANConfigDelete": swhPortVLANConfigDelete,
       "swh8021QVLANConfiguration": swh8021QVLANConfiguration,
       "swh8021QTrunkVLAN": swh8021QTrunkVLAN,
       "swh8021QTrunkVLANTable": swh8021QTrunkVLANTable,
       "swh8021QTrunkVLANEntry": swh8021QTrunkVLANEntry,
       "swh8021QTrunkVLANIndex": swh8021QTrunkVLANIndex,
       "swh8021QTrunkVLANValid": swh8021QTrunkVLANValid,
       "swh8021QTrunkVLANVID": swh8021QTrunkVLANVID,
       "swh8021QTrunkVLANName": swh8021QTrunkVLANName,
       "swh8021QTrunkVLANPort1": swh8021QTrunkVLANPort1,
       "swh8021QTrunkVLANPort2": swh8021QTrunkVLANPort2,
       "swh8021QTrunkVLANPort3": swh8021QTrunkVLANPort3,
       "swh8021QTrunkVLANPort4": swh8021QTrunkVLANPort4,
       "swh8021QTrunkVLANPort5": swh8021QTrunkVLANPort5,
       "swh8021QTrunkVLANPort6": swh8021QTrunkVLANPort6,
       "swh8021QTrunkVLANCPU": swh8021QTrunkVLANCPU,
       "swh8021QTrunkVLANDelete": swh8021QTrunkVLANDelete,
       "swh8021QPortVLANConfig": swh8021QPortVLANConfig,
       "swh8021QPortVLANConfigTable": swh8021QPortVLANConfigTable,
       "swh8021QPortVLANConfigEntry": swh8021QPortVLANConfigEntry,
       "swh8021QPortIndex": swh8021QPortIndex,
       "swh8021QPortAccessVLAN": swh8021QPortAccessVLAN,
       "swh8021QPortVLANMode": swh8021QPortVLANMode,
       "swh8021QPortTrunkVLAN": swh8021QPortTrunkVLAN,
       "swh8021QTunnelEtherType": swh8021QTunnelEtherType,
       "swh8021QManagementVLANConfig": swh8021QManagementVLANConfig,
       "swh8021QManagementVLANConfigCPUVID": swh8021QManagementVLANConfigCPUVID,
       "swh8021QManagementVLANConfigVLANMode": swh8021QManagementVLANConfigVLANMode,
       "swh8021QManagementVLANConfigPort1": swh8021QManagementVLANConfigPort1,
       "swh8021QManagementVLANConfigPort2": swh8021QManagementVLANConfigPort2,
       "swh8021QManagementVLANConfigPort3": swh8021QManagementVLANConfigPort3,
       "swh8021QManagementVLANConfigPort4": swh8021QManagementVLANConfigPort4,
       "swh8021QManagementVLANConfigPort5": swh8021QManagementVLANConfigPort5,
       "swh8021QManagementVLANConfigPort6": swh8021QManagementVLANConfigPort6,
       "swhVLANTranslationConfiguration": swhVLANTranslationConfiguration,
       "swhVLANTranslationConfigVLANTranslation": swhVLANTranslationConfigVLANTranslation,
       "swhVLANTranslationConfigVLANTranslationDeleteAll": swhVLANTranslationConfigVLANTranslationDeleteAll,
       "swhVLANTranslationConfigTable": swhVLANTranslationConfigTable,
       "swhVLANTranslationConfigEntry": swhVLANTranslationConfigEntry,
       "swhVLANTranslationConfigIndex": swhVLANTranslationConfigIndex,
       "swhVLANTranslationConfigValid": swhVLANTranslationConfigValid,
       "swhVLANTranslationConfigName": swhVLANTranslationConfigName,
       "swhVLANTranslationConfigPort": swhVLANTranslationConfigPort,
       "swhVLANTranslationConfigOriginalVID": swhVLANTranslationConfigOriginalVID,
       "swhVLANTranslationConfigMappedVID": swhVLANTranslationConfigMappedVID,
       "swhVLANTranslationConfigPriority": swhVLANTranslationConfigPriority,
       "swhVLANTranslationConfigDelete": swhVLANTranslationConfigDelete,
       "swhLoopDetection": swhLoopDetection,
       "swhLoopConfigPort1": swhLoopConfigPort1,
       "swhLoopConfigPort2": swhLoopConfigPort2,
       "swhLoopConfigPort3": swhLoopConfigPort3,
       "swhLoopConfigPort4": swhLoopConfigPort4,
       "swhLoopConfigPort5": swhLoopConfigPort5,
       "swhLoopConfigPort6": swhLoopConfigPort6,
       "swhLoopConfigLoopDetection": swhLoopConfigLoopDetection,
       "swhLoopConfigDetectionInterval": swhLoopConfigDetectionInterval,
       "swhLoopConfigUnlockInterval": swhLoopConfigUnlockInterval,
       "swhLoopConfigVLAN1": swhLoopConfigVLAN1,
       "swhLoopConfigVLAN2": swhLoopConfigVLAN2,
       "swhLoopConfigVLAN3": swhLoopConfigVLAN3,
       "swhLoopConfigVLAN4": swhLoopConfigVLAN4,
       "swhLoopConfigAllVLAN": swhLoopConfigAllVLAN,
       "swhLLDPConfiguration": swhLLDPConfiguration,
       "swhLLDPConfigPort1": swhLLDPConfigPort1,
       "swhLLDPConfigPort2": swhLLDPConfigPort2,
       "swhLLDPConfigPort3": swhLLDPConfigPort3,
       "swhLLDPConfigPort4": swhLLDPConfigPort4,
       "swhLLDPConfigPort5": swhLLDPConfigPort5,
       "swhLLDPConfigPort6": swhLLDPConfigPort6,
       "swhLLDPConfigReceiverHoldTime": swhLLDPConfigReceiverHoldTime,
       "swhLLDPConfigSendingLLDPPacketInterval": swhLLDPConfigSendingLLDPPacketInterval,
       "swhLLDPConfigSendingLLDPPacketPerDiscover": swhLLDPConfigSendingLLDPPacketPerDiscover,
       "swhLLDPConfigItem": swhLLDPConfigItem,
       "swhLLDPConfigPortDescription": swhLLDPConfigPortDescription,
       "swhLLDPConfigSystemName": swhLLDPConfigSystemName,
       "swhLLDPConfigSystemDescription": swhLLDPConfigSystemDescription,
       "swhLLDPConfigSystemCapabilities": swhLLDPConfigSystemCapabilities,
       "swhLLDPConfigManagementAddress": swhLLDPConfigManagementAddress,
       "swhPortMirroring": swhPortMirroring,
       "swhPortMirrorSourcePortConfigTable": swhPortMirrorSourcePortConfigTable,
       "swhPortMirrorSourcePortConfigEntry": swhPortMirrorSourcePortConfigEntry,
       "swhPortMirrorSourcePortConfigIndex": swhPortMirrorSourcePortConfigIndex,
       "swhPortMirrorSourcePortConfigMember": swhPortMirrorSourcePortConfigMember,
       "swhTargetPort": swhTargetPort,
       "swhDIDOConfiguration": swhDIDOConfiguration,
       "swhDIConfigTable": swhDIConfigTable,
       "swhDIConfigEntry": swhDIConfigEntry,
       "swhDIConfigIndex": swhDIConfigIndex,
       "swhDIConfigNormal": swhDIConfigNormal,
       "swhDOConfigTable": swhDOConfigTable,
       "swhDOConfigEntry": swhDOConfigEntry,
       "swhDOConfigIndex": swhDOConfigIndex,
       "swhDOConfigNormal": swhDOConfigNormal,
       "swhDOConfigEventTrigger": swhDOConfigEventTrigger,
       "swhDOConfigEventDigitalInput1": swhDOConfigEventDigitalInput1,
       "swhDOConfigEventPortList": swhDOConfigEventPortList,
       "swhDOConfigEventPower1": swhDOConfigEventPower1,
       "swhDOConfigEventPower2": swhDOConfigEventPower2,
       "swhPOEConfiguration": swhPOEConfiguration,
       "swhPOEPortConfigTable": swhPOEPortConfigTable,
       "swhPOEPortConfigEntry": swhPOEPortConfigEntry,
       "swhPOEPortConfigIndex": swhPOEPortConfigIndex,
       "swhPOEPortConfigState": swhPOEPortConfigState,
       "swhPOEPortConfigPort": swhPOEPortConfigPort,
       "swhPOEPortConfigName": swhPOEPortConfigName,
       "swhPOEPortConfigTimeRange": swhPOEPortConfigTimeRange,
       "swhPOEPortConfigSchedule": swhPOEPortConfigSchedule,
       "swhPOEPortConfigPriority": swhPOEPortConfigPriority,
       "swhPOEConfigTotalBudget": swhPOEConfigTotalBudget,
       "swhRingDetection": swhRingDetection,
       "swhRingDetectionEnable": swhRingDetectionEnable,
       "swhRingDetectionSoftwareRole": swhRingDetectionSoftwareRole,
       "swhRingDetectionPortList": swhRingDetectionPortList,
       "swhMacAddressManagement": swhMacAddressManagement,
       "swhMACTableLearning": swhMACTableLearning,
       "swhMACTableLearningTable": swhMACTableLearningTable,
       "swhMACTableLearningEntry": swhMACTableLearningEntry,
       "swhMACTableLearningIndex": swhMACTableLearningIndex,
       "swhMACTableLearningLearning": swhMACTableLearningLearning,
       "swhStaticMACTableConfiguration": swhStaticMACTableConfiguration,
       "swhStaticForwardTable": swhStaticForwardTable,
       "swhStaticForwardEntry": swhStaticForwardEntry,
       "swhStaticForwardIndex": swhStaticForwardIndex,
       "swhStaticForwardValid": swhStaticForwardValid,
       "swhStaticForwardMacAddress": swhStaticForwardMacAddress,
       "swhStaticForwardVID": swhStaticForwardVID,
       "swhStaticForwardPort": swhStaticForwardPort,
       "swhStaticForwardDelete": swhStaticForwardDelete,
       "swhLayer2ProtocolTunnel": swhLayer2ProtocolTunnel,
       "swhL2PTConfigState": swhL2PTConfigState,
       "swhL2PTConfigDestinationMACAddress": swhL2PTConfigDestinationMACAddress,
       "swhL2PTConfigClassOfService": swhL2PTConfigClassOfService,
       "swhL2PTPortConfigTable": swhL2PTPortConfigTable,
       "swhL2PTPortConfigEntry": swhL2PTPortConfigEntry,
       "swhL2PTPortConfigIndex": swhL2PTPortConfigIndex,
       "swhL2PTPortConfigPort": swhL2PTPortConfigPort,
       "swhL2PTPortConfigCDP": swhL2PTPortConfigCDP,
       "swhL2PTPortConfigLLDP": swhL2PTPortConfigLLDP,
       "swhL2PTPortConfigSTP": swhL2PTPortConfigSTP,
       "swhL2PTPortConfigVTP": swhL2PTPortConfigVTP,
       "swhL2PTPortConfigLACP": swhL2PTPortConfigLACP,
       "swhL2PTPortConfigPAgP": swhL2PTPortConfigPAgP,
       "swhL2PTPortConfigUDLD": swhL2PTPortConfigUDLD,
       "swhL2PTPortConfigClear": swhL2PTPortConfigClear,
       "swhRapidSpanningTree": swhRapidSpanningTree,
       "swhRSTPSwitchSettings": swhRSTPSwitchSettings,
       "swhRSTPSwitchSettingsSystemPriority": swhRSTPSwitchSettingsSystemPriority,
       "swhRSTPSwitchSettingsSystemPriorityIndex": swhRSTPSwitchSettingsSystemPriorityIndex,
       "swhRSTPSwitchSettingsMaxAge": swhRSTPSwitchSettingsMaxAge,
       "swhRSTPSwitchSettingsHelloTime": swhRSTPSwitchSettingsHelloTime,
       "swhRSTPSwitchSettingsForwardDelay": swhRSTPSwitchSettingsForwardDelay,
       "swhRSTPSwitchSettingsForceVersion": swhRSTPSwitchSettingsForceVersion,
       "swhRSTPAggregatedPortSettings": swhRSTPAggregatedPortSettings,
       "swhRSTPAggregatedPortSettingsState": swhRSTPAggregatedPortSettingsState,
       "swhRSTPAggregatedPortSettingsCost": swhRSTPAggregatedPortSettingsCost,
       "swhRSTPAggregatedPortSettingsPriority": swhRSTPAggregatedPortSettingsPriority,
       "swhRSTPAggregatedPortSettingsPriorityIndex": swhRSTPAggregatedPortSettingsPriorityIndex,
       "swhRSTPAggregatedPortSettingsEdge": swhRSTPAggregatedPortSettingsEdge,
       "swhRSTPAggregatedPortSettingsPoint2point": swhRSTPAggregatedPortSettingsPoint2point,
       "swhRSTPPhysicalPortSettings": swhRSTPPhysicalPortSettings,
       "swhRSTPPhysicalPortSettingsTable": swhRSTPPhysicalPortSettingsTable,
       "swhRSTPPhysicalPortSettingsEntry": swhRSTPPhysicalPortSettingsEntry,
       "swhRSTPPhysicalPortSettingsIndex": swhRSTPPhysicalPortSettingsIndex,
       "swhRSTPPhysicalPortSettingsState": swhRSTPPhysicalPortSettingsState,
       "swhRSTPPhysicalPortSettingsEdge": swhRSTPPhysicalPortSettingsEdge,
       "swhRSTPPhysicalPortSettingsPathCost": swhRSTPPhysicalPortSettingsPathCost,
       "swhRSTPPhysicalPortSettingsPriority": swhRSTPPhysicalPortSettingsPriority,
       "swhRSTPPhysicalPortSettingsPriorityIndex": swhRSTPPhysicalPortSettingsPriorityIndex,
       "swhRSTPPhysicalPortSettingsPoint2point": swhRSTPPhysicalPortSettingsPoint2point,
       "swhLinkAggregation": swhLinkAggregation,
       "swhDistributionRule": swhDistributionRule,
       "swhDistributionRuleSourceIPAddress": swhDistributionRuleSourceIPAddress,
       "swhDistributionRuleDestinationIPAddress": swhDistributionRuleDestinationIPAddress,
       "swhDistributionRuleSourceL4Port": swhDistributionRuleSourceL4Port,
       "swhDistributionRuleDestinationL4Port": swhDistributionRuleDestinationL4Port,
       "swhDistributionRuleSourceMACAddress": swhDistributionRuleSourceMACAddress,
       "swhDistributionRuleDestinationMACAddress": swhDistributionRuleDestinationMACAddress,
       "swhPortTrunkConfiguration": swhPortTrunkConfiguration,
       "swhPortTrunkConfigTable": swhPortTrunkConfigTable,
       "swhPortTrunkConfigEntry": swhPortTrunkConfigEntry,
       "swhPortTrunkConfigIndex": swhPortTrunkConfigIndex,
       "swhPortTrunkConfigValid": swhPortTrunkConfigValid,
       "swhPortTrunkConfigGroupName": swhPortTrunkConfigGroupName,
       "swhPortTrunkConfigPort1": swhPortTrunkConfigPort1,
       "swhPortTrunkConfigPort2": swhPortTrunkConfigPort2,
       "swhPortTrunkConfigPort3": swhPortTrunkConfigPort3,
       "swhPortTrunkConfigPort4": swhPortTrunkConfigPort4,
       "swhPortTrunkConfigPort5": swhPortTrunkConfigPort5,
       "swhPortTrunkConfigPort6": swhPortTrunkConfigPort6,
       "swhPortTrunkConfigDelete": swhPortTrunkConfigDelete,
       "swhLACPPortConfiguration": swhLACPPortConfiguration,
       "swhLACPPortConfigTable": swhLACPPortConfigTable,
       "swhLACPPortConfigEntry": swhLACPPortConfigEntry,
       "swhLACPPortConfigIndex": swhLACPPortConfigIndex,
       "swhLACPPortConfigKeyValue": swhLACPPortConfigKeyValue,
       "swhLACPPortConfigRole": swhLACPPortConfigRole,
       "swhIGMPSnooping": swhIGMPSnooping,
       "swhIGMPConfiguration": swhIGMPConfiguration,
       "swhIGMPConfigSnooping": swhIGMPConfigSnooping,
       "swhIGMPConfigFastLeave": swhIGMPConfigFastLeave,
       "swhIGMPConfigRouterPort1": swhIGMPConfigRouterPort1,
       "swhIGMPConfigRouterPort2": swhIGMPConfigRouterPort2,
       "swhIGMPConfigRouterPort3": swhIGMPConfigRouterPort3,
       "swhIGMPConfigRouterPort4": swhIGMPConfigRouterPort4,
       "swhIGMPConfigRouterPort5": swhIGMPConfigRouterPort5,
       "swhIGMPConfigRouterPort6": swhIGMPConfigRouterPort6,
       "swhIGMPConfigUnregisteredIPMCFlooding": swhIGMPConfigUnregisteredIPMCFlooding,
       "swhIGMPConfigQueryResponseInterval": swhIGMPConfigQueryResponseInterval,
       "swhIGMPConfigQueryInterval": swhIGMPConfigQueryInterval,
       "swhIGMPConfigSnoopingV3": swhIGMPConfigSnoopingV3,
       "swhIGMPVIDConfiguration": swhIGMPVIDConfiguration,
       "swhIGMPVIDConfigTable": swhIGMPVIDConfigTable,
       "swhIGMPVIDConfigEntry": swhIGMPVIDConfigEntry,
       "swhIGMPVIDConfigIndex": swhIGMPVIDConfigIndex,
       "swhIGMPVIDConfigVLANName": swhIGMPVIDConfigVLANName,
       "swhIGMPVIDConfigVLANID": swhIGMPVIDConfigVLANID,
       "swhIGMPVIDConfigSnooping": swhIGMPVIDConfigSnooping,
       "swhIGMPVIDConfigQuerying": swhIGMPVIDConfigQuerying,
       "swhIPMCSegment": swhIPMCSegment,
       "swhIPMCSegmentTable": swhIPMCSegmentTable,
       "swhIPMCSegmentEntry": swhIPMCSegmentEntry,
       "swhIPMCSegmentIndex": swhIPMCSegmentIndex,
       "swhIPMCSegmentValid": swhIPMCSegmentValid,
       "swhIPMCSegmentSegmentID": swhIPMCSegmentSegmentID,
       "swhIPMCSegmentSegmentName": swhIPMCSegmentSegmentName,
       "swhIPMCSegmentIPRange1": swhIPMCSegmentIPRange1,
       "swhIPMCSegmentIPRange2": swhIPMCSegmentIPRange2,
       "swhIPMCSegmentDelete": swhIPMCSegmentDelete,
       "swhIPMCProfile": swhIPMCProfile,
       "swhIPMCProfileTable": swhIPMCProfileTable,
       "swhIPMCProfileEntry": swhIPMCProfileEntry,
       "swhIPMCProfileIndex": swhIPMCProfileIndex,
       "swhIPMCProfileValid": swhIPMCProfileValid,
       "swhIPMCProfileProfileName": swhIPMCProfileProfileName,
       "swhIPMCProfileSegment1": swhIPMCProfileSegment1,
       "swhIPMCProfileSegment2": swhIPMCProfileSegment2,
       "swhIPMCProfileSegment3": swhIPMCProfileSegment3,
       "swhIPMCProfileSegment4": swhIPMCProfileSegment4,
       "swhIPMCProfileSegment5": swhIPMCProfileSegment5,
       "swhIPMCProfileSegment6": swhIPMCProfileSegment6,
       "swhIPMCProfileSegment7": swhIPMCProfileSegment7,
       "swhIPMCProfileSegment8": swhIPMCProfileSegment8,
       "swhIPMCProfileSegment9": swhIPMCProfileSegment9,
       "swhIPMCProfileSegment10": swhIPMCProfileSegment10,
       "swhIPMCProfileDelete": swhIPMCProfileDelete,
       "swhIGMPFiltering": swhIGMPFiltering,
       "swhIGMPFilterTable": swhIGMPFilterTable,
       "swhIGMPFilterEntry": swhIGMPFilterEntry,
       "swhIGMPFilterIndex": swhIGMPFilterIndex,
       "swhIGMPFilterEnable": swhIGMPFilterEnable,
       "swhIGMPFilterPortName": swhIGMPFilterPortName,
       "swhIGMPFilterIPMCProfile1": swhIGMPFilterIPMCProfile1,
       "swhIGMPFilterIPMCProfile2": swhIGMPFilterIPMCProfile2,
       "swhIGMPFilterIPMCProfile3": swhIGMPFilterIPMCProfile3,
       "swhIGMPFilterIPMCProfile4": swhIGMPFilterIPMCProfile4,
       "swhIGMPFilterChannelLimit": swhIGMPFilterChannelLimit,
       "swhIGMPFilterState": swhIGMPFilterState,
       "swh8021XConfiguration": swh8021XConfiguration,
       "swh8021XSystemConfig": swh8021XSystemConfig,
       "swh8021XSystemConfigMode": swh8021XSystemConfigMode,
       "swh8021XSystemConfigRADIUSIP": swh8021XSystemConfigRADIUSIP,
       "swh8021XSystemConfigRADIUSSecret": swh8021XSystemConfigRADIUSSecret,
       "swh8021XSystemConfigRauthenticationEn": swh8021XSystemConfigRauthenticationEn,
       "swh8021XSystemConfigRadiusAssignedVLANEn": swh8021XSystemConfigRadiusAssignedVLANEn,
       "swh8021XPortConfig": swh8021XPortConfig,
       "swh8021XPortConfigTable": swh8021XPortConfigTable,
       "swh8021XPortConfigEntry": swh8021XPortConfigEntry,
       "swh8021XPortConfigIndex": swh8021XPortConfigIndex,
       "swh8021XPortConfigAdminState": swh8021XPortConfigAdminState,
       "swh8021XPortConfigReauthenticate": swh8021XPortConfigReauthenticate,
       "swh8021XPortConfigRadiusAssignedVLAN": swh8021XPortConfigRadiusAssignedVLAN,
       "swh8021XPortConfigMAB": swh8021XPortConfigMAB,
       "swh8021XPortConfigreAuthEnable": swh8021XPortConfigreAuthEnable,
       "swh8021XPortConfigreAuthSec": swh8021XPortConfigreAuthSec,
       "swh8021XPortConfigEAPTimeout": swh8021XPortConfigEAPTimeout,
       "swh8021XPortConfigMaxreq": swh8021XPortConfigMaxreq,
       "swhQoSConfiguration": swhQoSConfiguration,
       "swhQoSConfigPriority": swhQoSConfigPriority,
       "swhQoSConfigPriorityMode": swhQoSConfigPriorityMode,
       "swhQoSConfigPriorityQueuingMode": swhQoSConfigPriorityQueuingMode,
       "swhQoSConfig8021pPriorityTable": swhQoSConfig8021pPriorityTable,
       "swhQoSConfig8021pPriorityEntry": swhQoSConfig8021pPriorityEntry,
       "swhQoSConfig8021pPriorityIndex": swhQoSConfig8021pPriorityIndex,
       "swhQoSConfig8021pPriorityPriority": swhQoSConfig8021pPriorityPriority,
       "swhQoSConfig8021pPriorityQueue": swhQoSConfig8021pPriorityQueue,
       "swhQoSConfigDSCPPriorityTable": swhQoSConfigDSCPPriorityTable,
       "swhQoSConfigDSCPPriorityEntry": swhQoSConfigDSCPPriorityEntry,
       "swhQoSConfigDSCPPriorityIndex": swhQoSConfigDSCPPriorityIndex,
       "swhQoSConfigDSCPPriorityPriority": swhQoSConfigDSCPPriorityPriority,
       "swhQoSConfigDSCPPriorityQueue": swhQoSConfigDSCPPriorityQueue,
       "swhQoSConfigPriorityManagementPriority": swhQoSConfigPriorityManagementPriority,
       "swhQoSConfigPriorityQueueWeighted": swhQoSConfigPriorityQueueWeighted,
       "swhQoSConfigPriority8021pRemarking": swhQoSConfigPriority8021pRemarking,
       "swhQoSConfig8021pRemarkingTable": swhQoSConfig8021pRemarkingTable,
       "swhQoSConfig8021pRemarkingEntry": swhQoSConfig8021pRemarkingEntry,
       "swhQoSConfig8021pRemarkingIndex": swhQoSConfig8021pRemarkingIndex,
       "swhQoSConfig8021pRemarkingNew8021p": swhQoSConfig8021pRemarkingNew8021p,
       "swhQoSConfig8021pRemarkingRx8021p": swhQoSConfig8021pRemarkingRx8021p,
       "swhQoSConfigPriorityDSCPRemarking": swhQoSConfigPriorityDSCPRemarking,
       "swhQoSConfigDSCPRemarkingTable": swhQoSConfigDSCPRemarkingTable,
       "swhQoSConfigDSCPRemarkingEntry": swhQoSConfigDSCPRemarkingEntry,
       "swhQoSConfigDSCPRemarkingIndex": swhQoSConfigDSCPRemarkingIndex,
       "swhQoSConfigDSCPRemarkingNewDSCP": swhQoSConfigDSCPRemarkingNewDSCP,
       "swhQoSConfigDSCPRemarkingRxDSCP": swhQoSConfigDSCPRemarkingRxDSCP,
       "swhQoSConfigPortConfig": swhQoSConfigPortConfig,
       "swhQoSConfigPortConfigTable": swhQoSConfigPortConfigTable,
       "swhQoSConfigPortConfigEntry": swhQoSConfigPortConfigEntry,
       "swhQoSConfigPortConfigIndex": swhQoSConfigPortConfigIndex,
       "swhQoSConfigPortConfigUserPriority": swhQoSConfigPortConfigUserPriority,
       "swhQoSConfigRateLimiters": swhQoSConfigRateLimiters,
       "swhQoSConfigRateLimitersTable": swhQoSConfigRateLimitersTable,
       "swhQoSConfigRateLimitersEntry": swhQoSConfigRateLimitersEntry,
       "swhQoSConfigRateLimitersIndex": swhQoSConfigRateLimitersIndex,
       "swhQoSConfigRateLimitersIngressRate": swhQoSConfigRateLimitersIngressRate,
       "swhQoSConfigRateLimitersEgressRate": swhQoSConfigRateLimitersEgressRate,
       "swhDSCPRemark": swhDSCPRemark,
       "swhACLConfiguration": swhACLConfiguration,
       "swhAccessControlList": swhAccessControlList,
       "swhAccessControlListTable": swhAccessControlListTable,
       "swhAccessControlListEntry": swhAccessControlListEntry,
       "swhAccessControlListIndex": swhAccessControlListIndex,
       "swhAccessControlListValid": swhAccessControlListValid,
       "swhAccessControlListRuleID": swhAccessControlListRuleID,
       "swhAccessControlListIngressPort": swhAccessControlListIngressPort,
       "swhAccessControlListAction": swhAccessControlListAction,
       "swhAccessControlListRateLimiter": swhAccessControlListRateLimiter,
       "swhAccessControlListPortCopy": swhAccessControlListPortCopy,
       "swhAccessControlListDelete": swhAccessControlListDelete,
       "swhAccessControlListSourceMACFilter": swhAccessControlListSourceMACFilter,
       "swhAccessControlListSourceMACValue": swhAccessControlListSourceMACValue,
       "swhAccessControlListDestinationMACFilter": swhAccessControlListDestinationMACFilter,
       "swhAccessControlListDestinationMACValue": swhAccessControlListDestinationMACValue,
       "swhAccessControlListVLANIDFilter": swhAccessControlListVLANIDFilter,
       "swhAccessControlListVLANID": swhAccessControlListVLANID,
       "swhAccessControlListEtherTypeFilter": swhAccessControlListEtherTypeFilter,
       "swhAccessControlListEthernetTypeValue": swhAccessControlListEthernetTypeValue,
       "swhAccessControlListIngressPortFilter": swhAccessControlListIngressPortFilter,
       "swhAccessControlListSourceMACMask": swhAccessControlListSourceMACMask,
       "swhAccessControlListDestinationMACMask": swhAccessControlListDestinationMACMask,
       "swhAccessControlListTOSTrafficClassFilter": swhAccessControlListTOSTrafficClassFilter,
       "swhAccessControlListTOSTrafficClass": swhAccessControlListTOSTrafficClass,
       "swhAccessControlListProtocolNextHeaderFilter": swhAccessControlListProtocolNextHeaderFilter,
       "swhAccessControlListProtocolNextHeader": swhAccessControlListProtocolNextHeader,
       "swhAccessControlListIPv4SourceIPFilter": swhAccessControlListIPv4SourceIPFilter,
       "swhAccessControlListIPv4SourceIPAddress": swhAccessControlListIPv4SourceIPAddress,
       "swhAccessControlListIPv4SourceIPMask": swhAccessControlListIPv4SourceIPMask,
       "swhAccessControlListIPv4DestinationIPFilter": swhAccessControlListIPv4DestinationIPFilter,
       "swhAccessControlListIPv4DestinationIPAddress": swhAccessControlListIPv4DestinationIPAddress,
       "swhAccessControlListIPv4DestinationIPMask": swhAccessControlListIPv4DestinationIPMask,
       "swhAccessControlListIPv6SourceIPFilter": swhAccessControlListIPv6SourceIPFilter,
       "swhAccessControlListIPv6SourceIPAddress": swhAccessControlListIPv6SourceIPAddress,
       "swhAccessControlListIPv6SourceIPMask": swhAccessControlListIPv6SourceIPMask,
       "swhAccessControlListIPv6DestinationIPFilter": swhAccessControlListIPv6DestinationIPFilter,
       "swhAccessControlListIPv6DestinationIPAddress": swhAccessControlListIPv6DestinationIPAddress,
       "swhAccessControlListIPv6DestinationIPMask": swhAccessControlListIPv6DestinationIPMask,
       "swhAccessControlListTCPUDPSourcePortFilter": swhAccessControlListTCPUDPSourcePortFilter,
       "swhAccessControlListTCPUDPSourcePort": swhAccessControlListTCPUDPSourcePort,
       "swhAccessControlListTCPUDPSourcePortMask": swhAccessControlListTCPUDPSourcePortMask,
       "swhAccessControlListTCPUDPDestinationPortFilter": swhAccessControlListTCPUDPDestinationPortFilter,
       "swhAccessControlListTCPUDPDestinationPort": swhAccessControlListTCPUDPDestinationPort,
       "swhAccessControlListTCPUDPDestinationPortMask": swhAccessControlListTCPUDPDestinationPortMask,
       "swhAccessControlListApply": swhAccessControlListApply,
       "swhStaticMulticastConfiguration": swhStaticMulticastConfiguration,
       "swhMulticastTable": swhMulticastTable,
       "swhMulticastEntry": swhMulticastEntry,
       "swhMulticastIndex": swhMulticastIndex,
       "swhMulticastValid": swhMulticastValid,
       "swhMulticastIPAddress": swhMulticastIPAddress,
       "swhMulticastVLANID": swhMulticastVLANID,
       "swhMulticastForwardingPort": swhMulticastForwardingPort,
       "swhMulticastDelete": swhMulticastDelete,
       "swhMulticastIPv6Address": swhMulticastIPv6Address,
       "swhSecurityConfiguration": swhSecurityConfiguration,
       "swhDHCPOpt82Settings": swhDHCPOpt82Settings,
       "swhSecurityConfigDHCPOpt82RelayAgent": swhSecurityConfigDHCPOpt82RelayAgent,
       "swhSecurityConfigRemoteID": swhSecurityConfigRemoteID,
       "swhSecurityConfigDHCPOpt82PortTable": swhSecurityConfigDHCPOpt82PortTable,
       "swhSecurityConfigDHCPOpt82PortTableEntry": swhSecurityConfigDHCPOpt82PortTableEntry,
       "swhDHCPOpt82PortIndex": swhDHCPOpt82PortIndex,
       "swhDHCPOpt82PortOpt82Port": swhDHCPOpt82PortOpt82Port,
       "swhDHCPOpt82PortTrustPort": swhDHCPOpt82PortTrustPort,
       "swhIPSourceGuardSettings": swhIPSourceGuardSettings,
       "swhIPSourceGuardSettingsPort1": swhIPSourceGuardSettingsPort1,
       "swhIPSourceGuardSettingsPort2": swhIPSourceGuardSettingsPort2,
       "swhIPSourceGuardSettingsPort3": swhIPSourceGuardSettingsPort3,
       "swhIPSourceGuardSettingsPort4": swhIPSourceGuardSettingsPort4,
       "swhIPSourceGuardSettingsPort5": swhIPSourceGuardSettingsPort5,
       "swhIPSourceGuardSettingsPort6": swhIPSourceGuardSettingsPort6,
       "swhDHCPSnooping": swhDHCPSnooping,
       "swhFilterConfigDHCPSnooping": swhFilterConfigDHCPSnooping,
       "swhFilterConfigDefaultDHCPInitiatedTime": swhFilterConfigDefaultDHCPInitiatedTime,
       "swhFilterConfigDefaultDHCPLeasedTime": swhFilterConfigDefaultDHCPLeasedTime,
       "swhSecurityDHCPServerTrustPort": swhSecurityDHCPServerTrustPort,
       "swhSecurityDHCPServerTable": swhSecurityDHCPServerTable,
       "swhSecurityDHCPServerTableEntry": swhSecurityDHCPServerTableEntry,
       "swhSecurityDHCPServerTableIndex": swhSecurityDHCPServerTableIndex,
       "swhSecurityDHCPServerTableState": swhSecurityDHCPServerTableState,
       "swhSecurityDHCPServerTrustIP": swhSecurityDHCPServerTrustIP,
       "swhSecurityDHCPServerIP": swhSecurityDHCPServerIP,
       "swhSecurityDHCPServerIPTable": swhSecurityDHCPServerIPTable,
       "swhSecurityDHCPServerIPEntry": swhSecurityDHCPServerIPEntry,
       "swhSecurityDHCPServerIPIndex": swhSecurityDHCPServerIPIndex,
       "swhSecurityDHCPServerIPIPAddress": swhSecurityDHCPServerIPIPAddress,
       "swhSecurityDHCPServerIPIPv6Address": swhSecurityDHCPServerIPIPv6Address,
       "swhSecurityDHCPServerIPDelete": swhSecurityDHCPServerIPDelete,
       "swhStaticIPTableConfiguration": swhStaticIPTableConfiguration,
       "swhStaticIPTable": swhStaticIPTable,
       "swhStaticIPTableEntry": swhStaticIPTableEntry,
       "swhStaticIPTableIndex": swhStaticIPTableIndex,
       "swhStaticIPTableValid": swhStaticIPTableValid,
       "swhStaticIPTableIPAddress": swhStaticIPTableIPAddress,
       "swhStaticIPTableVLANID": swhStaticIPTableVLANID,
       "swhStaticIPTablePort": swhStaticIPTablePort,
       "swhStaticIPTableDelete": swhStaticIPTableDelete,
       "swhStaticIPTableIPv6Address": swhStaticIPTableIPv6Address,
       "swhDHCPOpt82Configuration": swhDHCPOpt82Configuration,
       "swhDHCPOpt82CircuitIDPortList": swhDHCPOpt82CircuitIDPortList,
       "swhDHCPOpt82CircuitIDTable": swhDHCPOpt82CircuitIDTable,
       "swhDHCPOpt82CircuitIDTableEntry": swhDHCPOpt82CircuitIDTableEntry,
       "swhDHCPOpt82CircuitIDTableIndex": swhDHCPOpt82CircuitIDTableIndex,
       "swhDHCPOpt82CircuitIDTableCircuitID": swhDHCPOpt82CircuitIDTableCircuitID,
       "swhDHCPOpt82CircuitIDTableDelete": swhDHCPOpt82CircuitIDTableDelete,
       "swhDHCPOpt82RemoteIDEnable": swhDHCPOpt82RemoteIDEnable,
       "swhDHCPOpt82RemoteID": swhDHCPOpt82RemoteID,
       "swhDHCPOpt82CircuitIDFormattedPortList": swhDHCPOpt82CircuitIDFormattedPortList,
       "swhDHCPOpt82RemoteIDFormattedEnable": swhDHCPOpt82RemoteIDFormattedEnable,
       "swhMacLimiters": swhMacLimiters,
       "swhMacLimitersEnable": swhMacLimitersEnable,
       "swhMacLimitersThresholdInterval": swhMacLimitersThresholdInterval,
       "swhMacLimitersPortTable": swhMacLimitersPortTable,
       "swhMacLimitersPortEntry": swhMacLimitersPortEntry,
       "swhMacLimitersPortIndex": swhMacLimitersPortIndex,
       "swhMacLimitersPortEnable": swhMacLimitersPortEnable,
       "swhMacLimitersPortLimit": swhMacLimitersPortLimit,
       "swhStormControl": swhStormControl,
       "swhThresholdInterval": swhThresholdInterval,
       "swhSecurityStormControlTable": swhSecurityStormControlTable,
       "swhSecurityStormControlEntry": swhSecurityStormControlEntry,
       "swhSecurityStormControlIndex": swhSecurityStormControlIndex,
       "swhSecurityStormControlBroadcastRate": swhSecurityStormControlBroadcastRate,
       "swhSecurityStormControlUnknownMulticastRate": swhSecurityStormControlUnknownMulticastRate,
       "swhSecurityStormControlUnknownUnicastRate": swhSecurityStormControlUnknownUnicastRate,
       "swhSecurityStormControlPortConfigPort": swhSecurityStormControlPortConfigPort,
       "swhStormControlEnable": swhStormControlEnable,
       "swhPortIsolationConfiguration": swhPortIsolationConfiguration,
       "swhPortIsolationConfigPortIsolation": swhPortIsolationConfigPortIsolation,
       "swhPortIsolationConfigUplinkPortList": swhPortIsolationConfigUplinkPortList,
       "swhPoEManagementAndMonitor": swhPoEManagementAndMonitor,
       "swhFastRedundancy": swhFastRedundancy,
       "swhFastRedundancyConfigTable": swhFastRedundancyConfigTable,
       "swhFastRedundancyConfigEntry": swhFastRedundancyConfigEntry,
       "swhFastRedundancyConfigIndex": swhFastRedundancyConfigIndex,
       "swhFastRedundancyConfigValid": swhFastRedundancyConfigValid,
       "swhFastRedundancyConfigGroupID": swhFastRedundancyConfigGroupID,
       "swhFastRedundancyConfigDescription": swhFastRedundancyConfigDescription,
       "swhFastRedundancyConfigProtocol": swhFastRedundancyConfigProtocol,
       "swhFastRedundancyConfigEnable": swhFastRedundancyConfigEnable,
       "swhFastRedundancyConfigRole": swhFastRedundancyConfigRole,
       "swhFastRedundancyConfigPort1": swhFastRedundancyConfigPort1,
       "swhFastRedundancyConfigPort1Role": swhFastRedundancyConfigPort1Role,
       "swhFastRedundancyConfigPort2": swhFastRedundancyConfigPort2,
       "swhFastRedundancyConfigPort2Role": swhFastRedundancyConfigPort2Role,
       "swhFastRedundancyConfigDelete": swhFastRedundancyConfigDelete,
       "swhSwitchMonitor": swhSwitchMonitor,
       "swhPortStatus": swhPortStatus,
       "swhPortStatusTable": swhPortStatusTable,
       "swhPortStatusEntry": swhPortStatusEntry,
       "swhPortStatusIndex": swhPortStatusIndex,
       "swhPortStatusDescription": swhPortStatusDescription,
       "swhPortStatusPortMedia": swhPortStatusPortMedia,
       "swhPortStatusPortState": swhPortStatusPortState,
       "swhPortStatusPortLink": swhPortStatusPortLink,
       "swhPortStatusPortSpeed": swhPortStatusPortSpeed,
       "swhPortStatusPortDuplex": swhPortStatusPortDuplex,
       "swhPortStatusPortFlowCtrl": swhPortStatusPortFlowCtrl,
       "swh8021QTagVLAN": swh8021QTagVLAN,
       "swh8021QTagVLANTable": swh8021QTagVLANTable,
       "swh8021QTagVLANEntry": swh8021QTagVLANEntry,
       "swh8021QTagVLANIndex": swh8021QTagVLANIndex,
       "swh8021QTagVLANVID": swh8021QTagVLANVID,
       "swh8021QTagVLANName": swh8021QTagVLANName,
       "swh8021QTagVLANPort1": swh8021QTagVLANPort1,
       "swh8021QTagVLANPort2": swh8021QTagVLANPort2,
       "swh8021QTagVLANPort3": swh8021QTagVLANPort3,
       "swh8021QTagVLANPort4": swh8021QTagVLANPort4,
       "swh8021QTagVLANPort5": swh8021QTagVLANPort5,
       "swh8021QTagVLANPort6": swh8021QTagVLANPort6,
       "swh8021QTagVLANCPU": swh8021QTagVLANCPU,
       "swhPortCountersRates": swhPortCountersRates,
       "swhCountersRatesTable": swhCountersRatesTable,
       "swhCountersRatesEntry": swhCountersRatesEntry,
       "swhCountersRatesIndex": swhCountersRatesIndex,
       "swhCountersRatesBytesReceived": swhCountersRatesBytesReceived,
       "swhCountersRatesFramesReceived": swhCountersRatesFramesReceived,
       "swhCountersRatesReceivedUtilization": swhCountersRatesReceivedUtilization,
       "swhCountersRatesBytesSent": swhCountersRatesBytesSent,
       "swhCountersRatesFramesSent": swhCountersRatesFramesSent,
       "swhCountersRatesSentUtilization": swhCountersRatesSentUtilization,
       "swhCountersRatesTotalBytes": swhCountersRatesTotalBytes,
       "swhCountersRatesTotalUtilization": swhCountersRatesTotalUtilization,
       "swhCountersRatesRxCRCError": swhCountersRatesRxCRCError,
       "swhCountersRatesRxFragments": swhCountersRatesRxFragments,
       "swhCountersRatesRxFilteredFrames": swhCountersRatesRxFilteredFrames,
       "swhCountersRatesRxAlignError": swhCountersRatesRxAlignError,
       "swhCountersRatesRxUndersizeFrames": swhCountersRatesRxUndersizeFrames,
       "swhCountersRatesRxOversizeFrames": swhCountersRatesRxOversizeFrames,
       "swhCountersRatesRxJabbers": swhCountersRatesRxJabbers,
       "swhCountersRatesRxDroppedFrames": swhCountersRatesRxDroppedFrames,
       "swhCountersRatesTxLateCollision": swhCountersRatesTxLateCollision,
       "swhCountersRatesTxDeferred": swhCountersRatesTxDeferred,
       "swhCountersRatesRxFrames64": swhCountersRatesRxFrames64,
       "swhCountersRatesRxFrames65to127": swhCountersRatesRxFrames65to127,
       "swhCountersRatesRxFrames128to255": swhCountersRatesRxFrames128to255,
       "swhCountersRatesRxFrames256to511": swhCountersRatesRxFrames256to511,
       "swhCountersRatesRxFrames512to1023": swhCountersRatesRxFrames512to1023,
       "swhCountersRatesRxMulticastFrames": swhCountersRatesRxMulticastFrames,
       "swhCountersRatesRxBroadcastFrames": swhCountersRatesRxBroadcastFrames,
       "swhCountersRatesTxMulticastFrames": swhCountersRatesTxMulticastFrames,
       "swhCountersRatesTxBroadcastFrames": swhCountersRatesTxBroadcastFrames,
       "swhCountersRatesTxCollision": swhCountersRatesTxCollision,
       "swhCountersRatesTotalErrors": swhCountersRatesTotalErrors,
       "swhCountersRatesRxFrames1024to1518": swhCountersRatesRxFrames1024to1518,
       "swhCountersRatesRxFrames1519toMaxSize": swhCountersRatesRxFrames1519toMaxSize,
       "swhPortCountersEvents": swhPortCountersEvents,
       "swhCountersEventsTable": swhCountersEventsTable,
       "swhCountersEventsEntry": swhCountersEventsEntry,
       "swhCountersEventsIndex": swhCountersEventsIndex,
       "swhCountersEventsBytesReceived": swhCountersEventsBytesReceived,
       "swhCountersEventsFramesReceived": swhCountersEventsFramesReceived,
       "swhCountersEventsBytesSent": swhCountersEventsBytesSent,
       "swhCountersEventsFramesSent": swhCountersEventsFramesSent,
       "swhCountersEventsTotalBytes": swhCountersEventsTotalBytes,
       "swhCountersEventsRxCRCError": swhCountersEventsRxCRCError,
       "swhCountersEventsRxFragments": swhCountersEventsRxFragments,
       "swhCountersEventsRxFilteredFrames": swhCountersEventsRxFilteredFrames,
       "swhCountersEventsRxAlignError": swhCountersEventsRxAlignError,
       "swhCountersEventsRxUndersizeFrames": swhCountersEventsRxUndersizeFrames,
       "swhCountersEventsRxOversizeFrames": swhCountersEventsRxOversizeFrames,
       "swhCountersEventsRxJabbers": swhCountersEventsRxJabbers,
       "swhCountersEventsRxDroppedFrames": swhCountersEventsRxDroppedFrames,
       "swhCountersEventsTxLateCollision": swhCountersEventsTxLateCollision,
       "swhCountersEventsTxDeferred": swhCountersEventsTxDeferred,
       "swhCountersEventsRxFrames64": swhCountersEventsRxFrames64,
       "swhCountersEventsRxFrames65to127": swhCountersEventsRxFrames65to127,
       "swhCountersEventsRxFrames128to255": swhCountersEventsRxFrames128to255,
       "swhCountersEventsRxFrames256to511": swhCountersEventsRxFrames256to511,
       "swhCountersEventsRxFrames512to1023": swhCountersEventsRxFrames512to1023,
       "swhCountersEventsRxMulticastFrames": swhCountersEventsRxMulticastFrames,
       "swhCountersEventsRxBroadcastFrames": swhCountersEventsRxBroadcastFrames,
       "swhCountersEventsTxMulticastFrames": swhCountersEventsTxMulticastFrames,
       "swhCountersEventsTxBroadcastFrames": swhCountersEventsTxBroadcastFrames,
       "swhCountersEventsTxCollision": swhCountersEventsTxCollision,
       "swhCountersEventsRxFrames1024to1518": swhCountersEventsRxFrames1024to1518,
       "swhCountersEventsRxFrames1519toMaxSize": swhCountersEventsRxFrames1519toMaxSize,
       "swhCountersEventsTotalErrors": swhCountersEventsTotalErrors,
       "swhCountersEventsClearCountersOfAllPort": swhCountersEventsClearCountersOfAllPort,
       "swhMacAddressTable": swhMacAddressTable,
       "swhMacAddressPortSelect": swhMacAddressPortSelect,
       "swhMacAddressClear": swhMacAddressClear,
       "swhMacAddressUpdate": swhMacAddressUpdate,
       "swhMacAddressTotal": swhMacAddressTotal,
       "swhMacAddressState": swhMacAddressState,
       "swhMacTable": swhMacTable,
       "swhMacTableEntry": swhMacTableEntry,
       "swhMacTableIndex": swhMacTableIndex,
       "swhMacTableAddr": swhMacTableAddr,
       "swhMacTableVID": swhMacTableVID,
       "swhMacTablePort": swhMacTablePort,
       "swhMacTableType": swhMacTableType,
       "swhMacAddressPageSelect": swhMacAddressPageSelect,
       "swhMacAddressVLANSelect": swhMacAddressVLANSelect,
       "swhMacAddressMACSelect": swhMacAddressMACSelect,
       "swhMacAddressCapacity": swhMacAddressCapacity,
       "swhMacAddressFree": swhMacAddressFree,
       "swhMacAddressUsed": swhMacAddressUsed,
       "swhMacAddressDynamic": swhMacAddressDynamic,
       "swhMacAddressStatic": swhMacAddressStatic,
       "swhMacAddressInternal": swhMacAddressInternal,
       "swhRSTPBridgeOverview": swhRSTPBridgeOverview,
       "swhRSTPBridgeTable": swhRSTPBridgeTable,
       "swhRSTPBridgeEntry": swhRSTPBridgeEntry,
       "swhRSTPBridgeIndex": swhRSTPBridgeIndex,
       "swhRSTPBridgeBridgeID": swhRSTPBridgeBridgeID,
       "swhRSTPBridgeMaxAge": swhRSTPBridgeMaxAge,
       "swhRSTPBridgeHelloTime": swhRSTPBridgeHelloTime,
       "swhRSTPBridgeFwdDelay": swhRSTPBridgeFwdDelay,
       "swhRSTPBridgeTopology": swhRSTPBridgeTopology,
       "swhRSTPBridgeRootID": swhRSTPBridgeRootID,
       "swhRSTPBridgeRootPort": swhRSTPBridgeRootPort,
       "swhLLDPStatus": swhLLDPStatus,
       "swhLLDPStatusTable": swhLLDPStatusTable,
       "swhLLDPStatusTableEntry": swhLLDPStatusTableEntry,
       "swhLLDPStatusTableIndex": swhLLDPStatusTableIndex,
       "swhLLDPStatusTableChassisID": swhLLDPStatusTableChassisID,
       "swhLLDPStatusTableRemotePort": swhLLDPStatusTableRemotePort,
       "swhLLDPStatusTableSystemName": swhLLDPStatusTableSystemName,
       "swhLLDPStatusTablePortDescription": swhLLDPStatusTablePortDescription,
       "swhLLDPStatusTableSystemCapabilities": swhLLDPStatusTableSystemCapabilities,
       "swhLLDPStatusTableManagement1Address": swhLLDPStatusTableManagement1Address,
       "swhLLDPStatusTableManagement2Address": swhLLDPStatusTableManagement2Address,
       "swhLLDPStatusTableManagement3Address": swhLLDPStatusTableManagement3Address,
       "swhLLDPStatusTableManagement4Address": swhLLDPStatusTableManagement4Address,
       "swhLLDPStatusTableManagement5Address": swhLLDPStatusTableManagement5Address,
       "swhRSTPPortStatus": swhRSTPPortStatus,
       "swhRSTPPortStatusTable": swhRSTPPortStatusTable,
       "swhRSTPPortStatusEntry": swhRSTPPortStatusEntry,
       "swhRSTPPortStatusIndex": swhRSTPPortStatusIndex,
       "swhRSTPPortStatusPathCost": swhRSTPPortStatusPathCost,
       "swhRSTPPortStatusEdgePort": swhRSTPPortStatusEdgePort,
       "swhRSTPPortStatusP2pPort": swhRSTPPortStatusP2pPort,
       "swhRSTPPortStatusProtocol": swhRSTPPortStatusProtocol,
       "swhRSTPPortStatusRole": swhRSTPPortStatusRole,
       "swhRSTPPortStatusPortState": swhRSTPPortStatusPortState,
       "swhRSTPPortStatusPort": swhRSTPPortStatusPort,
       "swhRSTPStatistics": swhRSTPStatistics,
       "swhRSTPStatisticsTable": swhRSTPStatisticsTable,
       "swhRSTPStatisticsEntry": swhRSTPStatisticsEntry,
       "swhRSTPStatisticsIndex": swhRSTPStatisticsIndex,
       "swhRSTPStatisticsRSTPTransmitted": swhRSTPStatisticsRSTPTransmitted,
       "swhRSTPStatisticsSTPTransmitted": swhRSTPStatisticsSTPTransmitted,
       "swhRSTPStatisticsTCNTransmitted": swhRSTPStatisticsTCNTransmitted,
       "swhRSTPStatisticsRSTPReceived": swhRSTPStatisticsRSTPReceived,
       "swhRSTPStatisticsSTPReceived": swhRSTPStatisticsSTPReceived,
       "swhRSTPStatisticsTCNReceived": swhRSTPStatisticsTCNReceived,
       "swhRSTPStatisticsIllegalReceived": swhRSTPStatisticsIllegalReceived,
       "swhRSTPStatisticsUnknownReceived": swhRSTPStatisticsUnknownReceived,
       "swhRSTPStatisticsPort": swhRSTPStatisticsPort,
       "swhLACPPortStatus": swhLACPPortStatus,
       "swhLACPPortStatusTable": swhLACPPortStatusTable,
       "swhLACPPortStatusEntry": swhLACPPortStatusEntry,
       "swhLACPPortStatusIndex": swhLACPPortStatusIndex,
       "swhLACPPortStatusPartnerPort": swhLACPPortStatusPartnerPort,
       "swhLACPPortStatusLACPOperationalState": swhLACPPortStatusLACPOperationalState,
       "swhLACPPortStatusKey": swhLACPPortStatusKey,
       "swhLACPPortStatusAggrID": swhLACPPortStatusAggrID,
       "swhLACPPortStatusPartnerID": swhLACPPortStatusPartnerID,
       "swhLACPStatistics": swhLACPStatistics,
       "swhLACPStatisticsTable": swhLACPStatisticsTable,
       "swhLACPStatisticsEntry": swhLACPStatisticsEntry,
       "swhLACPStatisticsIndex": swhLACPStatisticsIndex,
       "swhLACPStatisticsLACPTransmitted": swhLACPStatisticsLACPTransmitted,
       "swhLACPStatisticsLACPReceived": swhLACPStatisticsLACPReceived,
       "swhLACPStatisticsIllegalReceived": swhLACPStatisticsIllegalReceived,
       "swhLACPStatisticsUnknownReceived": swhLACPStatisticsUnknownReceived,
       "swhLACPStatisticsClear": swhLACPStatisticsClear,
       "swhLACPStatisticsClearCountersOfAllPort": swhLACPStatisticsClearCountersOfAllPort,
       "swhLayer2ProtocolTunnelStatus": swhLayer2ProtocolTunnelStatus,
       "swhL2PTStatusClearCountersOfAllPort": swhL2PTStatusClearCountersOfAllPort,
       "swhL2PTStatusPortSelect": swhL2PTStatusPortSelect,
       "swhL2PTStatusPortClear": swhL2PTStatusPortClear,
       "swhL2PTStatusTable": swhL2PTStatusTable,
       "swhL2PTStatusEntry": swhL2PTStatusEntry,
       "swhL2PTStatusIndex": swhL2PTStatusIndex,
       "swhL2PTStatusCounterName": swhL2PTStatusCounterName,
       "swhL2PTStatusState": swhL2PTStatusState,
       "swhL2PTStatusEncapsulationCounters": swhL2PTStatusEncapsulationCounters,
       "swhL2PTStatusDecapsulationCounters": swhL2PTStatusDecapsulationCounters,
       "swhIGMPStatus": swhIGMPStatus,
       "swhIGMPStatusTable": swhIGMPStatusTable,
       "swhIGMPStatusEntry": swhIGMPStatusEntry,
       "swhIGMPStatusIndex": swhIGMPStatusIndex,
       "swhIGMPStatusVLANID": swhIGMPStatusVLANID,
       "swhIGMPStatusQuerier": swhIGMPStatusQuerier,
       "swhIGMPStatusQueriesTransmitted": swhIGMPStatusQueriesTransmitted,
       "swhIGMPStatusQueriesReceived": swhIGMPStatusQueriesReceived,
       "swhIGMPStatusV1Reports": swhIGMPStatusV1Reports,
       "swhIGMPStatusV2Reports": swhIGMPStatusV2Reports,
       "swhIGMPStatusV3Reports": swhIGMPStatusV3Reports,
       "swhIGMPStatusV2Leaves": swhIGMPStatusV2Leaves,
       "swhMLDStatus": swhMLDStatus,
       "swhMLDStatusTable": swhMLDStatusTable,
       "swhMLDStatusEntry": swhMLDStatusEntry,
       "swhMLDStatusIndex": swhMLDStatusIndex,
       "swhMLDStatusVLANID": swhMLDStatusVLANID,
       "swhMLDStatusQuerier": swhMLDStatusQuerier,
       "swhMLDStatusQueriesTransmitted": swhMLDStatusQueriesTransmitted,
       "swhMLDStatusQueriesReceived": swhMLDStatusQueriesReceived,
       "swhMLDStatusV1Reports": swhMLDStatusV1Reports,
       "swhMLDStatusV2Reports": swhMLDStatusV2Reports,
       "swhMLDStatusDone": swhMLDStatusDone,
       "swhIGMPGroupTable": swhIGMPGroupTable,
       "swhIGMPState": swhIGMPState,
       "swhIGMPTable": swhIGMPTable,
       "swhIGMPTableEntry": swhIGMPTableEntry,
       "swhIGMPGroupTableIndex": swhIGMPGroupTableIndex,
       "swhIGMPGroupTableGroup": swhIGMPGroupTableGroup,
       "swhIGMPGroupTablePort1": swhIGMPGroupTablePort1,
       "swhIGMPGroupTablePort2": swhIGMPGroupTablePort2,
       "swhIGMPGroupTablePort3": swhIGMPGroupTablePort3,
       "swhIGMPGroupTablePort4": swhIGMPGroupTablePort4,
       "swhIGMPGroupTablePort5": swhIGMPGroupTablePort5,
       "swhIGMPGroupTablePort6": swhIGMPGroupTablePort6,
       "swhIGMPGroupTableVID": swhIGMPGroupTableVID,
       "swhMLDGroupTable": swhMLDGroupTable,
       "swhMLDState": swhMLDState,
       "swhMLDTable": swhMLDTable,
       "swhMLDTableEntry": swhMLDTableEntry,
       "swhMLDGroupTableIndex": swhMLDGroupTableIndex,
       "swhMLDGroupTableGroup": swhMLDGroupTableGroup,
       "swhMLDGroupTablePort1": swhMLDGroupTablePort1,
       "swhMLDGroupTablePort2": swhMLDGroupTablePort2,
       "swhMLDGroupTablePort3": swhMLDGroupTablePort3,
       "swhMLDGroupTablePort4": swhMLDGroupTablePort4,
       "swhMLDGroupTablePort5": swhMLDGroupTablePort5,
       "swhMLDGroupTablePort6": swhMLDGroupTablePort6,
       "swhMLDGroupTableVID": swhMLDGroupTableVID,
       "swh8021XPortStatus": swh8021XPortStatus,
       "swh8021XPortStatusTable": swh8021XPortStatusTable,
       "swh8021XPortStatusEntry": swh8021XPortStatusEntry,
       "swh8021XPortStatusIndex": swh8021XPortStatusIndex,
       "swh8021XPortStatusState": swh8021XPortStatusState,
       "swh8021XPortStatusLastSource": swh8021XPortStatusLastSource,
       "swh8021XPortStatusLastID": swh8021XPortStatusLastID,
       "swh8021XPortStatusAssignedVLAN": swh8021XPortStatusAssignedVLAN,
       "swh8021XStatistics": swh8021XStatistics,
       "swh8021XStatisticsTable": swh8021XStatisticsTable,
       "swh8021XStatisticsEntry": swh8021XStatisticsEntry,
       "swh8021XStatisticsIndex": swh8021XStatisticsIndex,
       "swh8021XStatisticsRxTotal": swh8021XStatisticsRxTotal,
       "swh8021XStatisticsRxResponseID": swh8021XStatisticsRxResponseID,
       "swh8021XStatisticsRxResponse": swh8021XStatisticsRxResponse,
       "swh8021XStatisticsRxStart": swh8021XStatisticsRxStart,
       "swh8021XStatisticsRxLogoff": swh8021XStatisticsRxLogoff,
       "swh8021XStatisticsRxInvalidType": swh8021XStatisticsRxInvalidType,
       "swh8021XStatisticsRxInvalidLength": swh8021XStatisticsRxInvalidLength,
       "swh8021XStatisticsRxAccessChallenges": swh8021XStatisticsRxAccessChallenges,
       "swh8021XStatisticsRxOtherRequests": swh8021XStatisticsRxOtherRequests,
       "swh8021XStatisticsRxAuthSuccesses": swh8021XStatisticsRxAuthSuccesses,
       "swh8021XStatisticsRxAuthFailures": swh8021XStatisticsRxAuthFailures,
       "swh8021XStatisticsTxTotal": swh8021XStatisticsTxTotal,
       "swh8021XStatisticsTxRequestID": swh8021XStatisticsTxRequestID,
       "swh8021XStatisticsTxRequest": swh8021XStatisticsTxRequest,
       "swh8021XStatisticsTxResponses": swh8021XStatisticsTxResponses,
       "swh8021XStatisticsClear": swh8021XStatisticsClear,
       "swh8021XStatisticsClearCountersOfAllPort": swh8021XStatisticsClearCountersOfAllPort,
       "swhSFPInformation": swhSFPInformation,
       "swhSFPPortInfo": swhSFPPortInfo,
       "swhSFPPortInfoTable": swhSFPPortInfoTable,
       "swhSFPPortInfoEntry": swhSFPPortInfoEntry,
       "swhSFPPortInfoIndex": swhSFPPortInfoIndex,
       "swhSFPPortInfoPortName": swhSFPPortInfoPortName,
       "swhSFPPortInfoSpeed": swhSFPPortInfoSpeed,
       "swhSFPPortInfoDistance": swhSFPPortInfoDistance,
       "swhSFPPortInfoVendorName": swhSFPPortInfoVendorName,
       "swhSFPPortInfoVendorPN": swhSFPPortInfoVendorPN,
       "swhSFPPortInfoVendorSN": swhSFPPortInfoVendorSN,
       "swhSFPPortState": swhSFPPortState,
       "swhSFPPortStateTable": swhSFPPortStateTable,
       "swhSFPPortStateEntry": swhSFPPortStateEntry,
       "swhSFPPortStateIndex": swhSFPPortStateIndex,
       "swhSFPPortStatePortName": swhSFPPortStatePortName,
       "swhSFPPortStateTemperature": swhSFPPortStateTemperature,
       "swhSFPPortStateVoltage": swhSFPPortStateVoltage,
       "swhSFPPortStateTXBias": swhSFPPortStateTXBias,
       "swhSFPPortStateTXPower": swhSFPPortStateTXPower,
       "swhSFPPortStateRXPower": swhSFPPortStateRXPower,
       "swhDHCPSnoopingTable": swhDHCPSnoopingTable,
       "swhDHCPSnoopingTableTable": swhDHCPSnoopingTableTable,
       "swhDHCPSnoopingTableEntry": swhDHCPSnoopingTableEntry,
       "swhDHCPSnoopingTableIndex": swhDHCPSnoopingTableIndex,
       "swhDHCPSnoopingTableCliPort": swhDHCPSnoopingTableCliPort,
       "swhDHCPSnoopingTableSrvPort": swhDHCPSnoopingTableSrvPort,
       "swhDHCPSnoopingTableVID": swhDHCPSnoopingTableVID,
       "swhDHCPSnoopingTableCliIPAddr": swhDHCPSnoopingTableCliIPAddr,
       "swhDHCPSnoopingTableCliMacAddr": swhDHCPSnoopingTableCliMacAddr,
       "swhDHCPSnoopingTableSrvIPAddr": swhDHCPSnoopingTableSrvIPAddr,
       "swhDHCPSnoopingTableTimeLeft": swhDHCPSnoopingTableTimeLeft,
       "swhDHCPv6SnoopingTableTable": swhDHCPv6SnoopingTableTable,
       "swhDHCPv6SnoopingTableEntry": swhDHCPv6SnoopingTableEntry,
       "swhDHCPv6SnoopingTableIndex": swhDHCPv6SnoopingTableIndex,
       "swhDHCPv6SnoopingTableCliPort": swhDHCPv6SnoopingTableCliPort,
       "swhDHCPv6SnoopingTableSrvPort": swhDHCPv6SnoopingTableSrvPort,
       "swhDHCPv6SnoopingTableVID": swhDHCPv6SnoopingTableVID,
       "swhDHCPv6SnoopingTableCliIPAddr": swhDHCPv6SnoopingTableCliIPAddr,
       "swhDHCPv6SnoopingTableCliMacAddr": swhDHCPv6SnoopingTableCliMacAddr,
       "swhDHCPv6SnoopingTableSrvIPAddr": swhDHCPv6SnoopingTableSrvIPAddr,
       "swhDHCPv6SnoopingTableTimeLeft": swhDHCPv6SnoopingTableTimeLeft,
       "swhLoopDetectionStatus": swhLoopDetectionStatus,
       "swhLoopDetectionStatusUpdate": swhLoopDetectionStatusUpdate,
       "swhLoopDetectionStatusTable": swhLoopDetectionStatusTable,
       "swhLoopDetectionStatusEntry": swhLoopDetectionStatusEntry,
       "swhLoopDetectionStatusPort": swhLoopDetectionStatusPort,
       "swhLoopDetectionStatusLockCause": swhLoopDetectionStatusLockCause,
       "swhLoopDetectionStatusStatus": swhLoopDetectionStatusStatus,
       "swhMacLimitersStatus": swhMacLimitersStatus,
       "swhMacLimitersStatusTable": swhMacLimitersStatusTable,
       "swhMacLimitersStatusEntry": swhMacLimitersStatusEntry,
       "swhMacLimitersStatusPort": swhMacLimitersStatusPort,
       "swhMacLimitersStatusLimit": swhMacLimitersStatusLimit,
       "swhMacLimitersStatusCurrent": swhMacLimitersStatusCurrent,
       "swhDIDOStatus": swhDIDOStatus,
       "swhDIStatusTable": swhDIStatusTable,
       "swhDIStatusEntry": swhDIStatusEntry,
       "swhDIStatusIndex": swhDIStatusIndex,
       "swhDIStatusStatus": swhDIStatusStatus,
       "swhDIStatusAlarm": swhDIStatusAlarm,
       "swhDOStatusTable": swhDOStatusTable,
       "swhDOStatusEntry": swhDOStatusEntry,
       "swhDOStatusIndex": swhDOStatusIndex,
       "swhDOStatusStatus": swhDOStatusStatus,
       "swhDOStatusAlarm": swhDOStatusAlarm,
       "swhDOStatusTrigger": swhDOStatusTrigger,
       "swhDOStatusDigitalInput1": swhDOStatusDigitalInput1,
       "swhDOStatusPower1": swhDOStatusPower1,
       "swhDOStatusPower2": swhDOStatusPower2,
       "swhDOPortStatusTable": swhDOPortStatusTable,
       "swhDOPortStatusEntry": swhDOPortStatusEntry,
       "swhDOPortStatusIndex": swhDOPortStatusIndex,
       "swhDOPortStatusDigitalOutput1Status": swhDOPortStatusDigitalOutput1Status,
       "swhRingStatus": swhRingStatus,
       "swhRingState": swhRingState,
       "swhRingStatusTable": swhRingStatusTable,
       "swhRingStatusEntry": swhRingStatusEntry,
       "swhRingStatusIndex": swhRingStatusIndex,
       "swhRingStatusEnable": swhRingStatusEnable,
       "swhRingStatusState": swhRingStatusState,
       "swhRingStateAccording": swhRingStateAccording,
       "swhRingStateRole": swhRingStateRole,
       "swhPOEStatus": swhPOEStatus,
       "swhPOETotalPower": swhPOETotalPower,
       "swhPOEStatusTable": swhPOEStatusTable,
       "swhPOEStatusEntry": swhPOEStatusEntry,
       "swhPOEStatusIndex": swhPOEStatusIndex,
       "swhPOEStatusPort": swhPOEStatusPort,
       "swhPOEStatusName": swhPOEStatusName,
       "swhPOEStatusPower": swhPOEStatusPower,
       "swhPOEStatusVoltage": swhPOEStatusVoltage,
       "swhPOEStatusCurrent": swhPOEStatusCurrent,
       "swhPOEStatusPDClass": swhPOEStatusPDClass,
       "swhPOEStatusPoEDetection": swhPOEStatusPoEDetection,
       "swhPOEStatusOperationMode": swhPOEStatusOperationMode,
       "swhCPUTemperatureStatus": swhCPUTemperatureStatus,
       "swhCPUHighTemperatureThreshold": swhCPUHighTemperatureThreshold,
       "swhCPUThresholdInterval": swhCPUThresholdInterval,
       "swhCPUContinuousAlarm": swhCPUContinuousAlarm,
       "swhCPUCurrentCPUTemperature": swhCPUCurrentCPUTemperature,
       "swhCPUHistoricalHighCPUTemperature": swhCPUHistoricalHighCPUTemperature,
       "swhCPUHistoricalHighElapsedTime": swhCPUHistoricalHighElapsedTime,
       "swhCPUHistoricalLowCPUTemperature": swhCPUHistoricalLowCPUTemperature,
       "swhCPUHistoricalLowElapsedTime": swhCPUHistoricalLowElapsedTime,
       "swhFastRedundancyStatus": swhFastRedundancyStatus,
       "swhFastRedundancyStatusTable": swhFastRedundancyStatusTable,
       "swhFastRedundancyStatusEntry": swhFastRedundancyStatusEntry,
       "swhFastRedundancyStatusIndex": swhFastRedundancyStatusIndex,
       "swhFastRedundancyStatusGroupID": swhFastRedundancyStatusGroupID,
       "swhFastRedundancyStatusDescription": swhFastRedundancyStatusDescription,
       "swhFastRedundancyStatusEnable": swhFastRedundancyStatusEnable,
       "swhFastRedundancyStatusProtocol": swhFastRedundancyStatusProtocol,
       "swhFastRedundancyStatusRole": swhFastRedundancyStatusRole,
       "swhFastRedundancyStatusStatus": swhFastRedundancyStatusStatus,
       "swhFastRedundancyStatusPort1": swhFastRedundancyStatusPort1,
       "swhFastRedundancyStatusPort1Role": swhFastRedundancyStatusPort1Role,
       "swhFastRedundancyStatusPort1Statue": swhFastRedundancyStatusPort1Statue,
       "swhFastRedundancyStatusPort2": swhFastRedundancyStatusPort2,
       "swhFastRedundancyStatusPort2Role": swhFastRedundancyStatusPort2Role,
       "swhFastRedundancyStatusPort2Statue": swhFastRedundancyStatusPort2Statue,
       "swhRingStatusTimes": swhRingStatusTimes,
       "swhRingStatusLastChangeTime": swhRingStatusLastChangeTime,
       "swhRingStatusElapsedTime": swhRingStatusElapsedTime,
       "swhRingStatusTopologyClear": swhRingStatusTopologyClear,
       "swhFastRedundancyStatisticsTable": swhFastRedundancyStatisticsTable,
       "swhFastRedundancyStatisticsEntry": swhFastRedundancyStatisticsEntry,
       "swhFastRedundancyEntry": swhFastRedundancyEntry,
       "swhFastRedundancyTxNormal": swhFastRedundancyTxNormal,
       "swhFastRedundancyTxFailure": swhFastRedundancyTxFailure,
       "swhFastRedundancyRxNormal": swhFastRedundancyRxNormal,
       "swhFastRedundancyRxFailure": swhFastRedundancyRxFailure,
       "swhFastRedundancyCountersClear": swhFastRedundancyCountersClear,
       "swhSystemUtility": swhSystemUtility,
       "swhLoadFactorySetting": swhLoadFactorySetting,
       "swhLoadFactorySettingExceptNetworkConfiguration": swhLoadFactorySettingExceptNetworkConfiguration,
       "swhEventLog": swhEventLog,
       "swhEventLogTable": swhEventLogTable,
       "swhEventLogEntry": swhEventLogEntry,
       "swhEventLogIndex": swhEventLogIndex,
       "swhEventLogType": swhEventLogType,
       "swhEventLogTime": swhEventLogTime,
       "swhEventLogUpTime": swhEventLogUpTime,
       "swhEventLogDescription": swhEventLogDescription,
       "swhEventLogSource": swhEventLogSource,
       "swhEventLogEvent": swhEventLogEvent,
       "swhEventLogNameCommunity": swhEventLogNameCommunity,
       "swhEventLogIPAddr": swhEventLogIPAddr,
       "swhEventLogClear": swhEventLogClear,
       "swhUpdateFirmware": swhUpdateFirmware,
       "swhUpdateProtocol": swhUpdateProtocol,
       "swhUpdateFileType": swhUpdateFileType,
       "swhUpdateServerIPAddr": swhUpdateServerIPAddr,
       "swhUpdateUserName": swhUpdateUserName,
       "swhUpdatePassword": swhUpdatePassword,
       "swhUpdateFileLocation": swhUpdateFileLocation,
       "swhUpdatePut": swhUpdatePut,
       "swhUpdateUpdate": swhUpdateUpdate,
       "swhUpdateState": swhUpdateState,
       "swhUpdateServerIPv6Addr": swhUpdateServerIPv6Addr,
       "swhUpdateConfigeType": swhUpdateConfigeType,
       "swhUpdateImageOption": swhUpdateImageOption,
       "swhAutoBackupConfiguration": swhAutoBackupConfiguration,
       "swhBackupAuto": swhBackupAuto,
       "swhBackupTime": swhBackupTime,
       "swhBackupProtocol": swhBackupProtocol,
       "swhBackupFileType": swhBackupFileType,
       "swhBackupServerIPAddr": swhBackupServerIPAddr,
       "swhBackupUserName": swhBackupUserName,
       "swhBackupPassword": swhBackupPassword,
       "swhBackupFileDirectory": swhBackupFileDirectory,
       "swhBackupFileName": swhBackupFileName,
       "swhBackupState": swhBackupState,
       "swhBackupTrigger": swhBackupTrigger,
       "swhBackupNTPStatus": swhBackupNTPStatus,
       "swhLoopbackTest": swhLoopbackTest,
       "swhDiagnosticPort": swhDiagnosticPort,
       "swhVlanID": swhVlanID,
       "swhTestTime": swhTestTime,
       "swhState": swhState,
       "swhTimeRemaining": swhTimeRemaining,
       "swhLoopbackStop": swhLoopbackStop,
       "swhStop": swhStop,
       "swhSaveConfiguration": swhSaveConfiguration,
       "swhResetSystem": swhResetSystem,
       "switchTraps": switchTraps,
       "swhSystemPowerDown": swhSystemPowerDown,
       "swhFaultAlarm": swhFaultAlarm,
       "swhWarningAlarm": swhWarningAlarm,
       "swhMinorAlarm": swhMinorAlarm,
       "swhCriticalAlarm": swhCriticalAlarm,
       "swhLoopBack": swhLoopBack,
       "swhNormalAlarm": swhNormalAlarm,
       "swhCaseFanState": swhCaseFanState,
       "swhSystemPowerOn": swhSystemPowerOn,
       "swhSystemPowerUp": swhSystemPowerUp,
       "swhNewBootUpImage": swhNewBootUpImage}
)
