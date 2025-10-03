# SNMP MIB module (ZYXEL-AS-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\zyxel\ZYXEL-AS-ATM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:53 2025
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

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(accessSwitchCommonATM,) = mibBuilder.importSymbols(
    "ZYXEL-MIB",
    "accessSwitchCommonATM")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsMaxNumOfChannels_Type = Integer32
_AsMaxNumOfChannels_Object = MibScalar
asMaxNumOfChannels = _AsMaxNumOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 1),
    _AsMaxNumOfChannels_Type()
)
asMaxNumOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMaxNumOfChannels.setStatus("mandatory")
_AsChannelTable_Object = MibTable
asChannelTable = _AsChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 2)
)
if mibBuilder.loadTexts:
    asChannelTable.setStatus("mandatory")
_AsChannelEntry_Object = MibTableRow
asChannelEntry = _AsChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 2, 1)
)
asChannelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-AS-ATM-MIB", "asChannelVpi"),
    (0, "ZYXEL-AS-ATM-MIB", "asChannelVci"),
)
if mibBuilder.loadTexts:
    asChannelEntry.setStatus("mandatory")


class _AsChannelVpi_Type(Integer32):
    """Custom type asChannelVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsChannelVpi_Type.__name__ = "Integer32"
_AsChannelVpi_Object = MibTableColumn
asChannelVpi = _AsChannelVpi_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 2, 1, 1),
    _AsChannelVpi_Type()
)
asChannelVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asChannelVpi.setStatus("mandatory")


class _AsChannelVci_Type(Integer32):
    """Custom type asChannelVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AsChannelVci_Type.__name__ = "Integer32"
_AsChannelVci_Object = MibTableColumn
asChannelVci = _AsChannelVci_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 2, 1, 2),
    _AsChannelVci_Type()
)
asChannelVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asChannelVci.setStatus("mandatory")
_AsChannelPvid_Type = VlanIndex
_AsChannelPvid_Object = MibTableColumn
asChannelPvid = _AsChannelPvid_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 2, 1, 3),
    _AsChannelPvid_Type()
)
asChannelPvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelPvid.setStatus("mandatory")


class _AsChannelPriority_Type(Integer32):
    """Custom type asChannelPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AsChannelPriority_Type.__name__ = "Integer32"
_AsChannelPriority_Object = MibTableColumn
asChannelPriority = _AsChannelPriority_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 2, 1, 5),
    _AsChannelPriority_Type()
)
asChannelPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelPriority.setStatus("mandatory")


class _AsChannelProfile_Type(DisplayString):
    """Custom type asChannelProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AsChannelProfile_Type.__name__ = "DisplayString"
_AsChannelProfile_Object = MibTableColumn
asChannelProfile = _AsChannelProfile_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 2, 1, 6),
    _AsChannelProfile_Type()
)
asChannelProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfile.setStatus("mandatory")
_AsChannelRowStatus_Type = RowStatus
_AsChannelRowStatus_Object = MibTableColumn
asChannelRowStatus = _AsChannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 2, 1, 7),
    _AsChannelRowStatus_Type()
)
asChannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelRowStatus.setStatus("mandatory")
_AsMaxNumOfChannelProfiles_Type = Integer32
_AsMaxNumOfChannelProfiles_Object = MibScalar
asMaxNumOfChannelProfiles = _AsMaxNumOfChannelProfiles_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 3),
    _AsMaxNumOfChannelProfiles_Type()
)
asMaxNumOfChannelProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMaxNumOfChannelProfiles.setStatus("mandatory")
_AsChannelProfileTable_Object = MibTable
asChannelProfileTable = _AsChannelProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6)
)
if mibBuilder.loadTexts:
    asChannelProfileTable.setStatus("mandatory")
_AsChannelProfileEntry_Object = MibTableRow
asChannelProfileEntry = _AsChannelProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1)
)
asChannelProfileEntry.setIndexNames(
    (1, "ZYXEL-AS-ATM-MIB", "asChannelProfileName"),
)
if mibBuilder.loadTexts:
    asChannelProfileEntry.setStatus("mandatory")


class _AsChannelProfileName_Type(DisplayString):
    """Custom type asChannelProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AsChannelProfileName_Type.__name__ = "DisplayString"
_AsChannelProfileName_Object = MibTableColumn
asChannelProfileName = _AsChannelProfileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 1),
    _AsChannelProfileName_Type()
)
asChannelProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asChannelProfileName.setStatus("mandatory")


class _AsChannelProfileEncap_Type(Integer32):
    """Custom type asChannelProfileEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("vc", 2))
    )


_AsChannelProfileEncap_Type.__name__ = "Integer32"
_AsChannelProfileEncap_Object = MibTableColumn
asChannelProfileEncap = _AsChannelProfileEncap_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 2),
    _AsChannelProfileEncap_Type()
)
asChannelProfileEncap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfileEncap.setStatus("mandatory")


class _AsChannelProfileAAL_Type(Integer32):
    """Custom type asChannelProfileAAL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AsChannelProfileAAL_Type.__name__ = "Integer32"
_AsChannelProfileAAL_Object = MibTableColumn
asChannelProfileAAL = _AsChannelProfileAAL_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 3),
    _AsChannelProfileAAL_Type()
)
asChannelProfileAAL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfileAAL.setStatus("mandatory")


class _AsChannelProfileClass_Type(Integer32):
    """Custom type asChannelProfileClass based on Integer32"""
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
        *(("cbr", 1),
          ("rt-vbr", 2),
          ("nrt-vbr", 3),
          ("ubr", 4),
          ("abr", 5))
    )


_AsChannelProfileClass_Type.__name__ = "Integer32"
_AsChannelProfileClass_Object = MibTableColumn
asChannelProfileClass = _AsChannelProfileClass_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 4),
    _AsChannelProfileClass_Type()
)
asChannelProfileClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfileClass.setStatus("mandatory")
_AsChannelProfilePcr_Type = Unsigned32
_AsChannelProfilePcr_Object = MibTableColumn
asChannelProfilePcr = _AsChannelProfilePcr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 5),
    _AsChannelProfilePcr_Type()
)
asChannelProfilePcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfilePcr.setStatus("mandatory")


class _AsChannelProfileCdvt_Type(Integer32):
    """Custom type asChannelProfileCdvt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsChannelProfileCdvt_Type.__name__ = "Integer32"
_AsChannelProfileCdvt_Object = MibTableColumn
asChannelProfileCdvt = _AsChannelProfileCdvt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 6),
    _AsChannelProfileCdvt_Type()
)
asChannelProfileCdvt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfileCdvt.setStatus("mandatory")
_AsChannelProfileScrMcr_Type = Unsigned32
_AsChannelProfileScrMcr_Object = MibTableColumn
asChannelProfileScrMcr = _AsChannelProfileScrMcr_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 7),
    _AsChannelProfileScrMcr_Type()
)
asChannelProfileScrMcr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfileScrMcr.setStatus("mandatory")


class _AsChannelProfileBt_Type(Integer32):
    """Custom type asChannelProfileBt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsChannelProfileBt_Type.__name__ = "Integer32"
_AsChannelProfileBt_Object = MibTableColumn
asChannelProfileBt = _AsChannelProfileBt_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 8),
    _AsChannelProfileBt_Type()
)
asChannelProfileBt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfileBt.setStatus("mandatory")
_AsChannelProfileRowStatus_Type = RowStatus
_AsChannelProfileRowStatus_Object = MibTableColumn
asChannelProfileRowStatus = _AsChannelProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 6, 1, 9),
    _AsChannelProfileRowStatus_Type()
)
asChannelProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    asChannelProfileRowStatus.setStatus("mandatory")
_AsChannelStatusTable_Object = MibTable
asChannelStatusTable = _AsChannelStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 7)
)
if mibBuilder.loadTexts:
    asChannelStatusTable.setStatus("mandatory")
_AsChannelStatusEntry_Object = MibTableRow
asChannelStatusEntry = _AsChannelStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 7, 1)
)
asChannelStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ZYXEL-AS-ATM-MIB", "asChannelVpi"),
    (0, "ZYXEL-AS-ATM-MIB", "asChannelVci"),
)
if mibBuilder.loadTexts:
    asChannelStatusEntry.setStatus("mandatory")
_AsChannelTxPackets_Type = Counter32
_AsChannelTxPackets_Object = MibTableColumn
asChannelTxPackets = _AsChannelTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 7, 1, 1),
    _AsChannelTxPackets_Type()
)
asChannelTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asChannelTxPackets.setStatus("mandatory")
_AsChannelRxPackets_Type = Counter32
_AsChannelRxPackets_Object = MibTableColumn
asChannelRxPackets = _AsChannelRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 7, 1, 2),
    _AsChannelRxPackets_Type()
)
asChannelRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asChannelRxPackets.setStatus("mandatory")
_AsChannelTxCells_Type = Counter32
_AsChannelTxCells_Object = MibTableColumn
asChannelTxCells = _AsChannelTxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 7, 1, 3),
    _AsChannelTxCells_Type()
)
asChannelTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asChannelTxCells.setStatus("mandatory")
_AsChannelRxCells_Type = Counter32
_AsChannelRxCells_Object = MibTableColumn
asChannelRxCells = _AsChannelRxCells_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 5, 14, 7, 1, 4),
    _AsChannelRxCells_Type()
)
asChannelRxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asChannelRxCells.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-AS-ATM-MIB",
    **{"asMaxNumOfChannels": asMaxNumOfChannels,
       "asChannelTable": asChannelTable,
       "asChannelEntry": asChannelEntry,
       "asChannelVpi": asChannelVpi,
       "asChannelVci": asChannelVci,
       "asChannelPvid": asChannelPvid,
       "asChannelPriority": asChannelPriority,
       "asChannelProfile": asChannelProfile,
       "asChannelRowStatus": asChannelRowStatus,
       "asMaxNumOfChannelProfiles": asMaxNumOfChannelProfiles,
       "asChannelProfileTable": asChannelProfileTable,
       "asChannelProfileEntry": asChannelProfileEntry,
       "asChannelProfileName": asChannelProfileName,
       "asChannelProfileEncap": asChannelProfileEncap,
       "asChannelProfileAAL": asChannelProfileAAL,
       "asChannelProfileClass": asChannelProfileClass,
       "asChannelProfilePcr": asChannelProfilePcr,
       "asChannelProfileCdvt": asChannelProfileCdvt,
       "asChannelProfileScrMcr": asChannelProfileScrMcr,
       "asChannelProfileBt": asChannelProfileBt,
       "asChannelProfileRowStatus": asChannelProfileRowStatus,
       "asChannelStatusTable": asChannelStatusTable,
       "asChannelStatusEntry": asChannelStatusEntry,
       "asChannelTxPackets": asChannelTxPackets,
       "asChannelRxPackets": asChannelRxPackets,
       "asChannelTxCells": asChannelTxCells,
       "asChannelRxCells": asChannelRxCells}
)
