# SNMP MIB module (NTRON714FX6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\redlion\NTRON714FX6-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:16 2025
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

ntron714fx6 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7)
)
if mibBuilder.loadTexts:
    ntron714fx6.setRevisions(
        ("2014-07-22 20:00",
         "2014-07-14 19:00",
         "2011-05-26 15:00",
         "2011-05-10 19:00",
         "2011-02-07 15:00",
         "2009-11-17 19:15")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ntron_ObjectIdentity = ObjectIdentity
ntron = _Ntron_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381)
)
_Ntron7xx_ObjectIdentity = ObjectIdentity
ntron7xx = _Ntron7xx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700)
)
_NtronSysGroup_ObjectIdentity = ObjectIdentity
ntronSysGroup = _NtronSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1)
)


class _NtronSysReset_Type(Integer32):
    """Custom type ntronSysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switchNoReset", 1),
          ("switchReset", 2))
    )


_NtronSysReset_Type.__name__ = "Integer32"
_NtronSysReset_Object = MibScalar
ntronSysReset = _NtronSysReset_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 1),
    _NtronSysReset_Type()
)
ntronSysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronSysReset.setStatus("current")


class _NtronSwVersion_Type(DisplayString):
    """Custom type ntronSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtronSwVersion_Type.__name__ = "DisplayString"
_NtronSwVersion_Object = MibScalar
ntronSwVersion = _NtronSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 2),
    _NtronSwVersion_Type()
)
ntronSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronSwVersion.setStatus("current")


class _NtronBuildDateAndTime_Type(DisplayString):
    """Custom type ntronBuildDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtronBuildDateAndTime_Type.__name__ = "DisplayString"
_NtronBuildDateAndTime_Object = MibScalar
ntronBuildDateAndTime = _NtronBuildDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 3),
    _NtronBuildDateAndTime_Type()
)
ntronBuildDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronBuildDateAndTime.setStatus("current")
_NtronTotalRam_Type = Integer32
_NtronTotalRam_Object = MibScalar
ntronTotalRam = _NtronTotalRam_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 4),
    _NtronTotalRam_Type()
)
ntronTotalRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronTotalRam.setStatus("current")
_NtronTotalFlash_Type = Integer32
_NtronTotalFlash_Object = MibScalar
ntronTotalFlash = _NtronTotalFlash_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 5),
    _NtronTotalFlash_Type()
)
ntronTotalFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronTotalFlash.setStatus("current")
_NtronEthernetPortCount_Type = Integer32
_NtronEthernetPortCount_Object = MibScalar
ntronEthernetPortCount = _NtronEthernetPortCount_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 6),
    _NtronEthernetPortCount_Type()
)
ntronEthernetPortCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronEthernetPortCount.setStatus("current")
_NtronCurrentIpAddress_Type = IpAddress
_NtronCurrentIpAddress_Object = MibScalar
ntronCurrentIpAddress = _NtronCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 7),
    _NtronCurrentIpAddress_Type()
)
ntronCurrentIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronCurrentIpAddress.setStatus("current")
_NtronConfiguredIpAddress_Type = IpAddress
_NtronConfiguredIpAddress_Object = MibScalar
ntronConfiguredIpAddress = _NtronConfiguredIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 8),
    _NtronConfiguredIpAddress_Type()
)
ntronConfiguredIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronConfiguredIpAddress.setStatus("current")
_NtronConfiguredSubnetMask_Type = IpAddress
_NtronConfiguredSubnetMask_Object = MibScalar
ntronConfiguredSubnetMask = _NtronConfiguredSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 9),
    _NtronConfiguredSubnetMask_Type()
)
ntronConfiguredSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronConfiguredSubnetMask.setStatus("current")
_NtronConfiguredGateway_Type = IpAddress
_NtronConfiguredGateway_Object = MibScalar
ntronConfiguredGateway = _NtronConfiguredGateway_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 10),
    _NtronConfiguredGateway_Type()
)
ntronConfiguredGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronConfiguredGateway.setStatus("current")


class _NtronUpdateConfiguredIpAddr_Type(Integer32):
    """Custom type ntronUpdateConfiguredIpAddr based on Integer32"""
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


_NtronUpdateConfiguredIpAddr_Type.__name__ = "Integer32"
_NtronUpdateConfiguredIpAddr_Object = MibScalar
ntronUpdateConfiguredIpAddr = _NtronUpdateConfiguredIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 11),
    _NtronUpdateConfiguredIpAddr_Type()
)
ntronUpdateConfiguredIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronUpdateConfiguredIpAddr.setStatus("current")


class _NtronIPAddressStatus_Type(Integer32):
    """Custom type ntronIPAddressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fromCli", 1),
          ("fromDhcp", 2))
    )


_NtronIPAddressStatus_Type.__name__ = "Integer32"
_NtronIPAddressStatus_Object = MibScalar
ntronIPAddressStatus = _NtronIPAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 12),
    _NtronIPAddressStatus_Type()
)
ntronIPAddressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIPAddressStatus.setStatus("current")
_NtronTotalNoOfPorts_Type = Integer32
_NtronTotalNoOfPorts_Object = MibScalar
ntronTotalNoOfPorts = _NtronTotalNoOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 13),
    _NtronTotalNoOfPorts_Type()
)
ntronTotalNoOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronTotalNoOfPorts.setStatus("current")


class _NtronMacAddress_Type(DisplayString):
    """Custom type ntronMacAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NtronMacAddress_Type.__name__ = "DisplayString"
_NtronMacAddress_Object = MibScalar
ntronMacAddress = _NtronMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 14),
    _NtronMacAddress_Type()
)
ntronMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronMacAddress.setStatus("current")


class _NtronContactStatus_Type(Integer32):
    """Custom type ntronContactStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2),
          ("unsupported", 3))
    )


_NtronContactStatus_Type.__name__ = "Integer32"
_NtronContactStatus_Object = MibScalar
ntronContactStatus = _NtronContactStatus_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 15),
    _NtronContactStatus_Type()
)
ntronContactStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronContactStatus.setStatus("current")


class _NtronPowerFault_Type(Integer32):
    """Custom type ntronPowerFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faultNone", 1),
          ("faultPower1", 2),
          ("faultPower2", 3))
    )


_NtronPowerFault_Type.__name__ = "Integer32"
_NtronPowerFault_Object = MibScalar
ntronPowerFault = _NtronPowerFault_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 16),
    _NtronPowerFault_Type()
)
ntronPowerFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronPowerFault.setStatus("current")


class _NtronModelString_Type(DisplayString):
    """Custom type ntronModelString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_NtronModelString_Type.__name__ = "DisplayString"
_NtronModelString_Object = MibScalar
ntronModelString = _NtronModelString_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 17),
    _NtronModelString_Type()
)
ntronModelString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronModelString.setStatus("current")


class _NtronBlVersion_Type(DisplayString):
    """Custom type ntronBlVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_NtronBlVersion_Type.__name__ = "DisplayString"
_NtronBlVersion_Object = MibScalar
ntronBlVersion = _NtronBlVersion_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 1, 18),
    _NtronBlVersion_Type()
)
ntronBlVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronBlVersion.setStatus("current")
_NtronNViewGroup_ObjectIdentity = ObjectIdentity
ntronNViewGroup = _NtronNViewGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 2)
)


class _NtronNViewState_Type(Integer32):
    """Custom type ntronNViewState based on Integer32"""
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


_NtronNViewState_Type.__name__ = "Integer32"
_NtronNViewState_Object = MibScalar
ntronNViewState = _NtronNViewState_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 2, 1),
    _NtronNViewState_Type()
)
ntronNViewState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronNViewState.setStatus("current")


class _NtronNViewInterval_Type(Integer32):
    """Custom type ntronNViewInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_NtronNViewInterval_Type.__name__ = "Integer32"
_NtronNViewInterval_Object = MibScalar
ntronNViewInterval = _NtronNViewInterval_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 2, 2),
    _NtronNViewInterval_Type()
)
ntronNViewInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronNViewInterval.setStatus("current")
_NtronNViewTable_Object = MibTable
ntronNViewTable = _NtronNViewTable_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 2, 3)
)
if mibBuilder.loadTexts:
    ntronNViewTable.setStatus("current")
_NtronNViewEntry_Object = MibTableRow
ntronNViewEntry = _NtronNViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 2, 3, 1)
)
ntronNViewEntry.setIndexNames(
    (0, "NTRON714FX6-MIB", "ntronNViewPortNumber"),
)
if mibBuilder.loadTexts:
    ntronNViewEntry.setStatus("current")
_NtronNViewPortNumber_Type = Integer32
_NtronNViewPortNumber_Object = MibTableColumn
ntronNViewPortNumber = _NtronNViewPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 2, 3, 1, 1),
    _NtronNViewPortNumber_Type()
)
ntronNViewPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronNViewPortNumber.setStatus("current")


class _NtronNViewMulticast_Type(Integer32):
    """Custom type ntronNViewMulticast based on Integer32"""
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


_NtronNViewMulticast_Type.__name__ = "Integer32"
_NtronNViewMulticast_Object = MibTableColumn
ntronNViewMulticast = _NtronNViewMulticast_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 2, 3, 1, 2),
    _NtronNViewMulticast_Type()
)
ntronNViewMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronNViewMulticast.setStatus("current")


class _NtronNViewStats_Type(Integer32):
    """Custom type ntronNViewStats based on Integer32"""
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


_NtronNViewStats_Type.__name__ = "Integer32"
_NtronNViewStats_Object = MibTableColumn
ntronNViewStats = _NtronNViewStats_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 2, 3, 1, 3),
    _NtronNViewStats_Type()
)
ntronNViewStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronNViewStats.setStatus("current")
_NtronTFTPGroup_ObjectIdentity = ObjectIdentity
ntronTFTPGroup = _NtronTFTPGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 3)
)
_NtronTFTPServerIpAddress_Type = IpAddress
_NtronTFTPServerIpAddress_Object = MibScalar
ntronTFTPServerIpAddress = _NtronTFTPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 3, 1),
    _NtronTFTPServerIpAddress_Type()
)
ntronTFTPServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronTFTPServerIpAddress.setStatus("current")


class _NtronTFTPRemoteFileName_Type(DisplayString):
    """Custom type ntronTFTPRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtronTFTPRemoteFileName_Type.__name__ = "DisplayString"
_NtronTFTPRemoteFileName_Object = MibScalar
ntronTFTPRemoteFileName = _NtronTFTPRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 3, 2),
    _NtronTFTPRemoteFileName_Type()
)
ntronTFTPRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronTFTPRemoteFileName.setStatus("current")


class _NtronTFTPAction_Type(Integer32):
    """Custom type ntronTFTPAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("downloadImage", 2),
          ("configUpload", 3),
          ("configDownload", 4),
          ("downloadBootImage", 6))
    )


_NtronTFTPAction_Type.__name__ = "Integer32"
_NtronTFTPAction_Object = MibScalar
ntronTFTPAction = _NtronTFTPAction_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 3, 3),
    _NtronTFTPAction_Type()
)
ntronTFTPAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronTFTPAction.setStatus("current")


class _NtronTFTPConfigFlags_Type(Integer32):
    """Custom type ntronTFTPConfigFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32)
        )
    )
    namedValues = NamedValues(
        *(("main", 1),
          ("snmp", 2),
          ("dhcp", 4),
          ("macSec", 8),
          ("macSecManualOnly", 16),
          ("keepCurrentIp", 32))
    )


_NtronTFTPConfigFlags_Type.__name__ = "Integer32"
_NtronTFTPConfigFlags_Object = MibScalar
ntronTFTPConfigFlags = _NtronTFTPConfigFlags_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 3, 4),
    _NtronTFTPConfigFlags_Type()
)
ntronTFTPConfigFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronTFTPConfigFlags.setStatus("current")
_NtronPortMirroringGroup_ObjectIdentity = ObjectIdentity
ntronPortMirroringGroup = _NtronPortMirroringGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 7)
)


class _NtronMirroringState_Type(Integer32):
    """Custom type ntronMirroringState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_NtronMirroringState_Type.__name__ = "Integer32"
_NtronMirroringState_Object = MibScalar
ntronMirroringState = _NtronMirroringState_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 7, 1),
    _NtronMirroringState_Type()
)
ntronMirroringState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronMirroringState.setStatus("current")
_NtronMirroringDestinationPort_Type = Integer32
_NtronMirroringDestinationPort_Object = MibScalar
ntronMirroringDestinationPort = _NtronMirroringDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 7, 2),
    _NtronMirroringDestinationPort_Type()
)
ntronMirroringDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronMirroringDestinationPort.setStatus("current")
_NtronPortMirroringTable_Object = MibTable
ntronPortMirroringTable = _NtronPortMirroringTable_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 7, 3)
)
if mibBuilder.loadTexts:
    ntronPortMirroringTable.setStatus("current")
_NtronPortMirroringEntry_Object = MibTableRow
ntronPortMirroringEntry = _NtronPortMirroringEntry_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 7, 3, 1)
)
ntronPortMirroringEntry.setIndexNames(
    (0, "NTRON714FX6-MIB", "ntronPortMirroringNo"),
)
if mibBuilder.loadTexts:
    ntronPortMirroringEntry.setStatus("current")
_NtronPortMirroringNo_Type = Integer32
_NtronPortMirroringNo_Object = MibTableColumn
ntronPortMirroringNo = _NtronPortMirroringNo_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 7, 3, 1, 1),
    _NtronPortMirroringNo_Type()
)
ntronPortMirroringNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronPortMirroringNo.setStatus("current")
_NtronPortMirroringTx_Type = Integer32
_NtronPortMirroringTx_Object = MibTableColumn
ntronPortMirroringTx = _NtronPortMirroringTx_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 7, 3, 1, 2),
    _NtronPortMirroringTx_Type()
)
ntronPortMirroringTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortMirroringTx.setStatus("current")
_NtronPortMirroringRx_Type = Integer32
_NtronPortMirroringRx_Object = MibTableColumn
ntronPortMirroringRx = _NtronPortMirroringRx_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 7, 3, 1, 3),
    _NtronPortMirroringRx_Type()
)
ntronPortMirroringRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortMirroringRx.setStatus("current")
_NtronPortConfigGroup_ObjectIdentity = ObjectIdentity
ntronPortConfigGroup = _NtronPortConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8)
)
_NtronPortConfigTable_Object = MibTable
ntronPortConfigTable = _NtronPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1)
)
if mibBuilder.loadTexts:
    ntronPortConfigTable.setStatus("current")
_NtronPortConfigEntry_Object = MibTableRow
ntronPortConfigEntry = _NtronPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1)
)
ntronPortConfigEntry.setIndexNames(
    (0, "NTRON714FX6-MIB", "ntronPortNo"),
)
if mibBuilder.loadTexts:
    ntronPortConfigEntry.setStatus("current")
_NtronPortNo_Type = Integer32
_NtronPortNo_Object = MibTableColumn
ntronPortNo = _NtronPortNo_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 1),
    _NtronPortNo_Type()
)
ntronPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronPortNo.setStatus("current")
_NtronPortName_Type = DisplayString
_NtronPortName_Object = MibTableColumn
ntronPortName = _NtronPortName_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 2),
    _NtronPortName_Type()
)
ntronPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronPortName.setStatus("current")


class _NtronPortAdminState_Type(Integer32):
    """Custom type ntronPortAdminState based on Integer32"""
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


_NtronPortAdminState_Type.__name__ = "Integer32"
_NtronPortAdminState_Object = MibTableColumn
ntronPortAdminState = _NtronPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 3),
    _NtronPortAdminState_Type()
)
ntronPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortAdminState.setStatus("current")


class _NtronPortSpeed_Type(Integer32):
    """Custom type ntronPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tenMbps", 1),
          ("hundredMbps", 2),
          ("thousandMbps", 3))
    )


_NtronPortSpeed_Type.__name__ = "Integer32"
_NtronPortSpeed_Object = MibTableColumn
ntronPortSpeed = _NtronPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 4),
    _NtronPortSpeed_Type()
)
ntronPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortSpeed.setStatus("current")


class _NtronPortDuplexStatus_Type(Integer32):
    """Custom type ntronPortDuplexStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )


_NtronPortDuplexStatus_Type.__name__ = "Integer32"
_NtronPortDuplexStatus_Object = MibTableColumn
ntronPortDuplexStatus = _NtronPortDuplexStatus_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 5),
    _NtronPortDuplexStatus_Type()
)
ntronPortDuplexStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortDuplexStatus.setStatus("current")


class _NtronPortLinkState_Type(Integer32):
    """Custom type ntronPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_NtronPortLinkState_Type.__name__ = "Integer32"
_NtronPortLinkState_Object = MibTableColumn
ntronPortLinkState = _NtronPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 6),
    _NtronPortLinkState_Type()
)
ntronPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronPortLinkState.setStatus("current")


class _NtronPortPriority_Type(Integer32):
    """Custom type ntronPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NtronPortPriority_Type.__name__ = "Integer32"
_NtronPortPriority_Object = MibTableColumn
ntronPortPriority = _NtronPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 7),
    _NtronPortPriority_Type()
)
ntronPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortPriority.setStatus("current")


class _NtronPortFlowControl_Type(Integer32):
    """Custom type ntronPortFlowControl based on Integer32"""
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


_NtronPortFlowControl_Type.__name__ = "Integer32"
_NtronPortFlowControl_Object = MibTableColumn
ntronPortFlowControl = _NtronPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 8),
    _NtronPortFlowControl_Type()
)
ntronPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortFlowControl.setStatus("current")


class _NtronPortBackPressure_Type(Integer32):
    """Custom type ntronPortBackPressure based on Integer32"""
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


_NtronPortBackPressure_Type.__name__ = "Integer32"
_NtronPortBackPressure_Object = MibTableColumn
ntronPortBackPressure = _NtronPortBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 9),
    _NtronPortBackPressure_Type()
)
ntronPortBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortBackPressure.setStatus("current")


class _NtronPortAutonegotiation_Type(Integer32):
    """Custom type ntronPortAutonegotiation based on Integer32"""
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


_NtronPortAutonegotiation_Type.__name__ = "Integer32"
_NtronPortAutonegotiation_Object = MibTableColumn
ntronPortAutonegotiation = _NtronPortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 10),
    _NtronPortAutonegotiation_Type()
)
ntronPortAutonegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortAutonegotiation.setStatus("current")


class _NtronPortOverWritePriority_Type(Integer32):
    """Custom type ntronPortOverWritePriority based on Integer32"""
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


_NtronPortOverWritePriority_Type.__name__ = "Integer32"
_NtronPortOverWritePriority_Object = MibTableColumn
ntronPortOverWritePriority = _NtronPortOverWritePriority_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 11),
    _NtronPortOverWritePriority_Type()
)
ntronPortOverWritePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortOverWritePriority.setStatus("current")
_NtronPortPVID_Type = Integer32
_NtronPortPVID_Object = MibTableColumn
ntronPortPVID = _NtronPortPVID_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 12),
    _NtronPortPVID_Type()
)
ntronPortPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortPVID.setStatus("current")


class _NtronPortCrossover_Type(Integer32):
    """Custom type ntronPortCrossover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("yes", 2),
          ("no", 3))
    )


_NtronPortCrossover_Type.__name__ = "Integer32"
_NtronPortCrossover_Object = MibTableColumn
ntronPortCrossover = _NtronPortCrossover_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 8, 1, 1, 13),
    _NtronPortCrossover_Type()
)
ntronPortCrossover.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronPortCrossover.setStatus("current")
_NtronIgmpGroup_ObjectIdentity = ObjectIdentity
ntronIgmpGroup = _NtronIgmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9)
)


class _NtronIgmpState_Type(Integer32):
    """Custom type ntronIgmpState based on Integer32"""
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


_NtronIgmpState_Type.__name__ = "Integer32"
_NtronIgmpState_Object = MibScalar
ntronIgmpState = _NtronIgmpState_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 1),
    _NtronIgmpState_Type()
)
ntronIgmpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronIgmpState.setStatus("current")


class _NtronQueryMode_Type(Integer32):
    """Custom type ntronQueryMode based on Integer32"""
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
          ("auto", 2),
          ("on", 3))
    )


_NtronQueryMode_Type.__name__ = "Integer32"
_NtronQueryMode_Object = MibScalar
ntronQueryMode = _NtronQueryMode_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 2),
    _NtronQueryMode_Type()
)
ntronQueryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronQueryMode.setStatus("current")


class _NtronRouterMode_Type(Integer32):
    """Custom type ntronRouterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("auto", 2),
          ("manual", 3))
    )


_NtronRouterMode_Type.__name__ = "Integer32"
_NtronRouterMode_Object = MibScalar
ntronRouterMode = _NtronRouterMode_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 3),
    _NtronRouterMode_Type()
)
ntronRouterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronRouterMode.setStatus("current")
_NtronIgmpMemberTable_Object = MibTable
ntronIgmpMemberTable = _NtronIgmpMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 4)
)
if mibBuilder.loadTexts:
    ntronIgmpMemberTable.setStatus("current")
_NtronIgmpMemberEntry_Object = MibTableRow
ntronIgmpMemberEntry = _NtronIgmpMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 4, 1)
)
ntronIgmpMemberEntry.setIndexNames(
    (0, "NTRON714FX6-MIB", "ntronIgmpMemberTableIndex"),
)
if mibBuilder.loadTexts:
    ntronIgmpMemberEntry.setStatus("current")
_NtronIgmpMemberTableIndex_Type = Integer32
_NtronIgmpMemberTableIndex_Object = MibTableColumn
ntronIgmpMemberTableIndex = _NtronIgmpMemberTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 4, 1, 1),
    _NtronIgmpMemberTableIndex_Type()
)
ntronIgmpMemberTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIgmpMemberTableIndex.setStatus("current")
_NtronIgmpGroupIpAddress_Type = IpAddress
_NtronIgmpGroupIpAddress_Object = MibTableColumn
ntronIgmpGroupIpAddress = _NtronIgmpGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 4, 1, 2),
    _NtronIgmpGroupIpAddress_Type()
)
ntronIgmpGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIgmpGroupIpAddress.setStatus("current")
_NtronIgmpPortNumber_Type = Integer32
_NtronIgmpPortNumber_Object = MibTableColumn
ntronIgmpPortNumber = _NtronIgmpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 4, 1, 3),
    _NtronIgmpPortNumber_Type()
)
ntronIgmpPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIgmpPortNumber.setStatus("current")
_NtronIgmpVlanId_Type = Integer32
_NtronIgmpVlanId_Object = MibTableColumn
ntronIgmpVlanId = _NtronIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 4, 1, 4),
    _NtronIgmpVlanId_Type()
)
ntronIgmpVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIgmpVlanId.setStatus("current")
_NtronIgmpRouterTable_Object = MibTable
ntronIgmpRouterTable = _NtronIgmpRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 5)
)
if mibBuilder.loadTexts:
    ntronIgmpRouterTable.setStatus("current")
_NtronIgmpRouterEntry_Object = MibTableRow
ntronIgmpRouterEntry = _NtronIgmpRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 5, 1)
)
ntronIgmpRouterEntry.setIndexNames(
    (0, "NTRON714FX6-MIB", "ntronIgmpRouterTableIndex"),
)
if mibBuilder.loadTexts:
    ntronIgmpRouterEntry.setStatus("current")
_NtronIgmpRouterTableIndex_Type = Integer32
_NtronIgmpRouterTableIndex_Object = MibTableColumn
ntronIgmpRouterTableIndex = _NtronIgmpRouterTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 5, 1, 1),
    _NtronIgmpRouterTableIndex_Type()
)
ntronIgmpRouterTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIgmpRouterTableIndex.setStatus("current")
_NtronIgmpRouterIpAddress_Type = IpAddress
_NtronIgmpRouterIpAddress_Object = MibTableColumn
ntronIgmpRouterIpAddress = _NtronIgmpRouterIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 5, 1, 2),
    _NtronIgmpRouterIpAddress_Type()
)
ntronIgmpRouterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIgmpRouterIpAddress.setStatus("current")
_NtronIgmpRouterPortNumber_Type = Integer32
_NtronIgmpRouterPortNumber_Object = MibTableColumn
ntronIgmpRouterPortNumber = _NtronIgmpRouterPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 5, 1, 3),
    _NtronIgmpRouterPortNumber_Type()
)
ntronIgmpRouterPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIgmpRouterPortNumber.setStatus("current")
_NtronIgmpPortTable_Object = MibTable
ntronIgmpPortTable = _NtronIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 6)
)
if mibBuilder.loadTexts:
    ntronIgmpPortTable.setStatus("current")
_NtronIgmpPortEntry_Object = MibTableRow
ntronIgmpPortEntry = _NtronIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 6, 1)
)
ntronIgmpPortEntry.setIndexNames(
    (0, "NTRON714FX6-MIB", "ntronIgmpPortTableIndex"),
)
if mibBuilder.loadTexts:
    ntronIgmpPortEntry.setStatus("current")
_NtronIgmpPortTableIndex_Type = Integer32
_NtronIgmpPortTableIndex_Object = MibTableColumn
ntronIgmpPortTableIndex = _NtronIgmpPortTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 6, 1, 1),
    _NtronIgmpPortTableIndex_Type()
)
ntronIgmpPortTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronIgmpPortTableIndex.setStatus("current")


class _NtronIgmpPortManRouter_Type(Integer32):
    """Custom type ntronIgmpPortManRouter based on Integer32"""
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


_NtronIgmpPortManRouter_Type.__name__ = "Integer32"
_NtronIgmpPortManRouter_Object = MibTableColumn
ntronIgmpPortManRouter = _NtronIgmpPortManRouter_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 6, 1, 2),
    _NtronIgmpPortManRouter_Type()
)
ntronIgmpPortManRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronIgmpPortManRouter.setStatus("current")


class _NtronIgmpPortRFilter_Type(Integer32):
    """Custom type ntronIgmpPortRFilter based on Integer32"""
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


_NtronIgmpPortRFilter_Type.__name__ = "Integer32"
_NtronIgmpPortRFilter_Object = MibTableColumn
ntronIgmpPortRFilter = _NtronIgmpPortRFilter_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 9, 6, 1, 3),
    _NtronIgmpPortRFilter_Type()
)
ntronIgmpPortRFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronIgmpPortRFilter.setStatus("current")
_NtronBroadcastGroup_ObjectIdentity = ObjectIdentity
ntronBroadcastGroup = _NtronBroadcastGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 13)
)
_NtronBroadcastBPCLTable_Object = MibTable
ntronBroadcastBPCLTable = _NtronBroadcastBPCLTable_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 13, 1)
)
if mibBuilder.loadTexts:
    ntronBroadcastBPCLTable.setStatus("current")
_NtronBroadcastBPCLEntry_Object = MibTableRow
ntronBroadcastBPCLEntry = _NtronBroadcastBPCLEntry_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 13, 1, 1)
)
ntronBroadcastBPCLEntry.setIndexNames(
    (0, "NTRON714FX6-MIB", "ntronBroadcastPortNumber"),
)
if mibBuilder.loadTexts:
    ntronBroadcastBPCLEntry.setStatus("current")
_NtronBroadcastPortNumber_Type = Integer32
_NtronBroadcastPortNumber_Object = MibTableColumn
ntronBroadcastPortNumber = _NtronBroadcastPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 13, 1, 1, 1),
    _NtronBroadcastPortNumber_Type()
)
ntronBroadcastPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronBroadcastPortNumber.setStatus("current")


class _NtronBroadcastPercentage_Type(Integer32):
    """Custom type ntronBroadcastPercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NtronBroadcastPercentage_Type.__name__ = "Integer32"
_NtronBroadcastPercentage_Object = MibTableColumn
ntronBroadcastPercentage = _NtronBroadcastPercentage_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 13, 1, 1, 2),
    _NtronBroadcastPercentage_Type()
)
ntronBroadcastPercentage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronBroadcastPercentage.setStatus("current")
_NtronConfigGroup_ObjectIdentity = ObjectIdentity
ntronConfigGroup = _NtronConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 14)
)


class _NtronConfigSave_Type(Integer32):
    """Custom type ntronConfigSave based on Integer32"""
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


_NtronConfigSave_Type.__name__ = "Integer32"
_NtronConfigSave_Object = MibScalar
ntronConfigSave = _NtronConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 14, 1),
    _NtronConfigSave_Type()
)
ntronConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronConfigSave.setStatus("current")


class _NtronConfigErase_Type(Integer32):
    """Custom type ntronConfigErase based on Integer32"""
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
        *(("disable", 1),
          ("enable", 2),
          ("keepip", 3),
          ("keepusers", 4),
          ("keepipandusers", 5))
    )


_NtronConfigErase_Type.__name__ = "Integer32"
_NtronConfigErase_Object = MibScalar
ntronConfigErase = _NtronConfigErase_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 14, 2),
    _NtronConfigErase_Type()
)
ntronConfigErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronConfigErase.setStatus("current")


class _NtronConfigEraseFlags_Type(Integer32):
    """Custom type ntronConfigEraseFlags based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("keepIp", 1),
          ("keepUsers", 2),
          ("keepSNMP", 4),
          ("keepDHCPS", 8),
          ("keepMacSec", 16))
    )


_NtronConfigEraseFlags_Type.__name__ = "Integer32"
_NtronConfigEraseFlags_Object = MibScalar
ntronConfigEraseFlags = _NtronConfigEraseFlags_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 14, 3),
    _NtronConfigEraseFlags_Type()
)
ntronConfigEraseFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronConfigEraseFlags.setStatus("current")
_NtronSnmpGroup_ObjectIdentity = ObjectIdentity
ntronSnmpGroup = _NtronSnmpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 15)
)


class _NtronSnmpGetCommunityName_Type(DisplayString):
    """Custom type ntronSnmpGetCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 15),
    )


_NtronSnmpGetCommunityName_Type.__name__ = "DisplayString"
_NtronSnmpGetCommunityName_Object = MibScalar
ntronSnmpGetCommunityName = _NtronSnmpGetCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 15, 1),
    _NtronSnmpGetCommunityName_Type()
)
ntronSnmpGetCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronSnmpGetCommunityName.setStatus("current")


class _NtronSnmpTrapCommunityName_Type(DisplayString):
    """Custom type ntronSnmpTrapCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 15),
    )


_NtronSnmpTrapCommunityName_Type.__name__ = "DisplayString"
_NtronSnmpTrapCommunityName_Object = MibScalar
ntronSnmpTrapCommunityName = _NtronSnmpTrapCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 15, 2),
    _NtronSnmpTrapCommunityName_Type()
)
ntronSnmpTrapCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronSnmpTrapCommunityName.setStatus("current")
_NtronSnmpManagerIpAddressTable_Object = MibTable
ntronSnmpManagerIpAddressTable = _NtronSnmpManagerIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 15, 3)
)
if mibBuilder.loadTexts:
    ntronSnmpManagerIpAddressTable.setStatus("current")
_NtronSnmpManagerIpAddressEntry_Object = MibTableRow
ntronSnmpManagerIpAddressEntry = _NtronSnmpManagerIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 15, 3, 1)
)
ntronSnmpManagerIpAddressEntry.setIndexNames(
    (0, "NTRON714FX6-MIB", "ntronSnmpManagerTableIndex"),
)
if mibBuilder.loadTexts:
    ntronSnmpManagerIpAddressEntry.setStatus("current")
_NtronSnmpManagerTableIndex_Type = Integer32
_NtronSnmpManagerTableIndex_Object = MibTableColumn
ntronSnmpManagerTableIndex = _NtronSnmpManagerTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 15, 3, 1, 1),
    _NtronSnmpManagerTableIndex_Type()
)
ntronSnmpManagerTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronSnmpManagerTableIndex.setStatus("current")
_NtronSnmpManagerIpAddress_Type = IpAddress
_NtronSnmpManagerIpAddress_Object = MibTableColumn
ntronSnmpManagerIpAddress = _NtronSnmpManagerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 15, 3, 1, 2),
    _NtronSnmpManagerIpAddress_Type()
)
ntronSnmpManagerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntronSnmpManagerIpAddress.setStatus("current")
_NtronNRingGroup_ObjectIdentity = ObjectIdentity
ntronNRingGroup = _NtronNRingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 16)
)


class _NtronNRingMode_Type(Integer32):
    """Custom type ntronNRingMode based on Integer32"""
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
        *(("disabled", 1),
          ("automember", 2),
          ("activemember", 3),
          ("manager", 4),
          ("multimember", 5))
    )


_NtronNRingMode_Type.__name__ = "Integer32"
_NtronNRingMode_Object = MibScalar
ntronNRingMode = _NtronNRingMode_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 16, 1),
    _NtronNRingMode_Type()
)
ntronNRingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronNRingMode.setStatus("current")


class _NtronNRingState_Type(Integer32):
    """Custom type ntronNRingState based on Integer32"""
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
        *(("healthy", 1),
          ("broken-lo", 2),
          ("broken-hi", 3),
          ("broken", 4))
    )


_NtronNRingState_Type.__name__ = "Integer32"
_NtronNRingState_Object = MibScalar
ntronNRingState = _NtronNRingState_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 16, 2),
    _NtronNRingState_Type()
)
ntronNRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronNRingState.setStatus("current")
_NtronNRingVersion_Type = Integer32
_NtronNRingVersion_Object = MibScalar
ntronNRingVersion = _NtronNRingVersion_Object(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 16, 3),
    _NtronNRingVersion_Type()
)
ntronNRingVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntronNRingVersion.setStatus("current")
_NtronTrapGroup_ObjectIdentity = ObjectIdentity
ntronTrapGroup = _NtronTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 18)
)

# Managed Objects groups


# Notification objects

ntronPowerChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 28381, 700, 7, 18, 1)
)
ntronPowerChange.setObjects(
    ("NTRON714FX6-MIB", "ntronPowerFault")
)
if mibBuilder.loadTexts:
    ntronPowerChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NTRON714FX6-MIB",
    **{"ntron": ntron,
       "ntron7xx": ntron7xx,
       "ntron714fx6": ntron714fx6,
       "ntronSysGroup": ntronSysGroup,
       "ntronSysReset": ntronSysReset,
       "ntronSwVersion": ntronSwVersion,
       "ntronBuildDateAndTime": ntronBuildDateAndTime,
       "ntronTotalRam": ntronTotalRam,
       "ntronTotalFlash": ntronTotalFlash,
       "ntronEthernetPortCount": ntronEthernetPortCount,
       "ntronCurrentIpAddress": ntronCurrentIpAddress,
       "ntronConfiguredIpAddress": ntronConfiguredIpAddress,
       "ntronConfiguredSubnetMask": ntronConfiguredSubnetMask,
       "ntronConfiguredGateway": ntronConfiguredGateway,
       "ntronUpdateConfiguredIpAddr": ntronUpdateConfiguredIpAddr,
       "ntronIPAddressStatus": ntronIPAddressStatus,
       "ntronTotalNoOfPorts": ntronTotalNoOfPorts,
       "ntronMacAddress": ntronMacAddress,
       "ntronContactStatus": ntronContactStatus,
       "ntronPowerFault": ntronPowerFault,
       "ntronModelString": ntronModelString,
       "ntronBlVersion": ntronBlVersion,
       "ntronNViewGroup": ntronNViewGroup,
       "ntronNViewState": ntronNViewState,
       "ntronNViewInterval": ntronNViewInterval,
       "ntronNViewTable": ntronNViewTable,
       "ntronNViewEntry": ntronNViewEntry,
       "ntronNViewPortNumber": ntronNViewPortNumber,
       "ntronNViewMulticast": ntronNViewMulticast,
       "ntronNViewStats": ntronNViewStats,
       "ntronTFTPGroup": ntronTFTPGroup,
       "ntronTFTPServerIpAddress": ntronTFTPServerIpAddress,
       "ntronTFTPRemoteFileName": ntronTFTPRemoteFileName,
       "ntronTFTPAction": ntronTFTPAction,
       "ntronTFTPConfigFlags": ntronTFTPConfigFlags,
       "ntronPortMirroringGroup": ntronPortMirroringGroup,
       "ntronMirroringState": ntronMirroringState,
       "ntronMirroringDestinationPort": ntronMirroringDestinationPort,
       "ntronPortMirroringTable": ntronPortMirroringTable,
       "ntronPortMirroringEntry": ntronPortMirroringEntry,
       "ntronPortMirroringNo": ntronPortMirroringNo,
       "ntronPortMirroringTx": ntronPortMirroringTx,
       "ntronPortMirroringRx": ntronPortMirroringRx,
       "ntronPortConfigGroup": ntronPortConfigGroup,
       "ntronPortConfigTable": ntronPortConfigTable,
       "ntronPortConfigEntry": ntronPortConfigEntry,
       "ntronPortNo": ntronPortNo,
       "ntronPortName": ntronPortName,
       "ntronPortAdminState": ntronPortAdminState,
       "ntronPortSpeed": ntronPortSpeed,
       "ntronPortDuplexStatus": ntronPortDuplexStatus,
       "ntronPortLinkState": ntronPortLinkState,
       "ntronPortPriority": ntronPortPriority,
       "ntronPortFlowControl": ntronPortFlowControl,
       "ntronPortBackPressure": ntronPortBackPressure,
       "ntronPortAutonegotiation": ntronPortAutonegotiation,
       "ntronPortOverWritePriority": ntronPortOverWritePriority,
       "ntronPortPVID": ntronPortPVID,
       "ntronPortCrossover": ntronPortCrossover,
       "ntronIgmpGroup": ntronIgmpGroup,
       "ntronIgmpState": ntronIgmpState,
       "ntronQueryMode": ntronQueryMode,
       "ntronRouterMode": ntronRouterMode,
       "ntronIgmpMemberTable": ntronIgmpMemberTable,
       "ntronIgmpMemberEntry": ntronIgmpMemberEntry,
       "ntronIgmpMemberTableIndex": ntronIgmpMemberTableIndex,
       "ntronIgmpGroupIpAddress": ntronIgmpGroupIpAddress,
       "ntronIgmpPortNumber": ntronIgmpPortNumber,
       "ntronIgmpVlanId": ntronIgmpVlanId,
       "ntronIgmpRouterTable": ntronIgmpRouterTable,
       "ntronIgmpRouterEntry": ntronIgmpRouterEntry,
       "ntronIgmpRouterTableIndex": ntronIgmpRouterTableIndex,
       "ntronIgmpRouterIpAddress": ntronIgmpRouterIpAddress,
       "ntronIgmpRouterPortNumber": ntronIgmpRouterPortNumber,
       "ntronIgmpPortTable": ntronIgmpPortTable,
       "ntronIgmpPortEntry": ntronIgmpPortEntry,
       "ntronIgmpPortTableIndex": ntronIgmpPortTableIndex,
       "ntronIgmpPortManRouter": ntronIgmpPortManRouter,
       "ntronIgmpPortRFilter": ntronIgmpPortRFilter,
       "ntronBroadcastGroup": ntronBroadcastGroup,
       "ntronBroadcastBPCLTable": ntronBroadcastBPCLTable,
       "ntronBroadcastBPCLEntry": ntronBroadcastBPCLEntry,
       "ntronBroadcastPortNumber": ntronBroadcastPortNumber,
       "ntronBroadcastPercentage": ntronBroadcastPercentage,
       "ntronConfigGroup": ntronConfigGroup,
       "ntronConfigSave": ntronConfigSave,
       "ntronConfigErase": ntronConfigErase,
       "ntronConfigEraseFlags": ntronConfigEraseFlags,
       "ntronSnmpGroup": ntronSnmpGroup,
       "ntronSnmpGetCommunityName": ntronSnmpGetCommunityName,
       "ntronSnmpTrapCommunityName": ntronSnmpTrapCommunityName,
       "ntronSnmpManagerIpAddressTable": ntronSnmpManagerIpAddressTable,
       "ntronSnmpManagerIpAddressEntry": ntronSnmpManagerIpAddressEntry,
       "ntronSnmpManagerTableIndex": ntronSnmpManagerTableIndex,
       "ntronSnmpManagerIpAddress": ntronSnmpManagerIpAddress,
       "ntronNRingGroup": ntronNRingGroup,
       "ntronNRingMode": ntronNRingMode,
       "ntronNRingState": ntronNRingState,
       "ntronNRingVersion": ntronNRingVersion,
       "ntronTrapGroup": ntronTrapGroup,
       "ntronPowerChange": ntronPowerChange}
)
