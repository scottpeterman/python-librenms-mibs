# SNMP MIB module (CISCOSB-DHCPCL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCOSB-DHCPCL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:28:29 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlDhcpCl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76)
)
if mibBuilder.loadTexts:
    rlDhcpCl.setRevisions(
        ("2007-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RlDhcpClActionTable_Object = MibTable
rlDhcpClActionTable = _RlDhcpClActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 3)
)
if mibBuilder.loadTexts:
    rlDhcpClActionTable.setStatus("current")
_RlDhcpClActionEntry_Object = MibTableRow
rlDhcpClActionEntry = _RlDhcpClActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 3, 1)
)
rlDhcpClActionEntry.setIndexNames(
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpClActionIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClActionEntry.setStatus("current")
_RlDhcpClActionIfIndex_Type = InterfaceIndex
_RlDhcpClActionIfIndex_Object = MibTableColumn
rlDhcpClActionIfIndex = _RlDhcpClActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 3, 1, 1),
    _RlDhcpClActionIfIndex_Type()
)
rlDhcpClActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClActionIfIndex.setStatus("current")
_RlDhcpClActionStatus_Type = RowStatus
_RlDhcpClActionStatus_Object = MibTableColumn
rlDhcpClActionStatus = _RlDhcpClActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 3, 1, 2),
    _RlDhcpClActionStatus_Type()
)
rlDhcpClActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpClActionStatus.setStatus("current")


class _RlDhcpClActionHostName_Type(SnmpAdminString):
    """Custom type rlDhcpClActionHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RlDhcpClActionHostName_Type.__name__ = "SnmpAdminString"
_RlDhcpClActionHostName_Object = MibTableColumn
rlDhcpClActionHostName = _RlDhcpClActionHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 3, 1, 3),
    _RlDhcpClActionHostName_Type()
)
rlDhcpClActionHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpClActionHostName.setStatus("current")
_RlDhcpApprovalEnabled_Type = TruthValue
_RlDhcpApprovalEnabled_Object = MibScalar
rlDhcpApprovalEnabled = _RlDhcpApprovalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 4),
    _RlDhcpApprovalEnabled_Type()
)
rlDhcpApprovalEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalEnabled.setStatus("current")
_RlDhcpApprovalWaitingTable_Object = MibTable
rlDhcpApprovalWaitingTable = _RlDhcpApprovalWaitingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 5)
)
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingTable.setStatus("current")
_RlDhcpApprovalWaitingEntry_Object = MibTableRow
rlDhcpApprovalWaitingEntry = _RlDhcpApprovalWaitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 5, 1)
)
rlDhcpApprovalWaitingEntry.setIndexNames(
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpApprovalWaitingIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingEntry.setStatus("current")
_RlDhcpApprovalWaitingIfIndex_Type = InterfaceIndex
_RlDhcpApprovalWaitingIfIndex_Object = MibTableColumn
rlDhcpApprovalWaitingIfIndex = _RlDhcpApprovalWaitingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 5, 1, 1),
    _RlDhcpApprovalWaitingIfIndex_Type()
)
rlDhcpApprovalWaitingIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingIfIndex.setStatus("current")
_RlDhcpApprovalWaitingAddress_Type = IpAddress
_RlDhcpApprovalWaitingAddress_Object = MibTableColumn
rlDhcpApprovalWaitingAddress = _RlDhcpApprovalWaitingAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 5, 1, 2),
    _RlDhcpApprovalWaitingAddress_Type()
)
rlDhcpApprovalWaitingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingAddress.setStatus("current")
_RlDhcpApprovalWaitingMask_Type = IpAddress
_RlDhcpApprovalWaitingMask_Object = MibTableColumn
rlDhcpApprovalWaitingMask = _RlDhcpApprovalWaitingMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 5, 1, 3),
    _RlDhcpApprovalWaitingMask_Type()
)
rlDhcpApprovalWaitingMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingMask.setStatus("current")
_RlDhcpApprovalWaitingGateway_Type = IpAddress
_RlDhcpApprovalWaitingGateway_Object = MibTableColumn
rlDhcpApprovalWaitingGateway = _RlDhcpApprovalWaitingGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 5, 1, 4),
    _RlDhcpApprovalWaitingGateway_Type()
)
rlDhcpApprovalWaitingGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalWaitingGateway.setStatus("current")
_RlDhcpApprovalActionTable_Object = MibTable
rlDhcpApprovalActionTable = _RlDhcpApprovalActionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 6)
)
if mibBuilder.loadTexts:
    rlDhcpApprovalActionTable.setStatus("current")
_RlDhcpApprovalActionEntry_Object = MibTableRow
rlDhcpApprovalActionEntry = _RlDhcpApprovalActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 6, 1)
)
rlDhcpApprovalActionEntry.setIndexNames(
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpApprovalActionIfIndex"),
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpApprovalActionAddress"),
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpApprovalActionMask"),
)
if mibBuilder.loadTexts:
    rlDhcpApprovalActionEntry.setStatus("current")
_RlDhcpApprovalActionIfIndex_Type = InterfaceIndex
_RlDhcpApprovalActionIfIndex_Object = MibTableColumn
rlDhcpApprovalActionIfIndex = _RlDhcpApprovalActionIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 6, 1, 1),
    _RlDhcpApprovalActionIfIndex_Type()
)
rlDhcpApprovalActionIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionIfIndex.setStatus("current")
_RlDhcpApprovalActionAddress_Type = IpAddress
_RlDhcpApprovalActionAddress_Object = MibTableColumn
rlDhcpApprovalActionAddress = _RlDhcpApprovalActionAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 6, 1, 2),
    _RlDhcpApprovalActionAddress_Type()
)
rlDhcpApprovalActionAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionAddress.setStatus("current")
_RlDhcpApprovalActionMask_Type = IpAddress
_RlDhcpApprovalActionMask_Object = MibTableColumn
rlDhcpApprovalActionMask = _RlDhcpApprovalActionMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 6, 1, 3),
    _RlDhcpApprovalActionMask_Type()
)
rlDhcpApprovalActionMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionMask.setStatus("current")
_RlDhcpApprovalActionApprove_Type = TruthValue
_RlDhcpApprovalActionApprove_Object = MibTableColumn
rlDhcpApprovalActionApprove = _RlDhcpApprovalActionApprove_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 6, 1, 4),
    _RlDhcpApprovalActionApprove_Type()
)
rlDhcpApprovalActionApprove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpApprovalActionApprove.setStatus("current")
_RlDhcpClCommandTable_Object = MibTable
rlDhcpClCommandTable = _RlDhcpClCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 7)
)
if mibBuilder.loadTexts:
    rlDhcpClCommandTable.setStatus("current")
_RlDhcpClCommandEntry_Object = MibTableRow
rlDhcpClCommandEntry = _RlDhcpClCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 7, 1)
)
rlDhcpClCommandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClCommandEntry.setStatus("current")


class _RlDhcpClCommandAction_Type(Integer32):
    """Custom type rlDhcpClCommandAction based on Integer32"""
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
          ("renew", 1),
          ("renewForceAutoconfig", 2))
    )


_RlDhcpClCommandAction_Type.__name__ = "Integer32"
_RlDhcpClCommandAction_Object = MibTableColumn
rlDhcpClCommandAction = _RlDhcpClCommandAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 7, 1, 2),
    _RlDhcpClCommandAction_Type()
)
rlDhcpClCommandAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClCommandAction.setStatus("current")


class _RlDhcpClConfigurationFileName_Type(DisplayString):
    """Custom type rlDhcpClConfigurationFileName based on DisplayString"""
    defaultValue = OctetString("")


_RlDhcpClConfigurationFileName_Type.__name__ = "DisplayString"
_RlDhcpClConfigurationFileName_Object = MibScalar
rlDhcpClConfigurationFileName = _RlDhcpClConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 8),
    _RlDhcpClConfigurationFileName_Type()
)
rlDhcpClConfigurationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClConfigurationFileName.setStatus("current")


class _RlDhcpClOption67Enable_Type(Integer32):
    """Custom type rlDhcpClOption67Enable based on Integer32"""
    defaultValue = 1

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


_RlDhcpClOption67Enable_Type.__name__ = "Integer32"
_RlDhcpClOption67Enable_Object = MibScalar
rlDhcpClOption67Enable = _RlDhcpClOption67Enable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 9),
    _RlDhcpClOption67Enable_Type()
)
rlDhcpClOption67Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClOption67Enable.setStatus("current")
_RlDhcpClManualTftpServerAddress_Type = IpAddress
_RlDhcpClManualTftpServerAddress_Object = MibScalar
rlDhcpClManualTftpServerAddress = _RlDhcpClManualTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 10),
    _RlDhcpClManualTftpServerAddress_Type()
)
rlDhcpClManualTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClManualTftpServerAddress.setStatus("current")
_RlDhcpClSelectedTftpServerAddress_Type = IpAddress
_RlDhcpClSelectedTftpServerAddress_Object = MibScalar
rlDhcpClSelectedTftpServerAddress = _RlDhcpClSelectedTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 11),
    _RlDhcpClSelectedTftpServerAddress_Type()
)
rlDhcpClSelectedTftpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedTftpServerAddress.setStatus("current")


class _RlDhcpClSelectedTftpServerAddressOrigin_Type(Integer32):
    """Custom type rlDhcpClSelectedTftpServerAddressOrigin based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("sname", 1),
          ("option66", 2),
          ("option150", 3),
          ("option129", 4),
          ("siaddr", 5),
          ("manual", 6),
          ("unknown", 7),
          ("none", 8),
          ("optionv6-59", 9),
          ("broadcastReply", 10))
    )


_RlDhcpClSelectedTftpServerAddressOrigin_Type.__name__ = "Integer32"
_RlDhcpClSelectedTftpServerAddressOrigin_Object = MibScalar
rlDhcpClSelectedTftpServerAddressOrigin = _RlDhcpClSelectedTftpServerAddressOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 12),
    _RlDhcpClSelectedTftpServerAddressOrigin_Type()
)
rlDhcpClSelectedTftpServerAddressOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedTftpServerAddressOrigin.setStatus("current")


class _RlDhcpClManualConfigurationFileName_Type(DisplayString):
    """Custom type rlDhcpClManualConfigurationFileName based on DisplayString"""
    defaultValue = OctetString("")


_RlDhcpClManualConfigurationFileName_Type.__name__ = "DisplayString"
_RlDhcpClManualConfigurationFileName_Object = MibScalar
rlDhcpClManualConfigurationFileName = _RlDhcpClManualConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 13),
    _RlDhcpClManualConfigurationFileName_Type()
)
rlDhcpClManualConfigurationFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClManualConfigurationFileName.setStatus("current")
_RlDhcpClSelectedConfigurationFileName_Type = DisplayString
_RlDhcpClSelectedConfigurationFileName_Object = MibScalar
rlDhcpClSelectedConfigurationFileName = _RlDhcpClSelectedConfigurationFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 14),
    _RlDhcpClSelectedConfigurationFileName_Type()
)
rlDhcpClSelectedConfigurationFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedConfigurationFileName.setStatus("current")


class _RlDhcpClSelectedConfigurationFileNameOrigin_Type(Integer32):
    """Custom type rlDhcpClSelectedConfigurationFileNameOrigin based on Integer32"""
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
        *(("file", 1),
          ("option67", 2),
          ("manual", 3),
          ("none", 4),
          ("hostname", 5),
          ("defaultConfigFile", 6),
          ("optionv6-60", 7))
    )


_RlDhcpClSelectedConfigurationFileNameOrigin_Type.__name__ = "Integer32"
_RlDhcpClSelectedConfigurationFileNameOrigin_Object = MibScalar
rlDhcpClSelectedConfigurationFileNameOrigin = _RlDhcpClSelectedConfigurationFileNameOrigin_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 15),
    _RlDhcpClSelectedConfigurationFileNameOrigin_Type()
)
rlDhcpClSelectedConfigurationFileNameOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedConfigurationFileNameOrigin.setStatus("current")


class _RlDhcpClEnabledByDefaultRemovedIfindex_Type(Integer32):
    """Custom type rlDhcpClEnabledByDefaultRemovedIfindex based on Integer32"""
    defaultValue = 0


_RlDhcpClEnabledByDefaultRemovedIfindex_Type.__name__ = "Integer32"
_RlDhcpClEnabledByDefaultRemovedIfindex_Object = MibScalar
rlDhcpClEnabledByDefaultRemovedIfindex = _RlDhcpClEnabledByDefaultRemovedIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 16),
    _RlDhcpClEnabledByDefaultRemovedIfindex_Type()
)
rlDhcpClEnabledByDefaultRemovedIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClEnabledByDefaultRemovedIfindex.setStatus("current")
_RlDhcpClAutoUpdateEnabled_Type = TruthValue
_RlDhcpClAutoUpdateEnabled_Object = MibScalar
rlDhcpClAutoUpdateEnabled = _RlDhcpClAutoUpdateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 17),
    _RlDhcpClAutoUpdateEnabled_Type()
)
rlDhcpClAutoUpdateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoUpdateEnabled.setStatus("current")


class _RlDhcpClAutoUpdateStatus_Type(Integer32):
    """Custom type rlDhcpClAutoUpdateStatus based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("noData", 1),
          ("openingIndirectFile", 2),
          ("downloadedIndirectFile", 3),
          ("startDownloadImageFile", 4),
          ("failedToDownloadImageFile", 5),
          ("quitFileContentsLenZero", 6),
          ("quitImageFileNameLenZero", 7),
          ("quitVersionAlreadyUpdated", 8),
          ("quitIndirectFileNotFound", 9),
          ("quitImageFileNotFound", 10),
          ("quitImageVersionNotSupported", 11),
          ("quitNoTftpOutgoingInterface", 12),
          ("quitUsbSetupFileOpenError", 13),
          ("quitUsbSetupFileFormatError", 14),
          ("quitUsbSetupFileReadWriteError", 15),
          ("quitUsbSetupFileSetIpAddrError", 16),
          ("quitUsbSetupFileImageFileNotExist", 17),
          ("quitUsbSetupFileConfigFileNotExist", 18))
    )


_RlDhcpClAutoUpdateStatus_Type.__name__ = "Integer32"
_RlDhcpClAutoUpdateStatus_Object = MibScalar
rlDhcpClAutoUpdateStatus = _RlDhcpClAutoUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 18),
    _RlDhcpClAutoUpdateStatus_Type()
)
rlDhcpClAutoUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClAutoUpdateStatus.setStatus("current")
_RlDhcpClAutoConfigForce_Type = TruthValue
_RlDhcpClAutoConfigForce_Object = MibScalar
rlDhcpClAutoConfigForce = _RlDhcpClAutoConfigForce_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 19),
    _RlDhcpClAutoConfigForce_Type()
)
rlDhcpClAutoConfigForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoConfigForce.setStatus("current")
_RlDhcpClAutoConfigAutoSave_Type = TruthValue
_RlDhcpClAutoConfigAutoSave_Object = MibScalar
rlDhcpClAutoConfigAutoSave = _RlDhcpClAutoConfigAutoSave_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 20),
    _RlDhcpClAutoConfigAutoSave_Type()
)
rlDhcpClAutoConfigAutoSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoConfigAutoSave.setStatus("current")


class _RlDhcpClAutoConfigStatus_Type(Integer32):
    """Custom type rlDhcpClAutoConfigStatus based on Integer32"""
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("noData", 1),
          ("openingDhcpConfigFile", 2),
          ("openingIndirectFile", 3),
          ("searchingHostnameInIndirectFile", 4),
          ("openingHostnameConfigFile", 5),
          ("openingHostnameCfgFile", 6),
          ("openingDefaultConfigFile", 7),
          ("downloadingConfigFile", 8),
          ("savingConfigInStartupCDB", 9),
          ("quitDhcpFileNotGivenOrNotExists", 10),
          ("quitFailedToFindAnyExistingConfigFile", 11),
          ("quitConfigFileContentsLenZero", 12),
          ("quitConfigFileDownloadFailed", 13),
          ("quitConditionsForAutoConfigChanged", 14),
          ("quitSelectedConfigFileNameUpdateFailed", 15),
          ("quitSelectedConfigFileNameOriginUpdateFailed", 16),
          ("quitSelectedTftpServerAddressUpdateFailed", 17),
          ("quitSelectedTftpServerAddressOriginUpdateFailed", 18),
          ("quitCopyRunningToStartupFailed", 19),
          ("quitNoTftpOutgoingInterface", 20),
          ("finishedSuccessfully", 21))
    )


_RlDhcpClAutoConfigStatus_Type.__name__ = "Integer32"
_RlDhcpClAutoConfigStatus_Object = MibScalar
rlDhcpClAutoConfigStatus = _RlDhcpClAutoConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 21),
    _RlDhcpClAutoConfigStatus_Type()
)
rlDhcpClAutoConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClAutoConfigStatus.setStatus("current")


class _RlDhcpClAutoConfigProtocol_Type(Integer32):
    """Custom type rlDhcpClAutoConfigProtocol based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("scp", 2),
          ("auto", 3))
    )


_RlDhcpClAutoConfigProtocol_Type.__name__ = "Integer32"
_RlDhcpClAutoConfigProtocol_Object = MibScalar
rlDhcpClAutoConfigProtocol = _RlDhcpClAutoConfigProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 22),
    _RlDhcpClAutoConfigProtocol_Type()
)
rlDhcpClAutoConfigProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoConfigProtocol.setStatus("current")


class _RlDhcpClAutoConfigScpFileExtention_Type(DisplayString):
    """Custom type rlDhcpClAutoConfigScpFileExtention based on DisplayString"""
    defaultValue = OctetString("scp")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpClAutoConfigScpFileExtention_Type.__name__ = "DisplayString"
_RlDhcpClAutoConfigScpFileExtention_Object = MibScalar
rlDhcpClAutoConfigScpFileExtention = _RlDhcpClAutoConfigScpFileExtention_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 23),
    _RlDhcpClAutoConfigScpFileExtention_Type()
)
rlDhcpClAutoConfigScpFileExtention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoConfigScpFileExtention.setStatus("current")
_RlDhcpClSelectedTftpServerInetAddressType_Type = InetAddressType
_RlDhcpClSelectedTftpServerInetAddressType_Object = MibScalar
rlDhcpClSelectedTftpServerInetAddressType = _RlDhcpClSelectedTftpServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 24),
    _RlDhcpClSelectedTftpServerInetAddressType_Type()
)
rlDhcpClSelectedTftpServerInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedTftpServerInetAddressType.setStatus("current")
_RlDhcpClSelectedTftpServerInetAddress_Type = InetAddress
_RlDhcpClSelectedTftpServerInetAddress_Object = MibScalar
rlDhcpClSelectedTftpServerInetAddress = _RlDhcpClSelectedTftpServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 25),
    _RlDhcpClSelectedTftpServerInetAddress_Type()
)
rlDhcpClSelectedTftpServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClSelectedTftpServerInetAddress.setStatus("current")
_RlDhcpClManualAutoConfigDataTable_Object = MibTable
rlDhcpClManualAutoConfigDataTable = _RlDhcpClManualAutoConfigDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 26)
)
if mibBuilder.loadTexts:
    rlDhcpClManualAutoConfigDataTable.setStatus("current")
_RlDhcpClManualAutoConfigDataEntry_Object = MibTableRow
rlDhcpClManualAutoConfigDataEntry = _RlDhcpClManualAutoConfigDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 26, 1)
)
rlDhcpClManualAutoConfigDataEntry.setIndexNames(
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpClManualAutoConfigDataIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClManualAutoConfigDataEntry.setStatus("current")
_RlDhcpClManualAutoConfigDataIndex_Type = Integer32
_RlDhcpClManualAutoConfigDataIndex_Object = MibTableColumn
rlDhcpClManualAutoConfigDataIndex = _RlDhcpClManualAutoConfigDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 26, 1, 1),
    _RlDhcpClManualAutoConfigDataIndex_Type()
)
rlDhcpClManualAutoConfigDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpClManualAutoConfigDataIndex.setStatus("current")
_RlDhcpClManualServerInetAddressType_Type = InetAddressType
_RlDhcpClManualServerInetAddressType_Object = MibTableColumn
rlDhcpClManualServerInetAddressType = _RlDhcpClManualServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 26, 1, 2),
    _RlDhcpClManualServerInetAddressType_Type()
)
rlDhcpClManualServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClManualServerInetAddressType.setStatus("current")
_RlDhcpClManualServerInetAddress_Type = InetAddress
_RlDhcpClManualServerInetAddress_Object = MibTableColumn
rlDhcpClManualServerInetAddress = _RlDhcpClManualServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 26, 1, 3),
    _RlDhcpClManualServerInetAddress_Type()
)
rlDhcpClManualServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClManualServerInetAddress.setStatus("current")
_RlDhcpClManualImageIndirectFileName_Type = DisplayString
_RlDhcpClManualImageIndirectFileName_Object = MibTableColumn
rlDhcpClManualImageIndirectFileName = _RlDhcpClManualImageIndirectFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 26, 1, 4),
    _RlDhcpClManualImageIndirectFileName_Type()
)
rlDhcpClManualImageIndirectFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClManualImageIndirectFileName.setStatus("current")
_RlDhcpClInformationTable_Object = MibTable
rlDhcpClInformationTable = _RlDhcpClInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27)
)
if mibBuilder.loadTexts:
    rlDhcpClInformationTable.setStatus("current")
_RlDhcpClInformationEntry_Object = MibTableRow
rlDhcpClInformationEntry = _RlDhcpClInformationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1)
)
rlDhcpClInformationEntry.setIndexNames(
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpClInformationIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClInformationEntry.setStatus("current")
_RlDhcpClInformationIfIndex_Type = InterfaceIndex
_RlDhcpClInformationIfIndex_Object = MibTableColumn
rlDhcpClInformationIfIndex = _RlDhcpClInformationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 1),
    _RlDhcpClInformationIfIndex_Type()
)
rlDhcpClInformationIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationIfIndex.setStatus("current")
_RlDhcpClInformationIpAddress_Type = IpAddress
_RlDhcpClInformationIpAddress_Object = MibTableColumn
rlDhcpClInformationIpAddress = _RlDhcpClInformationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 2),
    _RlDhcpClInformationIpAddress_Type()
)
rlDhcpClInformationIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationIpAddress.setStatus("current")
_RlDhcpClInformationIpMask_Type = IpAddress
_RlDhcpClInformationIpMask_Object = MibTableColumn
rlDhcpClInformationIpMask = _RlDhcpClInformationIpMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 3),
    _RlDhcpClInformationIpMask_Type()
)
rlDhcpClInformationIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationIpMask.setStatus("current")
_RlDhcpClInformationT1_Type = Unsigned32
_RlDhcpClInformationT1_Object = MibTableColumn
rlDhcpClInformationT1 = _RlDhcpClInformationT1_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 4),
    _RlDhcpClInformationT1_Type()
)
rlDhcpClInformationT1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationT1.setStatus("current")
_RlDhcpClInformationT2_Type = Unsigned32
_RlDhcpClInformationT2_Object = MibTableColumn
rlDhcpClInformationT2 = _RlDhcpClInformationT2_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 5),
    _RlDhcpClInformationT2_Type()
)
rlDhcpClInformationT2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationT2.setStatus("current")
_RlDhcpClInformationDefaultGateway_Type = IpAddress
_RlDhcpClInformationDefaultGateway_Object = MibTableColumn
rlDhcpClInformationDefaultGateway = _RlDhcpClInformationDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 6),
    _RlDhcpClInformationDefaultGateway_Type()
)
rlDhcpClInformationDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationDefaultGateway.setStatus("current")


class _RlDhcpClInformationHostName_Type(SnmpAdminString):
    """Custom type rlDhcpClInformationHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpClInformationHostName_Type.__name__ = "SnmpAdminString"
_RlDhcpClInformationHostName_Object = MibTableColumn
rlDhcpClInformationHostName = _RlDhcpClInformationHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 7),
    _RlDhcpClInformationHostName_Type()
)
rlDhcpClInformationHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationHostName.setStatus("current")


class _RlDhcpClInformationDomainName_Type(DisplayString):
    """Custom type rlDhcpClInformationDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpClInformationDomainName_Type.__name__ = "DisplayString"
_RlDhcpClInformationDomainName_Object = MibTableColumn
rlDhcpClInformationDomainName = _RlDhcpClInformationDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 8),
    _RlDhcpClInformationDomainName_Type()
)
rlDhcpClInformationDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationDomainName.setStatus("current")


class _RlDhcpClInformationTftpServerName_Type(DisplayString):
    """Custom type rlDhcpClInformationTftpServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpClInformationTftpServerName_Type.__name__ = "DisplayString"
_RlDhcpClInformationTftpServerName_Object = MibTableColumn
rlDhcpClInformationTftpServerName = _RlDhcpClInformationTftpServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 9),
    _RlDhcpClInformationTftpServerName_Type()
)
rlDhcpClInformationTftpServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationTftpServerName.setStatus("current")


class _RlDhcpClInformationTftpFileName_Type(DisplayString):
    """Custom type rlDhcpClInformationTftpFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpClInformationTftpFileName_Type.__name__ = "DisplayString"
_RlDhcpClInformationTftpFileName_Object = MibTableColumn
rlDhcpClInformationTftpFileName = _RlDhcpClInformationTftpFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 10),
    _RlDhcpClInformationTftpFileName_Type()
)
rlDhcpClInformationTftpFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationTftpFileName.setStatus("current")


class _RlDhcpClInformationTimeZone_Type(DisplayString):
    """Custom type rlDhcpClInformationTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlDhcpClInformationTimeZone_Type.__name__ = "DisplayString"
_RlDhcpClInformationTimeZone_Object = MibTableColumn
rlDhcpClInformationTimeZone = _RlDhcpClInformationTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 11),
    _RlDhcpClInformationTimeZone_Type()
)
rlDhcpClInformationTimeZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationTimeZone.setStatus("current")


class _RlDhcpClInformationTftpImageName_Type(DisplayString):
    """Custom type rlDhcpClInformationTftpImageName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpClInformationTftpImageName_Type.__name__ = "DisplayString"
_RlDhcpClInformationTftpImageName_Object = MibTableColumn
rlDhcpClInformationTftpImageName = _RlDhcpClInformationTftpImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 12),
    _RlDhcpClInformationTftpImageName_Type()
)
rlDhcpClInformationTftpImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationTftpImageName.setStatus("current")


class _RlDhcpClInformationPnpData_Type(DisplayString):
    """Custom type rlDhcpClInformationPnpData based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_RlDhcpClInformationPnpData_Type.__name__ = "DisplayString"
_RlDhcpClInformationPnpData_Object = MibTableColumn
rlDhcpClInformationPnpData = _RlDhcpClInformationPnpData_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 27, 1, 13),
    _RlDhcpClInformationPnpData_Type()
)
rlDhcpClInformationPnpData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationPnpData.setStatus("current")
_RlDhcpClInformationDnsServerListTable_Object = MibTable
rlDhcpClInformationDnsServerListTable = _RlDhcpClInformationDnsServerListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 28)
)
if mibBuilder.loadTexts:
    rlDhcpClInformationDnsServerListTable.setStatus("current")
_RlDhcpClInformationDnsServerListEntry_Object = MibTableRow
rlDhcpClInformationDnsServerListEntry = _RlDhcpClInformationDnsServerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 28, 1)
)
rlDhcpClInformationDnsServerListEntry.setIndexNames(
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpClInformationDnsServerListIfIndex"),
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpClInformationDnsServerListPriority"),
)
if mibBuilder.loadTexts:
    rlDhcpClInformationDnsServerListEntry.setStatus("current")
_RlDhcpClInformationDnsServerListIfIndex_Type = InterfaceIndex
_RlDhcpClInformationDnsServerListIfIndex_Object = MibTableColumn
rlDhcpClInformationDnsServerListIfIndex = _RlDhcpClInformationDnsServerListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 28, 1, 1),
    _RlDhcpClInformationDnsServerListIfIndex_Type()
)
rlDhcpClInformationDnsServerListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpClInformationDnsServerListIfIndex.setStatus("current")
_RlDhcpClInformationDnsServerListPriority_Type = Integer32
_RlDhcpClInformationDnsServerListPriority_Object = MibTableColumn
rlDhcpClInformationDnsServerListPriority = _RlDhcpClInformationDnsServerListPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 28, 1, 2),
    _RlDhcpClInformationDnsServerListPriority_Type()
)
rlDhcpClInformationDnsServerListPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpClInformationDnsServerListPriority.setStatus("current")
_RlDhcpClInformationDnsServerListAddress_Type = IpAddress
_RlDhcpClInformationDnsServerListAddress_Object = MibTableColumn
rlDhcpClInformationDnsServerListAddress = _RlDhcpClInformationDnsServerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 28, 1, 3),
    _RlDhcpClInformationDnsServerListAddress_Type()
)
rlDhcpClInformationDnsServerListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationDnsServerListAddress.setStatus("current")
_RlDhcpClInformationTftpServerListTable_Object = MibTable
rlDhcpClInformationTftpServerListTable = _RlDhcpClInformationTftpServerListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 29)
)
if mibBuilder.loadTexts:
    rlDhcpClInformationTftpServerListTable.setStatus("current")
_RlDhcpClInformationTftpServerListEntry_Object = MibTableRow
rlDhcpClInformationTftpServerListEntry = _RlDhcpClInformationTftpServerListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 29, 1)
)
rlDhcpClInformationTftpServerListEntry.setIndexNames(
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpClInformationTftpServerListIfIndex"),
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpClInformationTftpServerListPriority"),
)
if mibBuilder.loadTexts:
    rlDhcpClInformationTftpServerListEntry.setStatus("current")
_RlDhcpClInformationTftpServerListIfIndex_Type = InterfaceIndex
_RlDhcpClInformationTftpServerListIfIndex_Object = MibTableColumn
rlDhcpClInformationTftpServerListIfIndex = _RlDhcpClInformationTftpServerListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 29, 1, 1),
    _RlDhcpClInformationTftpServerListIfIndex_Type()
)
rlDhcpClInformationTftpServerListIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpClInformationTftpServerListIfIndex.setStatus("current")
_RlDhcpClInformationTftpServerListPriority_Type = Integer32
_RlDhcpClInformationTftpServerListPriority_Object = MibTableColumn
rlDhcpClInformationTftpServerListPriority = _RlDhcpClInformationTftpServerListPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 29, 1, 2),
    _RlDhcpClInformationTftpServerListPriority_Type()
)
rlDhcpClInformationTftpServerListPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlDhcpClInformationTftpServerListPriority.setStatus("current")
_RlDhcpClInformationTftpServerListAddress_Type = IpAddress
_RlDhcpClInformationTftpServerListAddress_Object = MibTableColumn
rlDhcpClInformationTftpServerListAddress = _RlDhcpClInformationTftpServerListAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 29, 1, 3),
    _RlDhcpClInformationTftpServerListAddress_Type()
)
rlDhcpClInformationTftpServerListAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClInformationTftpServerListAddress.setStatus("current")


class _RlDhcpClAutoUpdateProtocol_Type(Integer32):
    """Custom type rlDhcpClAutoUpdateProtocol based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("scp", 2),
          ("auto", 3))
    )


_RlDhcpClAutoUpdateProtocol_Type.__name__ = "Integer32"
_RlDhcpClAutoUpdateProtocol_Object = MibScalar
rlDhcpClAutoUpdateProtocol = _RlDhcpClAutoUpdateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 30),
    _RlDhcpClAutoUpdateProtocol_Type()
)
rlDhcpClAutoUpdateProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoUpdateProtocol.setStatus("current")


class _RlDhcpClAutoUpdateScpFileExtention_Type(DisplayString):
    """Custom type rlDhcpClAutoUpdateScpFileExtention based on DisplayString"""
    defaultValue = OctetString("scp")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpClAutoUpdateScpFileExtention_Type.__name__ = "DisplayString"
_RlDhcpClAutoUpdateScpFileExtention_Object = MibScalar
rlDhcpClAutoUpdateScpFileExtention = _RlDhcpClAutoUpdateScpFileExtention_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 31),
    _RlDhcpClAutoUpdateScpFileExtention_Type()
)
rlDhcpClAutoUpdateScpFileExtention.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpClAutoUpdateScpFileExtention.setStatus("current")
_RlDhcpClEnabledByDefaultRemovedTable_Object = MibTable
rlDhcpClEnabledByDefaultRemovedTable = _RlDhcpClEnabledByDefaultRemovedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 32)
)
if mibBuilder.loadTexts:
    rlDhcpClEnabledByDefaultRemovedTable.setStatus("current")
_RlDhcpClEnabledByDefaultRemovedEntry_Object = MibTableRow
rlDhcpClEnabledByDefaultRemovedEntry = _RlDhcpClEnabledByDefaultRemovedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 32, 1)
)
rlDhcpClEnabledByDefaultRemovedEntry.setIndexNames(
    (0, "CISCOSB-DHCPCL-MIB", "rlDhcpClEnabledByDefaultRemovedIfIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpClEnabledByDefaultRemovedEntry.setStatus("current")
_RlDhcpClEnabledByDefaultRemovedIfIndex_Type = InterfaceIndex
_RlDhcpClEnabledByDefaultRemovedIfIndex_Object = MibTableColumn
rlDhcpClEnabledByDefaultRemovedIfIndex = _RlDhcpClEnabledByDefaultRemovedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 32, 1, 1),
    _RlDhcpClEnabledByDefaultRemovedIfIndex_Type()
)
rlDhcpClEnabledByDefaultRemovedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpClEnabledByDefaultRemovedIfIndex.setStatus("current")
_RlDhcpClEnabledByDefaultRemovedStatus_Type = RowStatus
_RlDhcpClEnabledByDefaultRemovedStatus_Object = MibTableColumn
rlDhcpClEnabledByDefaultRemovedStatus = _RlDhcpClEnabledByDefaultRemovedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 76, 32, 1, 2),
    _RlDhcpClEnabledByDefaultRemovedStatus_Type()
)
rlDhcpClEnabledByDefaultRemovedStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rlDhcpClEnabledByDefaultRemovedStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DHCPCL-MIB",
    **{"rlDhcpCl": rlDhcpCl,
       "rlDhcpClActionTable": rlDhcpClActionTable,
       "rlDhcpClActionEntry": rlDhcpClActionEntry,
       "rlDhcpClActionIfIndex": rlDhcpClActionIfIndex,
       "rlDhcpClActionStatus": rlDhcpClActionStatus,
       "rlDhcpClActionHostName": rlDhcpClActionHostName,
       "rlDhcpApprovalEnabled": rlDhcpApprovalEnabled,
       "rlDhcpApprovalWaitingTable": rlDhcpApprovalWaitingTable,
       "rlDhcpApprovalWaitingEntry": rlDhcpApprovalWaitingEntry,
       "rlDhcpApprovalWaitingIfIndex": rlDhcpApprovalWaitingIfIndex,
       "rlDhcpApprovalWaitingAddress": rlDhcpApprovalWaitingAddress,
       "rlDhcpApprovalWaitingMask": rlDhcpApprovalWaitingMask,
       "rlDhcpApprovalWaitingGateway": rlDhcpApprovalWaitingGateway,
       "rlDhcpApprovalActionTable": rlDhcpApprovalActionTable,
       "rlDhcpApprovalActionEntry": rlDhcpApprovalActionEntry,
       "rlDhcpApprovalActionIfIndex": rlDhcpApprovalActionIfIndex,
       "rlDhcpApprovalActionAddress": rlDhcpApprovalActionAddress,
       "rlDhcpApprovalActionMask": rlDhcpApprovalActionMask,
       "rlDhcpApprovalActionApprove": rlDhcpApprovalActionApprove,
       "rlDhcpClCommandTable": rlDhcpClCommandTable,
       "rlDhcpClCommandEntry": rlDhcpClCommandEntry,
       "rlDhcpClCommandAction": rlDhcpClCommandAction,
       "rlDhcpClConfigurationFileName": rlDhcpClConfigurationFileName,
       "rlDhcpClOption67Enable": rlDhcpClOption67Enable,
       "rlDhcpClManualTftpServerAddress": rlDhcpClManualTftpServerAddress,
       "rlDhcpClSelectedTftpServerAddress": rlDhcpClSelectedTftpServerAddress,
       "rlDhcpClSelectedTftpServerAddressOrigin": rlDhcpClSelectedTftpServerAddressOrigin,
       "rlDhcpClManualConfigurationFileName": rlDhcpClManualConfigurationFileName,
       "rlDhcpClSelectedConfigurationFileName": rlDhcpClSelectedConfigurationFileName,
       "rlDhcpClSelectedConfigurationFileNameOrigin": rlDhcpClSelectedConfigurationFileNameOrigin,
       "rlDhcpClEnabledByDefaultRemovedIfindex": rlDhcpClEnabledByDefaultRemovedIfindex,
       "rlDhcpClAutoUpdateEnabled": rlDhcpClAutoUpdateEnabled,
       "rlDhcpClAutoUpdateStatus": rlDhcpClAutoUpdateStatus,
       "rlDhcpClAutoConfigForce": rlDhcpClAutoConfigForce,
       "rlDhcpClAutoConfigAutoSave": rlDhcpClAutoConfigAutoSave,
       "rlDhcpClAutoConfigStatus": rlDhcpClAutoConfigStatus,
       "rlDhcpClAutoConfigProtocol": rlDhcpClAutoConfigProtocol,
       "rlDhcpClAutoConfigScpFileExtention": rlDhcpClAutoConfigScpFileExtention,
       "rlDhcpClSelectedTftpServerInetAddressType": rlDhcpClSelectedTftpServerInetAddressType,
       "rlDhcpClSelectedTftpServerInetAddress": rlDhcpClSelectedTftpServerInetAddress,
       "rlDhcpClManualAutoConfigDataTable": rlDhcpClManualAutoConfigDataTable,
       "rlDhcpClManualAutoConfigDataEntry": rlDhcpClManualAutoConfigDataEntry,
       "rlDhcpClManualAutoConfigDataIndex": rlDhcpClManualAutoConfigDataIndex,
       "rlDhcpClManualServerInetAddressType": rlDhcpClManualServerInetAddressType,
       "rlDhcpClManualServerInetAddress": rlDhcpClManualServerInetAddress,
       "rlDhcpClManualImageIndirectFileName": rlDhcpClManualImageIndirectFileName,
       "rlDhcpClInformationTable": rlDhcpClInformationTable,
       "rlDhcpClInformationEntry": rlDhcpClInformationEntry,
       "rlDhcpClInformationIfIndex": rlDhcpClInformationIfIndex,
       "rlDhcpClInformationIpAddress": rlDhcpClInformationIpAddress,
       "rlDhcpClInformationIpMask": rlDhcpClInformationIpMask,
       "rlDhcpClInformationT1": rlDhcpClInformationT1,
       "rlDhcpClInformationT2": rlDhcpClInformationT2,
       "rlDhcpClInformationDefaultGateway": rlDhcpClInformationDefaultGateway,
       "rlDhcpClInformationHostName": rlDhcpClInformationHostName,
       "rlDhcpClInformationDomainName": rlDhcpClInformationDomainName,
       "rlDhcpClInformationTftpServerName": rlDhcpClInformationTftpServerName,
       "rlDhcpClInformationTftpFileName": rlDhcpClInformationTftpFileName,
       "rlDhcpClInformationTimeZone": rlDhcpClInformationTimeZone,
       "rlDhcpClInformationTftpImageName": rlDhcpClInformationTftpImageName,
       "rlDhcpClInformationPnpData": rlDhcpClInformationPnpData,
       "rlDhcpClInformationDnsServerListTable": rlDhcpClInformationDnsServerListTable,
       "rlDhcpClInformationDnsServerListEntry": rlDhcpClInformationDnsServerListEntry,
       "rlDhcpClInformationDnsServerListIfIndex": rlDhcpClInformationDnsServerListIfIndex,
       "rlDhcpClInformationDnsServerListPriority": rlDhcpClInformationDnsServerListPriority,
       "rlDhcpClInformationDnsServerListAddress": rlDhcpClInformationDnsServerListAddress,
       "rlDhcpClInformationTftpServerListTable": rlDhcpClInformationTftpServerListTable,
       "rlDhcpClInformationTftpServerListEntry": rlDhcpClInformationTftpServerListEntry,
       "rlDhcpClInformationTftpServerListIfIndex": rlDhcpClInformationTftpServerListIfIndex,
       "rlDhcpClInformationTftpServerListPriority": rlDhcpClInformationTftpServerListPriority,
       "rlDhcpClInformationTftpServerListAddress": rlDhcpClInformationTftpServerListAddress,
       "rlDhcpClAutoUpdateProtocol": rlDhcpClAutoUpdateProtocol,
       "rlDhcpClAutoUpdateScpFileExtention": rlDhcpClAutoUpdateScpFileExtention,
       "rlDhcpClEnabledByDefaultRemovedTable": rlDhcpClEnabledByDefaultRemovedTable,
       "rlDhcpClEnabledByDefaultRemovedEntry": rlDhcpClEnabledByDefaultRemovedEntry,
       "rlDhcpClEnabledByDefaultRemovedIfIndex": rlDhcpClEnabledByDefaultRemovedIfIndex,
       "rlDhcpClEnabledByDefaultRemovedStatus": rlDhcpClEnabledByDefaultRemovedStatus}
)
