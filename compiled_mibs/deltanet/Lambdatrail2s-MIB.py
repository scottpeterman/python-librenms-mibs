# SNMP MIB module (Lambdatrail2s-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\deltanet\Lambdatrail2s-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:23 2025
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

(deltanet,) = mibBuilder.importSymbols(
    "Deltanet-MIB",
    "deltanet")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lambdatrail2s = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 5)
)
if mibBuilder.loadTexts:
    lambdatrail2s.setRevisions(
        ("2015-02-10 00:00",
         "2015-01-20 00:00",
         "2015-01-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lt2sNotifications_ObjectIdentity = ObjectIdentity
lt2sNotifications = _Lt2sNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0)
)
_Lt2sAgent_ObjectIdentity = ObjectIdentity
lt2sAgent = _Lt2sAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1)
)


class _Lt2sDescription_Type(DisplayString):
    """Custom type lt2sDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Lt2sDescription_Type.__name__ = "DisplayString"
_Lt2sDescription_Object = MibScalar
lt2sDescription = _Lt2sDescription_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 1),
    _Lt2sDescription_Type()
)
lt2sDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sDescription.setStatus("current")


class _Lt2sDeviceType_Type(DisplayString):
    """Custom type lt2sDeviceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Lt2sDeviceType_Type.__name__ = "DisplayString"
_Lt2sDeviceType_Object = MibScalar
lt2sDeviceType = _Lt2sDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 2),
    _Lt2sDeviceType_Type()
)
lt2sDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sDeviceType.setStatus("current")


class _Lt2sHwRevision_Type(DisplayString):
    """Custom type lt2sHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Lt2sHwRevision_Type.__name__ = "DisplayString"
_Lt2sHwRevision_Object = MibScalar
lt2sHwRevision = _Lt2sHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 3),
    _Lt2sHwRevision_Type()
)
lt2sHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sHwRevision.setStatus("current")


class _Lt2sManufacturingDate_Type(DisplayString):
    """Custom type lt2sManufacturingDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Lt2sManufacturingDate_Type.__name__ = "DisplayString"
_Lt2sManufacturingDate_Object = MibScalar
lt2sManufacturingDate = _Lt2sManufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 4),
    _Lt2sManufacturingDate_Type()
)
lt2sManufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sManufacturingDate.setStatus("current")


class _Lt2sSerialNumber_Type(DisplayString):
    """Custom type lt2sSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Lt2sSerialNumber_Type.__name__ = "DisplayString"
_Lt2sSerialNumber_Object = MibScalar
lt2sSerialNumber = _Lt2sSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 5),
    _Lt2sSerialNumber_Type()
)
lt2sSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sSerialNumber.setStatus("current")


class _Lt2sSystemName_Type(DisplayString):
    """Custom type lt2sSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Lt2sSystemName_Type.__name__ = "DisplayString"
_Lt2sSystemName_Object = MibScalar
lt2sSystemName = _Lt2sSystemName_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 6),
    _Lt2sSystemName_Type()
)
lt2sSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sSystemName.setStatus("current")


class _Lt2sSystemLocation_Type(DisplayString):
    """Custom type lt2sSystemLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Lt2sSystemLocation_Type.__name__ = "DisplayString"
_Lt2sSystemLocation_Object = MibScalar
lt2sSystemLocation = _Lt2sSystemLocation_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 7),
    _Lt2sSystemLocation_Type()
)
lt2sSystemLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sSystemLocation.setStatus("current")


class _Lt2sSystemContact_Type(DisplayString):
    """Custom type lt2sSystemContact based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Lt2sSystemContact_Type.__name__ = "DisplayString"
_Lt2sSystemContact_Object = MibScalar
lt2sSystemContact = _Lt2sSystemContact_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 8),
    _Lt2sSystemContact_Type()
)
lt2sSystemContact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sSystemContact.setStatus("current")


class _Lt2sSystemUptime_Type(DisplayString):
    """Custom type lt2sSystemUptime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_Lt2sSystemUptime_Type.__name__ = "DisplayString"
_Lt2sSystemUptime_Object = MibScalar
lt2sSystemUptime = _Lt2sSystemUptime_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 9),
    _Lt2sSystemUptime_Type()
)
lt2sSystemUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sSystemUptime.setStatus("current")


class _Lt2sFirmwareVersion_Type(DisplayString):
    """Custom type lt2sFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Lt2sFirmwareVersion_Type.__name__ = "DisplayString"
_Lt2sFirmwareVersion_Object = MibScalar
lt2sFirmwareVersion = _Lt2sFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 10),
    _Lt2sFirmwareVersion_Type()
)
lt2sFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sFirmwareVersion.setStatus("current")


class _Lt2suCVersion_Type(DisplayString):
    """Custom type lt2suCVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 63),
    )


_Lt2suCVersion_Type.__name__ = "DisplayString"
_Lt2suCVersion_Object = MibScalar
lt2suCVersion = _Lt2suCVersion_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 11),
    _Lt2suCVersion_Type()
)
lt2suCVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2suCVersion.setStatus("current")


class _Lt2sSaveRunningCfg_Type(Integer32):
    """Custom type lt2sSaveRunningCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("saveConfig", 2))
    )


_Lt2sSaveRunningCfg_Type.__name__ = "Integer32"
_Lt2sSaveRunningCfg_Object = MibScalar
lt2sSaveRunningCfg = _Lt2sSaveRunningCfg_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 12),
    _Lt2sSaveRunningCfg_Type()
)
lt2sSaveRunningCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sSaveRunningCfg.setStatus("current")


class _Lt2sResetAgent_Type(Integer32):
    """Custom type lt2sResetAgent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("resetAgent", 2))
    )


_Lt2sResetAgent_Type.__name__ = "Integer32"
_Lt2sResetAgent_Object = MibScalar
lt2sResetAgent = _Lt2sResetAgent_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 13),
    _Lt2sResetAgent_Type()
)
lt2sResetAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sResetAgent.setStatus("current")


class _Lt2sSnmpGetCommunity_Type(DisplayString):
    """Custom type lt2sSnmpGetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Lt2sSnmpGetCommunity_Type.__name__ = "DisplayString"
_Lt2sSnmpGetCommunity_Object = MibScalar
lt2sSnmpGetCommunity = _Lt2sSnmpGetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 14),
    _Lt2sSnmpGetCommunity_Type()
)
lt2sSnmpGetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sSnmpGetCommunity.setStatus("current")


class _Lt2sSnmpSetCommunity_Type(DisplayString):
    """Custom type lt2sSnmpSetCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Lt2sSnmpSetCommunity_Type.__name__ = "DisplayString"
_Lt2sSnmpSetCommunity_Object = MibScalar
lt2sSnmpSetCommunity = _Lt2sSnmpSetCommunity_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 15),
    _Lt2sSnmpSetCommunity_Type()
)
lt2sSnmpSetCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sSnmpSetCommunity.setStatus("current")


class _Lt2sIp4DHCP_Type(Integer32):
    """Custom type lt2sIp4DHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Lt2sIp4DHCP_Type.__name__ = "Integer32"
_Lt2sIp4DHCP_Object = MibScalar
lt2sIp4DHCP = _Lt2sIp4DHCP_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 16),
    _Lt2sIp4DHCP_Type()
)
lt2sIp4DHCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sIp4DHCP.setStatus("current")
_Lt2sIp4Address_Type = IpAddress
_Lt2sIp4Address_Object = MibScalar
lt2sIp4Address = _Lt2sIp4Address_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 17),
    _Lt2sIp4Address_Type()
)
lt2sIp4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sIp4Address.setStatus("current")
_Lt2sIp4Mask_Type = IpAddress
_Lt2sIp4Mask_Object = MibScalar
lt2sIp4Mask = _Lt2sIp4Mask_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 18),
    _Lt2sIp4Mask_Type()
)
lt2sIp4Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sIp4Mask.setStatus("current")
_Lt2sIp4Gateway_Type = IpAddress
_Lt2sIp4Gateway_Object = MibScalar
lt2sIp4Gateway = _Lt2sIp4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 19),
    _Lt2sIp4Gateway_Type()
)
lt2sIp4Gateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sIp4Gateway.setStatus("current")
_Lt2sIp4PrimaryDns_Type = IpAddress
_Lt2sIp4PrimaryDns_Object = MibScalar
lt2sIp4PrimaryDns = _Lt2sIp4PrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 20),
    _Lt2sIp4PrimaryDns_Type()
)
lt2sIp4PrimaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sIp4PrimaryDns.setStatus("current")
_Lt2sIp4SecondaryDns_Type = IpAddress
_Lt2sIp4SecondaryDns_Object = MibScalar
lt2sIp4SecondaryDns = _Lt2sIp4SecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 21),
    _Lt2sIp4SecondaryDns_Type()
)
lt2sIp4SecondaryDns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sIp4SecondaryDns.setStatus("current")


class _Lt2sSnmpServer_Type(Integer32):
    """Custom type lt2sSnmpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Lt2sSnmpServer_Type.__name__ = "Integer32"
_Lt2sSnmpServer_Object = MibScalar
lt2sSnmpServer = _Lt2sSnmpServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 22),
    _Lt2sSnmpServer_Type()
)
lt2sSnmpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sSnmpServer.setStatus("current")


class _Lt2sHttpServer_Type(Integer32):
    """Custom type lt2sHttpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Lt2sHttpServer_Type.__name__ = "Integer32"
_Lt2sHttpServer_Object = MibScalar
lt2sHttpServer = _Lt2sHttpServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 23),
    _Lt2sHttpServer_Type()
)
lt2sHttpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sHttpServer.setStatus("current")


class _Lt2sTelnetServer_Type(Integer32):
    """Custom type lt2sTelnetServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Lt2sTelnetServer_Type.__name__ = "Integer32"
_Lt2sTelnetServer_Object = MibScalar
lt2sTelnetServer = _Lt2sTelnetServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 24),
    _Lt2sTelnetServer_Type()
)
lt2sTelnetServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sTelnetServer.setStatus("current")


class _Lt2sFtpServer_Type(Integer32):
    """Custom type lt2sFtpServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Lt2sFtpServer_Type.__name__ = "Integer32"
_Lt2sFtpServer_Object = MibScalar
lt2sFtpServer = _Lt2sFtpServer_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 25),
    _Lt2sFtpServer_Type()
)
lt2sFtpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sFtpServer.setStatus("current")
_Lt2sMgmtPortTable_Object = MibTable
lt2sMgmtPortTable = _Lt2sMgmtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26)
)
if mibBuilder.loadTexts:
    lt2sMgmtPortTable.setStatus("current")
_Lt2sMgmtPortEntry_Object = MibTableRow
lt2sMgmtPortEntry = _Lt2sMgmtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1)
)
lt2sMgmtPortEntry.setIndexNames(
    (0, "Lambdatrail2s-MIB", "lt2sMgmtPortId"),
)
if mibBuilder.loadTexts:
    lt2sMgmtPortEntry.setStatus("current")


class _Lt2sMgmtPortId_Type(Integer32):
    """Custom type lt2sMgmtPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Lt2sMgmtPortId_Type.__name__ = "Integer32"
_Lt2sMgmtPortId_Object = MibTableColumn
lt2sMgmtPortId = _Lt2sMgmtPortId_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 1),
    _Lt2sMgmtPortId_Type()
)
lt2sMgmtPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtPortId.setStatus("current")
_Lt2sMgmtPortName_Type = DisplayString
_Lt2sMgmtPortName_Object = MibTableColumn
lt2sMgmtPortName = _Lt2sMgmtPortName_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 2),
    _Lt2sMgmtPortName_Type()
)
lt2sMgmtPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtPortName.setStatus("current")


class _Lt2sMgmtPortEnable_Type(Integer32):
    """Custom type lt2sMgmtPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Lt2sMgmtPortEnable_Type.__name__ = "Integer32"
_Lt2sMgmtPortEnable_Object = MibTableColumn
lt2sMgmtPortEnable = _Lt2sMgmtPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 3),
    _Lt2sMgmtPortEnable_Type()
)
lt2sMgmtPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sMgmtPortEnable.setStatus("current")


class _Lt2sMgmtPortLink_Type(Integer32):
    """Custom type lt2sMgmtPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("notAvailable", 3))
    )


_Lt2sMgmtPortLink_Type.__name__ = "Integer32"
_Lt2sMgmtPortLink_Object = MibTableColumn
lt2sMgmtPortLink = _Lt2sMgmtPortLink_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 4),
    _Lt2sMgmtPortLink_Type()
)
lt2sMgmtPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtPortLink.setStatus("current")


class _Lt2sMgmtPortSpeed_Type(Integer32):
    """Custom type lt2sMgmtPortSpeed based on Integer32"""
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
        *(("full1000", 1),
          ("full100", 2),
          ("half100", 3),
          ("full10", 4),
          ("half10", 5),
          ("notAvailable", 6))
    )


_Lt2sMgmtPortSpeed_Type.__name__ = "Integer32"
_Lt2sMgmtPortSpeed_Object = MibTableColumn
lt2sMgmtPortSpeed = _Lt2sMgmtPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 5),
    _Lt2sMgmtPortSpeed_Type()
)
lt2sMgmtPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtPortSpeed.setStatus("current")


class _Lt2sMgmtPortTxBytes_Type(Integer32):
    """Custom type lt2sMgmtPortTxBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sMgmtPortTxBytes_Type.__name__ = "Integer32"
_Lt2sMgmtPortTxBytes_Object = MibTableColumn
lt2sMgmtPortTxBytes = _Lt2sMgmtPortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 6),
    _Lt2sMgmtPortTxBytes_Type()
)
lt2sMgmtPortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtPortTxBytes.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtPortTxBytes.setUnits("sent Bytes")


class _Lt2sMgmtPortRxBytes_Type(Integer32):
    """Custom type lt2sMgmtPortRxBytes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sMgmtPortRxBytes_Type.__name__ = "Integer32"
_Lt2sMgmtPortRxBytes_Object = MibTableColumn
lt2sMgmtPortRxBytes = _Lt2sMgmtPortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 7),
    _Lt2sMgmtPortRxBytes_Type()
)
lt2sMgmtPortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtPortRxBytes.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtPortRxBytes.setUnits("sent Bytes")


class _Lt2sMgmtSfpPlugged_Type(Integer32):
    """Custom type lt2sMgmtSfpPlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("removed", 1),
          ("inserted", 2),
          ("notAvailable", 3))
    )


_Lt2sMgmtSfpPlugged_Type.__name__ = "Integer32"
_Lt2sMgmtSfpPlugged_Object = MibTableColumn
lt2sMgmtSfpPlugged = _Lt2sMgmtSfpPlugged_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 8),
    _Lt2sMgmtSfpPlugged_Type()
)
lt2sMgmtSfpPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpPlugged.setStatus("current")


class _Lt2sMgmtSfpVendor_Type(DisplayString):
    """Custom type lt2sMgmtSfpVendor based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Lt2sMgmtSfpVendor_Type.__name__ = "DisplayString"
_Lt2sMgmtSfpVendor_Object = MibTableColumn
lt2sMgmtSfpVendor = _Lt2sMgmtSfpVendor_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 9),
    _Lt2sMgmtSfpVendor_Type()
)
lt2sMgmtSfpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpVendor.setStatus("current")


class _Lt2sMgmtSfpType_Type(DisplayString):
    """Custom type lt2sMgmtSfpType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Lt2sMgmtSfpType_Type.__name__ = "DisplayString"
_Lt2sMgmtSfpType_Object = MibTableColumn
lt2sMgmtSfpType = _Lt2sMgmtSfpType_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 10),
    _Lt2sMgmtSfpType_Type()
)
lt2sMgmtSfpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpType.setStatus("current")


class _Lt2sMgmtSfpSerial_Type(DisplayString):
    """Custom type lt2sMgmtSfpSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Lt2sMgmtSfpSerial_Type.__name__ = "DisplayString"
_Lt2sMgmtSfpSerial_Object = MibTableColumn
lt2sMgmtSfpSerial = _Lt2sMgmtSfpSerial_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 11),
    _Lt2sMgmtSfpSerial_Type()
)
lt2sMgmtSfpSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpSerial.setStatus("current")


class _Lt2sMgmtSfpWavelength_Type(DisplayString):
    """Custom type lt2sMgmtSfpWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Lt2sMgmtSfpWavelength_Type.__name__ = "DisplayString"
_Lt2sMgmtSfpWavelength_Object = MibTableColumn
lt2sMgmtSfpWavelength = _Lt2sMgmtSfpWavelength_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 12),
    _Lt2sMgmtSfpWavelength_Type()
)
lt2sMgmtSfpWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpWavelength.setStatus("current")


class _Lt2sMgmtSfpTxPower_Type(Integer32):
    """Custom type lt2sMgmtSfpTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sMgmtSfpTxPower_Type.__name__ = "Integer32"
_Lt2sMgmtSfpTxPower_Object = MibTableColumn
lt2sMgmtSfpTxPower = _Lt2sMgmtSfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 13),
    _Lt2sMgmtSfpTxPower_Type()
)
lt2sMgmtSfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtSfpTxPower.setUnits("0.001 dBm")


class _Lt2sMgmtSfpRxPower_Type(Integer32):
    """Custom type lt2sMgmtSfpRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sMgmtSfpRxPower_Type.__name__ = "Integer32"
_Lt2sMgmtSfpRxPower_Object = MibTableColumn
lt2sMgmtSfpRxPower = _Lt2sMgmtSfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 14),
    _Lt2sMgmtSfpRxPower_Type()
)
lt2sMgmtSfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpRxPower.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtSfpRxPower.setUnits("0.001 dBm")


class _Lt2sMgmtSfpLaserTemp_Type(Integer32):
    """Custom type lt2sMgmtSfpLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sMgmtSfpLaserTemp_Type.__name__ = "Integer32"
_Lt2sMgmtSfpLaserTemp_Object = MibTableColumn
lt2sMgmtSfpLaserTemp = _Lt2sMgmtSfpLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 15),
    _Lt2sMgmtSfpLaserTemp_Type()
)
lt2sMgmtSfpLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpLaserTemp.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtSfpLaserTemp.setUnits("0.01 degrees Celsius")


class _Lt2sMgmtSfpLaserBias_Type(Integer32):
    """Custom type lt2sMgmtSfpLaserBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sMgmtSfpLaserBias_Type.__name__ = "Integer32"
_Lt2sMgmtSfpLaserBias_Object = MibTableColumn
lt2sMgmtSfpLaserBias = _Lt2sMgmtSfpLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 16),
    _Lt2sMgmtSfpLaserBias_Type()
)
lt2sMgmtSfpLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sMgmtSfpLaserBias.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtSfpLaserBias.setUnits("0.001 Ampere")


class _Lt2sMgmtSfpTxLow_Type(Integer32):
    """Custom type lt2sMgmtSfpTxLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 2),
    )


_Lt2sMgmtSfpTxLow_Type.__name__ = "Integer32"
_Lt2sMgmtSfpTxLow_Object = MibTableColumn
lt2sMgmtSfpTxLow = _Lt2sMgmtSfpTxLow_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 17),
    _Lt2sMgmtSfpTxLow_Type()
)
lt2sMgmtSfpTxLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sMgmtSfpTxLow.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtSfpTxLow.setUnits("dBm")


class _Lt2sMgmtSfpTxHigh_Type(Integer32):
    """Custom type lt2sMgmtSfpTxHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 8),
    )


_Lt2sMgmtSfpTxHigh_Type.__name__ = "Integer32"
_Lt2sMgmtSfpTxHigh_Object = MibTableColumn
lt2sMgmtSfpTxHigh = _Lt2sMgmtSfpTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 18),
    _Lt2sMgmtSfpTxHigh_Type()
)
lt2sMgmtSfpTxHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sMgmtSfpTxHigh.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtSfpTxHigh.setUnits("dBm")


class _Lt2sMgmtSfpRxLow_Type(Integer32):
    """Custom type lt2sMgmtSfpRxLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_Lt2sMgmtSfpRxLow_Type.__name__ = "Integer32"
_Lt2sMgmtSfpRxLow_Object = MibTableColumn
lt2sMgmtSfpRxLow = _Lt2sMgmtSfpRxLow_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 19),
    _Lt2sMgmtSfpRxLow_Type()
)
lt2sMgmtSfpRxLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sMgmtSfpRxLow.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtSfpRxLow.setUnits("dBm")


class _Lt2sMgmtSfpRxHigh_Type(Integer32):
    """Custom type lt2sMgmtSfpRxHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 6),
    )


_Lt2sMgmtSfpRxHigh_Type.__name__ = "Integer32"
_Lt2sMgmtSfpRxHigh_Object = MibTableColumn
lt2sMgmtSfpRxHigh = _Lt2sMgmtSfpRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 1, 26, 1, 20),
    _Lt2sMgmtSfpRxHigh_Type()
)
lt2sMgmtSfpRxHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sMgmtSfpRxHigh.setStatus("current")
if mibBuilder.loadTexts:
    lt2sMgmtSfpRxHigh.setUnits("dBm")
_Lt2sSystem_ObjectIdentity = ObjectIdentity
lt2sSystem = _Lt2sSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2)
)


class _Lt2sTemperature_Type(Integer32):
    """Custom type lt2sTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )


_Lt2sTemperature_Type.__name__ = "Integer32"
_Lt2sTemperature_Object = MibScalar
lt2sTemperature = _Lt2sTemperature_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2, 1),
    _Lt2sTemperature_Type()
)
lt2sTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sTemperature.setStatus("current")


class _Lt2sPowerType_Type(Integer32):
    """Custom type lt2sPowerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("notAvailable", 3))
    )


_Lt2sPowerType_Type.__name__ = "Integer32"
_Lt2sPowerType_Object = MibScalar
lt2sPowerType = _Lt2sPowerType_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2, 2),
    _Lt2sPowerType_Type()
)
lt2sPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sPowerType.setStatus("current")


class _Lt2sPowerStatus_Type(Integer32):
    """Custom type lt2sPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("failed", 2),
          ("notPlugged", 3))
    )


_Lt2sPowerStatus_Type.__name__ = "Integer32"
_Lt2sPowerStatus_Object = MibScalar
lt2sPowerStatus = _Lt2sPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2, 3),
    _Lt2sPowerStatus_Type()
)
lt2sPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sPowerStatus.setStatus("current")


class _Lt2sPowerFanStatus_Type(Integer32):
    """Custom type lt2sPowerFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("on", 2),
          ("off", 3))
    )


_Lt2sPowerFanStatus_Type.__name__ = "Integer32"
_Lt2sPowerFanStatus_Object = MibScalar
lt2sPowerFanStatus = _Lt2sPowerFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2, 4),
    _Lt2sPowerFanStatus_Type()
)
lt2sPowerFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sPowerFanStatus.setStatus("current")


class _Lt2sPowerFanRPM_Type(Integer32):
    """Custom type lt2sPowerFanRPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_Lt2sPowerFanRPM_Type.__name__ = "Integer32"
_Lt2sPowerFanRPM_Object = MibScalar
lt2sPowerFanRPM = _Lt2sPowerFanRPM_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2, 5),
    _Lt2sPowerFanRPM_Type()
)
lt2sPowerFanRPM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sPowerFanRPM.setStatus("current")
if mibBuilder.loadTexts:
    lt2sPowerFanRPM.setUnits("revolutions per minute")


class _Lt2sPowerFanMode_Type(Integer32):
    """Custom type lt2sPowerFanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysOff", 1),
          ("alwaysOn", 2),
          ("byTemperature", 3))
    )


_Lt2sPowerFanMode_Type.__name__ = "Integer32"
_Lt2sPowerFanMode_Object = MibScalar
lt2sPowerFanMode = _Lt2sPowerFanMode_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2, 6),
    _Lt2sPowerFanMode_Type()
)
lt2sPowerFanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPowerFanMode.setStatus("current")


class _Lt2sPowerFanOnTemp_Type(Integer32):
    """Custom type lt2sPowerFanOnTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_Lt2sPowerFanOnTemp_Type.__name__ = "Integer32"
_Lt2sPowerFanOnTemp_Object = MibScalar
lt2sPowerFanOnTemp = _Lt2sPowerFanOnTemp_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2, 7),
    _Lt2sPowerFanOnTemp_Type()
)
lt2sPowerFanOnTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPowerFanOnTemp.setStatus("current")
if mibBuilder.loadTexts:
    lt2sPowerFanOnTemp.setUnits("degrees Celsius")


class _Lt2sPowerFanOffTemp_Type(Integer32):
    """Custom type lt2sPowerFanOffTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60),
    )


_Lt2sPowerFanOffTemp_Type.__name__ = "Integer32"
_Lt2sPowerFanOffTemp_Object = MibScalar
lt2sPowerFanOffTemp = _Lt2sPowerFanOffTemp_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 2, 8),
    _Lt2sPowerFanOffTemp_Type()
)
lt2sPowerFanOffTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPowerFanOffTemp.setStatus("current")
if mibBuilder.loadTexts:
    lt2sPowerFanOffTemp.setUnits("degrees Celsius")
_Lt2sPorts_ObjectIdentity = ObjectIdentity
lt2sPorts = _Lt2sPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3)
)
_Lt2sPortTable_Object = MibTable
lt2sPortTable = _Lt2sPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1)
)
if mibBuilder.loadTexts:
    lt2sPortTable.setStatus("current")
_Lt2sPortEntry_Object = MibTableRow
lt2sPortEntry = _Lt2sPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1)
)
lt2sPortEntry.setIndexNames(
    (0, "Lambdatrail2s-MIB", "lt2sPortId"),
)
if mibBuilder.loadTexts:
    lt2sPortEntry.setStatus("current")


class _Lt2sPortId_Type(Integer32):
    """Custom type lt2sPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Lt2sPortId_Type.__name__ = "Integer32"
_Lt2sPortId_Object = MibTableColumn
lt2sPortId = _Lt2sPortId_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 1),
    _Lt2sPortId_Type()
)
lt2sPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sPortId.setStatus("current")


class _Lt2sPortEnable_Type(Integer32):
    """Custom type lt2sPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_Lt2sPortEnable_Type.__name__ = "Integer32"
_Lt2sPortEnable_Object = MibTableColumn
lt2sPortEnable = _Lt2sPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 2),
    _Lt2sPortEnable_Type()
)
lt2sPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPortEnable.setStatus("current")


class _Lt2sPortApsd_Type(Integer32):
    """Custom type lt2sPortApsd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Lt2sPortApsd_Type.__name__ = "Integer32"
_Lt2sPortApsd_Object = MibTableColumn
lt2sPortApsd = _Lt2sPortApsd_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 3),
    _Lt2sPortApsd_Type()
)
lt2sPortApsd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPortApsd.setStatus("current")


class _Lt2sPortSpeed_Type(Integer32):
    """Custom type lt2sPortSpeed based on Integer32"""
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
        *(("transparent", 1),
          ("speed10g", 2),
          ("speed8g", 3),
          ("speed16g", 4))
    )


_Lt2sPortSpeed_Type.__name__ = "Integer32"
_Lt2sPortSpeed_Object = MibTableColumn
lt2sPortSpeed = _Lt2sPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 4),
    _Lt2sPortSpeed_Type()
)
lt2sPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPortSpeed.setStatus("current")


class _Lt2sPortReset_Type(Integer32):
    """Custom type lt2sPortReset based on Integer32"""
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


_Lt2sPortReset_Type.__name__ = "Integer32"
_Lt2sPortReset_Object = MibTableColumn
lt2sPortReset = _Lt2sPortReset_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 5),
    _Lt2sPortReset_Type()
)
lt2sPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPortReset.setStatus("current")


class _Lt2sPortLoop_Type(Integer32):
    """Custom type lt2sPortLoop based on Integer32"""
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
          ("line", 2),
          ("client", 3))
    )


_Lt2sPortLoop_Type.__name__ = "Integer32"
_Lt2sPortLoop_Object = MibTableColumn
lt2sPortLoop = _Lt2sPortLoop_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 6),
    _Lt2sPortLoop_Type()
)
lt2sPortLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPortLoop.setStatus("current")


class _Lt2sPortName_Type(DisplayString):
    """Custom type lt2sPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Lt2sPortName_Type.__name__ = "DisplayString"
_Lt2sPortName_Object = MibTableColumn
lt2sPortName = _Lt2sPortName_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 7),
    _Lt2sPortName_Type()
)
lt2sPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sPortName.setStatus("current")


class _Lt2sLinePlugged_Type(Integer32):
    """Custom type lt2sLinePlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPlugged", 1),
          ("plugged", 2),
          ("notAvailable", 3))
    )


_Lt2sLinePlugged_Type.__name__ = "Integer32"
_Lt2sLinePlugged_Object = MibTableColumn
lt2sLinePlugged = _Lt2sLinePlugged_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 8),
    _Lt2sLinePlugged_Type()
)
lt2sLinePlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLinePlugged.setStatus("current")


class _Lt2sLineLink_Type(Integer32):
    """Custom type lt2sLineLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("notAvailable", 3))
    )


_Lt2sLineLink_Type.__name__ = "Integer32"
_Lt2sLineLink_Object = MibTableColumn
lt2sLineLink = _Lt2sLineLink_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 9),
    _Lt2sLineLink_Type()
)
lt2sLineLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLineLink.setStatus("current")


class _Lt2sLineApsd_Type(Integer32):
    """Custom type lt2sLineApsd based on Integer32"""
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
        *(("no", 1),
          ("yes", 2),
          ("disabled", 3),
          ("notAvailable", 4))
    )


_Lt2sLineApsd_Type.__name__ = "Integer32"
_Lt2sLineApsd_Object = MibTableColumn
lt2sLineApsd = _Lt2sLineApsd_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 10),
    _Lt2sLineApsd_Type()
)
lt2sLineApsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLineApsd.setStatus("current")


class _Lt2sLineType_Type(DisplayString):
    """Custom type lt2sLineType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Lt2sLineType_Type.__name__ = "DisplayString"
_Lt2sLineType_Object = MibTableColumn
lt2sLineType = _Lt2sLineType_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 11),
    _Lt2sLineType_Type()
)
lt2sLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLineType.setStatus("current")


class _Lt2sLineWavelength_Type(DisplayString):
    """Custom type lt2sLineWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Lt2sLineWavelength_Type.__name__ = "DisplayString"
_Lt2sLineWavelength_Object = MibTableColumn
lt2sLineWavelength = _Lt2sLineWavelength_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 12),
    _Lt2sLineWavelength_Type()
)
lt2sLineWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLineWavelength.setStatus("current")


class _Lt2sLineTxPower_Type(Integer32):
    """Custom type lt2sLineTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sLineTxPower_Type.__name__ = "Integer32"
_Lt2sLineTxPower_Object = MibTableColumn
lt2sLineTxPower = _Lt2sLineTxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 13),
    _Lt2sLineTxPower_Type()
)
lt2sLineTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLineTxPower.setStatus("current")
if mibBuilder.loadTexts:
    lt2sLineTxPower.setUnits("0.001 dBm")


class _Lt2sLineRxPower_Type(Integer32):
    """Custom type lt2sLineRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sLineRxPower_Type.__name__ = "Integer32"
_Lt2sLineRxPower_Object = MibTableColumn
lt2sLineRxPower = _Lt2sLineRxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 14),
    _Lt2sLineRxPower_Type()
)
lt2sLineRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLineRxPower.setStatus("current")
if mibBuilder.loadTexts:
    lt2sLineRxPower.setUnits("0.001 dBm")


class _Lt2sLineLaserTemp_Type(Integer32):
    """Custom type lt2sLineLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sLineLaserTemp_Type.__name__ = "Integer32"
_Lt2sLineLaserTemp_Object = MibTableColumn
lt2sLineLaserTemp = _Lt2sLineLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 15),
    _Lt2sLineLaserTemp_Type()
)
lt2sLineLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLineLaserTemp.setStatus("current")
if mibBuilder.loadTexts:
    lt2sLineLaserTemp.setUnits("degrees Centigrade")


class _Lt2sLineLaserBias_Type(Integer32):
    """Custom type lt2sLineLaserBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sLineLaserBias_Type.__name__ = "Integer32"
_Lt2sLineLaserBias_Object = MibTableColumn
lt2sLineLaserBias = _Lt2sLineLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 16),
    _Lt2sLineLaserBias_Type()
)
lt2sLineLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sLineLaserBias.setStatus("current")
if mibBuilder.loadTexts:
    lt2sLineLaserBias.setUnits("0.001 Amp")


class _Lt2sLineTxLow_Type(Integer32):
    """Custom type lt2sLineTxLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 2),
    )


_Lt2sLineTxLow_Type.__name__ = "Integer32"
_Lt2sLineTxLow_Object = MibTableColumn
lt2sLineTxLow = _Lt2sLineTxLow_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 17),
    _Lt2sLineTxLow_Type()
)
lt2sLineTxLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sLineTxLow.setStatus("current")
if mibBuilder.loadTexts:
    lt2sLineTxLow.setUnits("dBm")


class _Lt2sLineTxHigh_Type(Integer32):
    """Custom type lt2sLineTxHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 8),
    )


_Lt2sLineTxHigh_Type.__name__ = "Integer32"
_Lt2sLineTxHigh_Object = MibTableColumn
lt2sLineTxHigh = _Lt2sLineTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 18),
    _Lt2sLineTxHigh_Type()
)
lt2sLineTxHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sLineTxHigh.setStatus("current")
if mibBuilder.loadTexts:
    lt2sLineTxHigh.setUnits("dBm")


class _Lt2sLineRxLow_Type(Integer32):
    """Custom type lt2sLineRxLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_Lt2sLineRxLow_Type.__name__ = "Integer32"
_Lt2sLineRxLow_Object = MibTableColumn
lt2sLineRxLow = _Lt2sLineRxLow_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 19),
    _Lt2sLineRxLow_Type()
)
lt2sLineRxLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sLineRxLow.setStatus("current")
if mibBuilder.loadTexts:
    lt2sLineRxLow.setUnits("dBm")


class _Lt2sLineRxHigh_Type(Integer32):
    """Custom type lt2sLineRxHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 6),
    )


_Lt2sLineRxHigh_Type.__name__ = "Integer32"
_Lt2sLineRxHigh_Object = MibTableColumn
lt2sLineRxHigh = _Lt2sLineRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 20),
    _Lt2sLineRxHigh_Type()
)
lt2sLineRxHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sLineRxHigh.setStatus("current")
if mibBuilder.loadTexts:
    lt2sLineRxHigh.setUnits("dBm")


class _Lt2sClientPlugged_Type(Integer32):
    """Custom type lt2sClientPlugged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPlugged", 1),
          ("plugged", 2),
          ("notAvailable", 3))
    )


_Lt2sClientPlugged_Type.__name__ = "Integer32"
_Lt2sClientPlugged_Object = MibTableColumn
lt2sClientPlugged = _Lt2sClientPlugged_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 21),
    _Lt2sClientPlugged_Type()
)
lt2sClientPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientPlugged.setStatus("current")


class _Lt2sClientLink_Type(Integer32):
    """Custom type lt2sClientLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2),
          ("notAvailable", 3))
    )


_Lt2sClientLink_Type.__name__ = "Integer32"
_Lt2sClientLink_Object = MibTableColumn
lt2sClientLink = _Lt2sClientLink_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 22),
    _Lt2sClientLink_Type()
)
lt2sClientLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientLink.setStatus("current")


class _Lt2sClientApsd_Type(Integer32):
    """Custom type lt2sClientApsd based on Integer32"""
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
        *(("no", 1),
          ("yes", 2),
          ("disabled", 3),
          ("notAvailable", 4))
    )


_Lt2sClientApsd_Type.__name__ = "Integer32"
_Lt2sClientApsd_Object = MibTableColumn
lt2sClientApsd = _Lt2sClientApsd_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 23),
    _Lt2sClientApsd_Type()
)
lt2sClientApsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientApsd.setStatus("current")


class _Lt2sClientType_Type(DisplayString):
    """Custom type lt2sClientType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Lt2sClientType_Type.__name__ = "DisplayString"
_Lt2sClientType_Object = MibTableColumn
lt2sClientType = _Lt2sClientType_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 24),
    _Lt2sClientType_Type()
)
lt2sClientType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientType.setStatus("current")


class _Lt2sClientWavelength_Type(DisplayString):
    """Custom type lt2sClientWavelength based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Lt2sClientWavelength_Type.__name__ = "DisplayString"
_Lt2sClientWavelength_Object = MibTableColumn
lt2sClientWavelength = _Lt2sClientWavelength_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 25),
    _Lt2sClientWavelength_Type()
)
lt2sClientWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientWavelength.setStatus("current")


class _Lt2sClientTxPower_Type(Integer32):
    """Custom type lt2sClientTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sClientTxPower_Type.__name__ = "Integer32"
_Lt2sClientTxPower_Object = MibTableColumn
lt2sClientTxPower = _Lt2sClientTxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 26),
    _Lt2sClientTxPower_Type()
)
lt2sClientTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientTxPower.setStatus("current")
if mibBuilder.loadTexts:
    lt2sClientTxPower.setUnits("0.001 dBm")


class _Lt2sClientRxPower_Type(Integer32):
    """Custom type lt2sClientRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sClientRxPower_Type.__name__ = "Integer32"
_Lt2sClientRxPower_Object = MibTableColumn
lt2sClientRxPower = _Lt2sClientRxPower_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 27),
    _Lt2sClientRxPower_Type()
)
lt2sClientRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientRxPower.setStatus("current")
if mibBuilder.loadTexts:
    lt2sClientRxPower.setUnits("0.001 dBm")


class _Lt2sClientLaserTemp_Type(Integer32):
    """Custom type lt2sClientLaserTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sClientLaserTemp_Type.__name__ = "Integer32"
_Lt2sClientLaserTemp_Object = MibTableColumn
lt2sClientLaserTemp = _Lt2sClientLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 28),
    _Lt2sClientLaserTemp_Type()
)
lt2sClientLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientLaserTemp.setStatus("current")
if mibBuilder.loadTexts:
    lt2sClientLaserTemp.setUnits("degrees Centigrade")


class _Lt2sClientLaserBias_Type(Integer32):
    """Custom type lt2sClientLaserBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_Lt2sClientLaserBias_Type.__name__ = "Integer32"
_Lt2sClientLaserBias_Object = MibTableColumn
lt2sClientLaserBias = _Lt2sClientLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 29),
    _Lt2sClientLaserBias_Type()
)
lt2sClientLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sClientLaserBias.setStatus("current")
if mibBuilder.loadTexts:
    lt2sClientLaserBias.setUnits("0.001 Amp")


class _Lt2sClientTxLow_Type(Integer32):
    """Custom type lt2sClientTxLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 2),
    )


_Lt2sClientTxLow_Type.__name__ = "Integer32"
_Lt2sClientTxLow_Object = MibTableColumn
lt2sClientTxLow = _Lt2sClientTxLow_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 30),
    _Lt2sClientTxLow_Type()
)
lt2sClientTxLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sClientTxLow.setStatus("current")
if mibBuilder.loadTexts:
    lt2sClientTxLow.setUnits("dBm")


class _Lt2sClientTxHigh_Type(Integer32):
    """Custom type lt2sClientTxHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-4, 8),
    )


_Lt2sClientTxHigh_Type.__name__ = "Integer32"
_Lt2sClientTxHigh_Object = MibTableColumn
lt2sClientTxHigh = _Lt2sClientTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 31),
    _Lt2sClientTxHigh_Type()
)
lt2sClientTxHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sClientTxHigh.setStatus("current")
if mibBuilder.loadTexts:
    lt2sClientTxHigh.setUnits("dBm")


class _Lt2sClientRxLow_Type(Integer32):
    """Custom type lt2sClientRxLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 0),
    )


_Lt2sClientRxLow_Type.__name__ = "Integer32"
_Lt2sClientRxLow_Object = MibTableColumn
lt2sClientRxLow = _Lt2sClientRxLow_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 32),
    _Lt2sClientRxLow_Type()
)
lt2sClientRxLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sClientRxLow.setStatus("current")
if mibBuilder.loadTexts:
    lt2sClientRxLow.setUnits("dBm")


class _Lt2sClientRxHigh_Type(Integer32):
    """Custom type lt2sClientRxHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 6),
    )


_Lt2sClientRxHigh_Type.__name__ = "Integer32"
_Lt2sClientRxHigh_Object = MibTableColumn
lt2sClientRxHigh = _Lt2sClientRxHigh_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 3, 1, 1, 33),
    _Lt2sClientRxHigh_Type()
)
lt2sClientRxHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lt2sClientRxHigh.setStatus("current")
if mibBuilder.loadTexts:
    lt2sClientRxHigh.setUnits("dBm")
_Lt2sInfo_ObjectIdentity = ObjectIdentity
lt2sInfo = _Lt2sInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 5, 4)
)
_Lt2sTrapDetails_Type = DisplayString
_Lt2sTrapDetails_Object = MibScalar
lt2sTrapDetails = _Lt2sTrapDetails_Object(
    (1, 3, 6, 1, 4, 1, 35616, 5, 4, 1),
    _Lt2sTrapDetails_Type()
)
lt2sTrapDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lt2sTrapDetails.setStatus("current")
_Lt2sCompliances_ObjectIdentity = ObjectIdentity
lt2sCompliances = _Lt2sCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 5, 8)
)
_Lt2sGroups_ObjectIdentity = ObjectIdentity
lt2sGroups = _Lt2sGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35616, 5, 9)
)

# Managed Objects groups

lt2sAgentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35616, 5, 9, 1)
)
lt2sAgentGroup.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sDescription"),
        ("Lambdatrail2s-MIB", "lt2sDeviceType"),
        ("Lambdatrail2s-MIB", "lt2sHwRevision"),
        ("Lambdatrail2s-MIB", "lt2sManufacturingDate"),
        ("Lambdatrail2s-MIB", "lt2sSerialNumber"),
        ("Lambdatrail2s-MIB", "lt2sSystemName"),
        ("Lambdatrail2s-MIB", "lt2sSystemLocation"),
        ("Lambdatrail2s-MIB", "lt2sSystemContact"),
        ("Lambdatrail2s-MIB", "lt2sSystemUptime"),
        ("Lambdatrail2s-MIB", "lt2sFirmwareVersion"),
        ("Lambdatrail2s-MIB", "lt2suCVersion"),
        ("Lambdatrail2s-MIB", "lt2sSaveRunningCfg"),
        ("Lambdatrail2s-MIB", "lt2sResetAgent"),
        ("Lambdatrail2s-MIB", "lt2sSnmpGetCommunity"),
        ("Lambdatrail2s-MIB", "lt2sSnmpSetCommunity"),
        ("Lambdatrail2s-MIB", "lt2sIp4DHCP"),
        ("Lambdatrail2s-MIB", "lt2sIp4Address"),
        ("Lambdatrail2s-MIB", "lt2sIp4Mask"),
        ("Lambdatrail2s-MIB", "lt2sIp4Gateway"),
        ("Lambdatrail2s-MIB", "lt2sIp4PrimaryDns"),
        ("Lambdatrail2s-MIB", "lt2sIp4SecondaryDns"),
        ("Lambdatrail2s-MIB", "lt2sSnmpServer"),
        ("Lambdatrail2s-MIB", "lt2sHttpServer"),
        ("Lambdatrail2s-MIB", "lt2sTelnetServer"),
        ("Lambdatrail2s-MIB", "lt2sFtpServer"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortEnable"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortLink"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortSpeed"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortTxBytes"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortRxBytes"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpPlugged"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpVendor"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpType"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpSerial"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpWavelength"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpTxPower"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpRxPower"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpLaserTemp"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpLaserBias"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpTxLow"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpTxHigh"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpRxLow"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpRxHigh"))
)
if mibBuilder.loadTexts:
    lt2sAgentGroup.setStatus("current")

lt2sSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35616, 5, 9, 2)
)
lt2sSystemGroup.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sTemperature"),
        ("Lambdatrail2s-MIB", "lt2sPowerType"),
        ("Lambdatrail2s-MIB", "lt2sPowerStatus"),
        ("Lambdatrail2s-MIB", "lt2sPowerFanStatus"),
        ("Lambdatrail2s-MIB", "lt2sPowerFanRPM"),
        ("Lambdatrail2s-MIB", "lt2sPowerFanMode"),
        ("Lambdatrail2s-MIB", "lt2sPowerFanOnTemp"),
        ("Lambdatrail2s-MIB", "lt2sPowerFanOffTemp"))
)
if mibBuilder.loadTexts:
    lt2sSystemGroup.setStatus("current")

lt2sPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35616, 5, 9, 3)
)
lt2sPortsGroup.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sPortEnable"),
        ("Lambdatrail2s-MIB", "lt2sPortApsd"),
        ("Lambdatrail2s-MIB", "lt2sPortSpeed"),
        ("Lambdatrail2s-MIB", "lt2sPortReset"),
        ("Lambdatrail2s-MIB", "lt2sPortLoop"),
        ("Lambdatrail2s-MIB", "lt2sPortName"),
        ("Lambdatrail2s-MIB", "lt2sLinePlugged"),
        ("Lambdatrail2s-MIB", "lt2sLineType"),
        ("Lambdatrail2s-MIB", "lt2sLineLink"),
        ("Lambdatrail2s-MIB", "lt2sLineApsd"),
        ("Lambdatrail2s-MIB", "lt2sLineWavelength"),
        ("Lambdatrail2s-MIB", "lt2sLineTxPower"),
        ("Lambdatrail2s-MIB", "lt2sLineRxPower"),
        ("Lambdatrail2s-MIB", "lt2sLineLaserTemp"),
        ("Lambdatrail2s-MIB", "lt2sLineLaserBias"),
        ("Lambdatrail2s-MIB", "lt2sClientPlugged"),
        ("Lambdatrail2s-MIB", "lt2sClientType"),
        ("Lambdatrail2s-MIB", "lt2sClientLink"),
        ("Lambdatrail2s-MIB", "lt2sClientApsd"),
        ("Lambdatrail2s-MIB", "lt2sClientWavelength"),
        ("Lambdatrail2s-MIB", "lt2sClientTxPower"),
        ("Lambdatrail2s-MIB", "lt2sClientRxPower"),
        ("Lambdatrail2s-MIB", "lt2sClientLaserTemp"),
        ("Lambdatrail2s-MIB", "lt2sClientLaserBias"),
        ("Lambdatrail2s-MIB", "lt2sLineTxLow"),
        ("Lambdatrail2s-MIB", "lt2sLineTxHigh"),
        ("Lambdatrail2s-MIB", "lt2sLineRxLow"),
        ("Lambdatrail2s-MIB", "lt2sLineRxHigh"),
        ("Lambdatrail2s-MIB", "lt2sClientTxLow"),
        ("Lambdatrail2s-MIB", "lt2sClientTxHigh"),
        ("Lambdatrail2s-MIB", "lt2sClientRxLow"),
        ("Lambdatrail2s-MIB", "lt2sClientRxHigh"))
)
if mibBuilder.loadTexts:
    lt2sPortsGroup.setStatus("current")

lt2sInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35616, 5, 9, 4)
)
lt2sInfoGroup.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sInfoGroup.setStatus("current")


# Notification objects

lt2sMgmtStartup = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 1)
)
lt2sMgmtStartup.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sMgmtStartup.setStatus(
        "current"
    )

lt2sMgmtAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 2)
)
lt2sMgmtAuthenticationFailure.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sMgmtAuthenticationFailure.setStatus(
        "current"
    )

lt2sTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 3)
)
lt2sTemperatureHigh.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sTemperatureHigh.setStatus(
        "current"
    )

lt2sTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 4)
)
lt2sTemperatureNormal.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sTemperatureNormal.setStatus(
        "current"
    )

lt2sPowerSupplyPluggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 5)
)
lt2sPowerSupplyPluggedIn.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sPowerSupplyPluggedIn.setStatus(
        "current"
    )

lt2sPowerSupplyPluggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 6)
)
lt2sPowerSupplyPluggedOut.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sPowerSupplyPluggedOut.setStatus(
        "current"
    )

lt2sPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 7)
)
lt2sPowerNormal.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sPowerNormal.setStatus(
        "current"
    )

lt2sPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 8)
)
lt2sPowerFailure.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sPowerFailure.setStatus(
        "current"
    )

lt2sFanOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 9)
)
lt2sFanOn.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sFanOn.setStatus(
        "current"
    )

lt2sFanOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 10)
)
lt2sFanOff.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sFanOff.setStatus(
        "current"
    )

lt2sFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 11)
)
lt2sFanFailure.setObjects(
    ("Lambdatrail2s-MIB", "lt2sTrapDetails")
)
if mibBuilder.loadTexts:
    lt2sFanFailure.setStatus(
        "current"
    )

lt2sMgmtSfpPluggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 12)
)
lt2sMgmtSfpPluggedIn.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtSfpPluggedIn.setStatus(
        "current"
    )

lt2sMgmtSfpPluggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 13)
)
lt2sMgmtSfpPluggedOut.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtSfpPluggedOut.setStatus(
        "current"
    )

lt2sMgmtLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 14)
)
lt2sMgmtLinkUp.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtLinkUp.setStatus(
        "current"
    )

lt2sMgmtLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 15)
)
lt2sMgmtLinkDown.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtLinkDown.setStatus(
        "current"
    )

lt2sMgmtTxLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 16)
)
lt2sMgmtTxLow.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtTxLow.setStatus(
        "current"
    )

lt2sMgmtTxHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 17)
)
lt2sMgmtTxHigh.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtTxHigh.setStatus(
        "current"
    )

lt2sMgmtTxNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 18)
)
lt2sMgmtTxNormal.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtTxNormal.setStatus(
        "current"
    )

lt2sMgmtRxLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 19)
)
lt2sMgmtRxLow.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtRxLow.setStatus(
        "current"
    )

lt2sMgmtRxHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 20)
)
lt2sMgmtRxHigh.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtRxHigh.setStatus(
        "current"
    )

lt2sMgmtRxNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 21)
)
lt2sMgmtRxNormal.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sMgmtPortName"))
)
if mibBuilder.loadTexts:
    lt2sMgmtRxNormal.setStatus(
        "current"
    )

lt2sPortEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 22)
)
lt2sPortEnabled.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortEnabled.setStatus(
        "current"
    )

lt2sPortDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 23)
)
lt2sPortDisabled.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortDisabled.setStatus(
        "current"
    )

lt2sPortReseted = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 24)
)
lt2sPortReseted.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortReseted.setStatus(
        "current"
    )

lt2sPortThermalShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 25)
)
lt2sPortThermalShutdown.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortThermalShutdown.setStatus(
        "current"
    )

lt2sPortThermalWakeup = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 26)
)
lt2sPortThermalWakeup.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortThermalWakeup.setStatus(
        "current"
    )

lt2sLinePluggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 27)
)
lt2sLinePluggedIn.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sLinePluggedIn.setStatus(
        "current"
    )

lt2sClientPluggedIn = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 28)
)
lt2sClientPluggedIn.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sClientPluggedIn.setStatus(
        "current"
    )

lt2sLinePluggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 29)
)
lt2sLinePluggedOut.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sLinePluggedOut.setStatus(
        "current"
    )

lt2sClientPluggedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 30)
)
lt2sClientPluggedOut.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sClientPluggedOut.setStatus(
        "current"
    )

lt2sLineLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 31)
)
lt2sLineLinkUp.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sLineLinkUp.setStatus(
        "current"
    )

lt2sClientLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 32)
)
lt2sClientLinkUp.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sClientLinkUp.setStatus(
        "current"
    )

lt2sLineLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 33)
)
lt2sLineLinkDown.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sLineLinkDown.setStatus(
        "current"
    )

lt2sClientLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 34)
)
lt2sClientLinkDown.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sClientLinkDown.setStatus(
        "current"
    )

lt2sLineLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 35)
)
lt2sLineLoopOn.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sLineLoopOn.setStatus(
        "current"
    )

lt2sLineLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 36)
)
lt2sLineLoopOff.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sLineLoopOff.setStatus(
        "current"
    )

lt2sClientLoopOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 37)
)
lt2sClientLoopOn.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sClientLoopOn.setStatus(
        "current"
    )

lt2sClientLoopOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 38)
)
lt2sClientLoopOff.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sClientLoopOff.setStatus(
        "current"
    )

lt2sPortTxLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 39)
)
lt2sPortTxLow.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortTxLow.setStatus(
        "current"
    )

lt2sPortTxHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 40)
)
lt2sPortTxHigh.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortTxHigh.setStatus(
        "current"
    )

lt2sPortTxNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 41)
)
lt2sPortTxNormal.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortTxNormal.setStatus(
        "current"
    )

lt2sPortRxLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 42)
)
lt2sPortRxLow.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortRxLow.setStatus(
        "current"
    )

lt2sPortRxHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 43)
)
lt2sPortRxHigh.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortRxHigh.setStatus(
        "current"
    )

lt2sPortRxNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 35616, 5, 0, 44)
)
lt2sPortRxNormal.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sPortId"),
        ("Lambdatrail2s-MIB", "lt2sTrapDetails"),
        ("Lambdatrail2s-MIB", "lt2sPortName"))
)
if mibBuilder.loadTexts:
    lt2sPortRxNormal.setStatus(
        "current"
    )


# Notifications groups

lt2sNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35616, 5, 9, 5)
)
lt2sNotificationGroup.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sMgmtStartup"),
        ("Lambdatrail2s-MIB", "lt2sMgmtAuthenticationFailure"),
        ("Lambdatrail2s-MIB", "lt2sTemperatureHigh"),
        ("Lambdatrail2s-MIB", "lt2sTemperatureNormal"),
        ("Lambdatrail2s-MIB", "lt2sPowerSupplyPluggedIn"),
        ("Lambdatrail2s-MIB", "lt2sPowerSupplyPluggedOut"),
        ("Lambdatrail2s-MIB", "lt2sPowerNormal"),
        ("Lambdatrail2s-MIB", "lt2sPowerFailure"),
        ("Lambdatrail2s-MIB", "lt2sFanOn"),
        ("Lambdatrail2s-MIB", "lt2sFanOff"),
        ("Lambdatrail2s-MIB", "lt2sFanFailure"),
        ("Lambdatrail2s-MIB", "lt2sPortEnabled"),
        ("Lambdatrail2s-MIB", "lt2sPortDisabled"),
        ("Lambdatrail2s-MIB", "lt2sPortReseted"),
        ("Lambdatrail2s-MIB", "lt2sPortThermalShutdown"),
        ("Lambdatrail2s-MIB", "lt2sPortThermalWakeup"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpPluggedIn"),
        ("Lambdatrail2s-MIB", "lt2sLinePluggedIn"),
        ("Lambdatrail2s-MIB", "lt2sClientPluggedIn"),
        ("Lambdatrail2s-MIB", "lt2sMgmtSfpPluggedOut"),
        ("Lambdatrail2s-MIB", "lt2sLinePluggedOut"),
        ("Lambdatrail2s-MIB", "lt2sClientPluggedOut"),
        ("Lambdatrail2s-MIB", "lt2sMgmtLinkUp"),
        ("Lambdatrail2s-MIB", "lt2sLineLinkUp"),
        ("Lambdatrail2s-MIB", "lt2sClientLinkUp"),
        ("Lambdatrail2s-MIB", "lt2sMgmtLinkDown"),
        ("Lambdatrail2s-MIB", "lt2sLineLinkDown"),
        ("Lambdatrail2s-MIB", "lt2sClientLinkDown"),
        ("Lambdatrail2s-MIB", "lt2sLineLoopOn"),
        ("Lambdatrail2s-MIB", "lt2sLineLoopOff"),
        ("Lambdatrail2s-MIB", "lt2sClientLoopOn"),
        ("Lambdatrail2s-MIB", "lt2sClientLoopOff"),
        ("Lambdatrail2s-MIB", "lt2sMgmtTxLow"),
        ("Lambdatrail2s-MIB", "lt2sPortTxLow"),
        ("Lambdatrail2s-MIB", "lt2sMgmtTxHigh"),
        ("Lambdatrail2s-MIB", "lt2sPortTxHigh"),
        ("Lambdatrail2s-MIB", "lt2sMgmtTxNormal"),
        ("Lambdatrail2s-MIB", "lt2sPortTxNormal"),
        ("Lambdatrail2s-MIB", "lt2sMgmtRxLow"),
        ("Lambdatrail2s-MIB", "lt2sPortRxLow"),
        ("Lambdatrail2s-MIB", "lt2sMgmtRxHigh"),
        ("Lambdatrail2s-MIB", "lt2sPortRxHigh"),
        ("Lambdatrail2s-MIB", "lt2sMgmtRxNormal"),
        ("Lambdatrail2s-MIB", "lt2sPortRxNormal"))
)
if mibBuilder.loadTexts:
    lt2sNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lt2sCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35616, 5, 8, 1)
)
lt2sCompliance.setObjects(
      *(("Lambdatrail2s-MIB", "lt2sAgentGroup"),
        ("Lambdatrail2s-MIB", "lt2sSystemGroup"),
        ("Lambdatrail2s-MIB", "lt2sPortsGroup"),
        ("Lambdatrail2s-MIB", "lt2sInfoGroup"),
        ("Lambdatrail2s-MIB", "lt2sNotificationGroup"))
)
if mibBuilder.loadTexts:
    lt2sCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Lambdatrail2s-MIB",
    **{"lambdatrail2s": lambdatrail2s,
       "lt2sNotifications": lt2sNotifications,
       "lt2sMgmtStartup": lt2sMgmtStartup,
       "lt2sMgmtAuthenticationFailure": lt2sMgmtAuthenticationFailure,
       "lt2sTemperatureHigh": lt2sTemperatureHigh,
       "lt2sTemperatureNormal": lt2sTemperatureNormal,
       "lt2sPowerSupplyPluggedIn": lt2sPowerSupplyPluggedIn,
       "lt2sPowerSupplyPluggedOut": lt2sPowerSupplyPluggedOut,
       "lt2sPowerNormal": lt2sPowerNormal,
       "lt2sPowerFailure": lt2sPowerFailure,
       "lt2sFanOn": lt2sFanOn,
       "lt2sFanOff": lt2sFanOff,
       "lt2sFanFailure": lt2sFanFailure,
       "lt2sMgmtSfpPluggedIn": lt2sMgmtSfpPluggedIn,
       "lt2sMgmtSfpPluggedOut": lt2sMgmtSfpPluggedOut,
       "lt2sMgmtLinkUp": lt2sMgmtLinkUp,
       "lt2sMgmtLinkDown": lt2sMgmtLinkDown,
       "lt2sMgmtTxLow": lt2sMgmtTxLow,
       "lt2sMgmtTxHigh": lt2sMgmtTxHigh,
       "lt2sMgmtTxNormal": lt2sMgmtTxNormal,
       "lt2sMgmtRxLow": lt2sMgmtRxLow,
       "lt2sMgmtRxHigh": lt2sMgmtRxHigh,
       "lt2sMgmtRxNormal": lt2sMgmtRxNormal,
       "lt2sPortEnabled": lt2sPortEnabled,
       "lt2sPortDisabled": lt2sPortDisabled,
       "lt2sPortReseted": lt2sPortReseted,
       "lt2sPortThermalShutdown": lt2sPortThermalShutdown,
       "lt2sPortThermalWakeup": lt2sPortThermalWakeup,
       "lt2sLinePluggedIn": lt2sLinePluggedIn,
       "lt2sClientPluggedIn": lt2sClientPluggedIn,
       "lt2sLinePluggedOut": lt2sLinePluggedOut,
       "lt2sClientPluggedOut": lt2sClientPluggedOut,
       "lt2sLineLinkUp": lt2sLineLinkUp,
       "lt2sClientLinkUp": lt2sClientLinkUp,
       "lt2sLineLinkDown": lt2sLineLinkDown,
       "lt2sClientLinkDown": lt2sClientLinkDown,
       "lt2sLineLoopOn": lt2sLineLoopOn,
       "lt2sLineLoopOff": lt2sLineLoopOff,
       "lt2sClientLoopOn": lt2sClientLoopOn,
       "lt2sClientLoopOff": lt2sClientLoopOff,
       "lt2sPortTxLow": lt2sPortTxLow,
       "lt2sPortTxHigh": lt2sPortTxHigh,
       "lt2sPortTxNormal": lt2sPortTxNormal,
       "lt2sPortRxLow": lt2sPortRxLow,
       "lt2sPortRxHigh": lt2sPortRxHigh,
       "lt2sPortRxNormal": lt2sPortRxNormal,
       "lt2sAgent": lt2sAgent,
       "lt2sDescription": lt2sDescription,
       "lt2sDeviceType": lt2sDeviceType,
       "lt2sHwRevision": lt2sHwRevision,
       "lt2sManufacturingDate": lt2sManufacturingDate,
       "lt2sSerialNumber": lt2sSerialNumber,
       "lt2sSystemName": lt2sSystemName,
       "lt2sSystemLocation": lt2sSystemLocation,
       "lt2sSystemContact": lt2sSystemContact,
       "lt2sSystemUptime": lt2sSystemUptime,
       "lt2sFirmwareVersion": lt2sFirmwareVersion,
       "lt2suCVersion": lt2suCVersion,
       "lt2sSaveRunningCfg": lt2sSaveRunningCfg,
       "lt2sResetAgent": lt2sResetAgent,
       "lt2sSnmpGetCommunity": lt2sSnmpGetCommunity,
       "lt2sSnmpSetCommunity": lt2sSnmpSetCommunity,
       "lt2sIp4DHCP": lt2sIp4DHCP,
       "lt2sIp4Address": lt2sIp4Address,
       "lt2sIp4Mask": lt2sIp4Mask,
       "lt2sIp4Gateway": lt2sIp4Gateway,
       "lt2sIp4PrimaryDns": lt2sIp4PrimaryDns,
       "lt2sIp4SecondaryDns": lt2sIp4SecondaryDns,
       "lt2sSnmpServer": lt2sSnmpServer,
       "lt2sHttpServer": lt2sHttpServer,
       "lt2sTelnetServer": lt2sTelnetServer,
       "lt2sFtpServer": lt2sFtpServer,
       "lt2sMgmtPortTable": lt2sMgmtPortTable,
       "lt2sMgmtPortEntry": lt2sMgmtPortEntry,
       "lt2sMgmtPortId": lt2sMgmtPortId,
       "lt2sMgmtPortName": lt2sMgmtPortName,
       "lt2sMgmtPortEnable": lt2sMgmtPortEnable,
       "lt2sMgmtPortLink": lt2sMgmtPortLink,
       "lt2sMgmtPortSpeed": lt2sMgmtPortSpeed,
       "lt2sMgmtPortTxBytes": lt2sMgmtPortTxBytes,
       "lt2sMgmtPortRxBytes": lt2sMgmtPortRxBytes,
       "lt2sMgmtSfpPlugged": lt2sMgmtSfpPlugged,
       "lt2sMgmtSfpVendor": lt2sMgmtSfpVendor,
       "lt2sMgmtSfpType": lt2sMgmtSfpType,
       "lt2sMgmtSfpSerial": lt2sMgmtSfpSerial,
       "lt2sMgmtSfpWavelength": lt2sMgmtSfpWavelength,
       "lt2sMgmtSfpTxPower": lt2sMgmtSfpTxPower,
       "lt2sMgmtSfpRxPower": lt2sMgmtSfpRxPower,
       "lt2sMgmtSfpLaserTemp": lt2sMgmtSfpLaserTemp,
       "lt2sMgmtSfpLaserBias": lt2sMgmtSfpLaserBias,
       "lt2sMgmtSfpTxLow": lt2sMgmtSfpTxLow,
       "lt2sMgmtSfpTxHigh": lt2sMgmtSfpTxHigh,
       "lt2sMgmtSfpRxLow": lt2sMgmtSfpRxLow,
       "lt2sMgmtSfpRxHigh": lt2sMgmtSfpRxHigh,
       "lt2sSystem": lt2sSystem,
       "lt2sTemperature": lt2sTemperature,
       "lt2sPowerType": lt2sPowerType,
       "lt2sPowerStatus": lt2sPowerStatus,
       "lt2sPowerFanStatus": lt2sPowerFanStatus,
       "lt2sPowerFanRPM": lt2sPowerFanRPM,
       "lt2sPowerFanMode": lt2sPowerFanMode,
       "lt2sPowerFanOnTemp": lt2sPowerFanOnTemp,
       "lt2sPowerFanOffTemp": lt2sPowerFanOffTemp,
       "lt2sPorts": lt2sPorts,
       "lt2sPortTable": lt2sPortTable,
       "lt2sPortEntry": lt2sPortEntry,
       "lt2sPortId": lt2sPortId,
       "lt2sPortEnable": lt2sPortEnable,
       "lt2sPortApsd": lt2sPortApsd,
       "lt2sPortSpeed": lt2sPortSpeed,
       "lt2sPortReset": lt2sPortReset,
       "lt2sPortLoop": lt2sPortLoop,
       "lt2sPortName": lt2sPortName,
       "lt2sLinePlugged": lt2sLinePlugged,
       "lt2sLineLink": lt2sLineLink,
       "lt2sLineApsd": lt2sLineApsd,
       "lt2sLineType": lt2sLineType,
       "lt2sLineWavelength": lt2sLineWavelength,
       "lt2sLineTxPower": lt2sLineTxPower,
       "lt2sLineRxPower": lt2sLineRxPower,
       "lt2sLineLaserTemp": lt2sLineLaserTemp,
       "lt2sLineLaserBias": lt2sLineLaserBias,
       "lt2sLineTxLow": lt2sLineTxLow,
       "lt2sLineTxHigh": lt2sLineTxHigh,
       "lt2sLineRxLow": lt2sLineRxLow,
       "lt2sLineRxHigh": lt2sLineRxHigh,
       "lt2sClientPlugged": lt2sClientPlugged,
       "lt2sClientLink": lt2sClientLink,
       "lt2sClientApsd": lt2sClientApsd,
       "lt2sClientType": lt2sClientType,
       "lt2sClientWavelength": lt2sClientWavelength,
       "lt2sClientTxPower": lt2sClientTxPower,
       "lt2sClientRxPower": lt2sClientRxPower,
       "lt2sClientLaserTemp": lt2sClientLaserTemp,
       "lt2sClientLaserBias": lt2sClientLaserBias,
       "lt2sClientTxLow": lt2sClientTxLow,
       "lt2sClientTxHigh": lt2sClientTxHigh,
       "lt2sClientRxLow": lt2sClientRxLow,
       "lt2sClientRxHigh": lt2sClientRxHigh,
       "lt2sInfo": lt2sInfo,
       "lt2sTrapDetails": lt2sTrapDetails,
       "lt2sCompliances": lt2sCompliances,
       "lt2sCompliance": lt2sCompliance,
       "lt2sGroups": lt2sGroups,
       "lt2sAgentGroup": lt2sAgentGroup,
       "lt2sSystemGroup": lt2sSystemGroup,
       "lt2sPortsGroup": lt2sPortsGroup,
       "lt2sInfoGroup": lt2sInfoGroup,
       "lt2sNotificationGroup": lt2sNotificationGroup}
)
