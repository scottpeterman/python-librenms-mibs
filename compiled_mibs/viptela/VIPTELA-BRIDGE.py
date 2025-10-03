# SNMP MIB module (VIPTELA-BRIDGE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-BRIDGE
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:00 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_bridge = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 10)
)
if mibBuilder.loadTexts:
    viptela_bridge.setRevisions(
        ("2020-07-01 00:00",
         "2020-02-24 00:00",
         "2019-11-15 00:00",
         "2019-08-15 00:00",
         "2018-11-01 00:00",
         "2018-08-20 00:00",
         "2018-06-25 00:00",
         "2018-04-25 00:00",
         "2018-03-15 00:00",
         "2018-01-16 00:00",
         "2017-11-01 00:00",
         "2017-08-01 00:00",
         "2017-05-25 00:00",
         "2017-04-06 00:00",
         "2017-02-15 00:00",
         "2017-02-06 00:00",
         "2016-11-16 00:00",
         "2016-10-25 00:00",
         "2016-10-24 00:00",
         "2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedShort(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


# MIB Managed Objects in the order of their OIDs

_Bridge_ObjectIdentity = ObjectIdentity
bridge = _Bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1)
)
_BridgeTableTable_Object = MibTable
bridgeTableTable = _BridgeTableTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4)
)
if mibBuilder.loadTexts:
    bridgeTableTable.setStatus("current")
_BridgeTableEntry_Object = MibTableRow
bridgeTableEntry = _BridgeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1)
)
bridgeTableEntry.setIndexNames(
    (0, "VIPTELA-BRIDGE", "bridgeTableBridgeId"),
)
if mibBuilder.loadTexts:
    bridgeTableEntry.setStatus("current")


class _BridgeTableBridgeId_Type(Unsigned32):
    """Custom type bridgeTableBridgeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_BridgeTableBridgeId_Type.__name__ = "Unsigned32"
_BridgeTableBridgeId_Object = MibTableColumn
bridgeTableBridgeId = _BridgeTableBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 1),
    _BridgeTableBridgeId_Type()
)
bridgeTableBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeTableBridgeId.setStatus("current")


class _BridgeTableName_Type(String):
    """Custom type bridgeTableName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BridgeTableName_Type.__name__ = "String"
_BridgeTableName_Object = MibTableColumn
bridgeTableName = _BridgeTableName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 2),
    _BridgeTableName_Type()
)
bridgeTableName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableName.setStatus("current")
_BridgeTableVlan_Type = UnsignedShort
_BridgeTableVlan_Object = MibTableColumn
bridgeTableVlan = _BridgeTableVlan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 3),
    _BridgeTableVlan_Type()
)
bridgeTableVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableVlan.setStatus("current")


class _BridgeTableRoutingInterface_Type(String):
    """Custom type bridgeTableRoutingInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BridgeTableRoutingInterface_Type.__name__ = "String"
_BridgeTableRoutingInterface_Object = MibTableColumn
bridgeTableRoutingInterface = _BridgeTableRoutingInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 4),
    _BridgeTableRoutingInterface_Type()
)
bridgeTableRoutingInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableRoutingInterface.setStatus("current")
_BridgeTableMaxMacs_Type = Unsigned32
_BridgeTableMaxMacs_Object = MibTableColumn
bridgeTableMaxMacs = _BridgeTableMaxMacs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 5),
    _BridgeTableMaxMacs_Type()
)
bridgeTableMaxMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableMaxMacs.setStatus("current")
_BridgeTableNumMacs_Type = Unsigned32
_BridgeTableNumMacs_Object = MibTableColumn
bridgeTableNumMacs = _BridgeTableNumMacs_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 6),
    _BridgeTableNumMacs_Type()
)
bridgeTableNumMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableNumMacs.setStatus("current")
_BridgeTableAgeTime_Type = Unsigned32
_BridgeTableAgeTime_Object = MibTableColumn
bridgeTableAgeTime = _BridgeTableAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 7),
    _BridgeTableAgeTime_Type()
)
bridgeTableAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableAgeTime.setStatus("current")
_BridgeTableRxPackets_Type = Counter64
_BridgeTableRxPackets_Object = MibTableColumn
bridgeTableRxPackets = _BridgeTableRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 8),
    _BridgeTableRxPackets_Type()
)
bridgeTableRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableRxPackets.setStatus("current")
_BridgeTableRxOctets_Type = Counter64
_BridgeTableRxOctets_Object = MibTableColumn
bridgeTableRxOctets = _BridgeTableRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 9),
    _BridgeTableRxOctets_Type()
)
bridgeTableRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableRxOctets.setStatus("current")
_BridgeTableTxPackets_Type = Counter64
_BridgeTableTxPackets_Object = MibTableColumn
bridgeTableTxPackets = _BridgeTableTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 10),
    _BridgeTableTxPackets_Type()
)
bridgeTableTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableTxPackets.setStatus("current")
_BridgeTableTxOctets_Type = Counter64
_BridgeTableTxOctets_Object = MibTableColumn
bridgeTableTxOctets = _BridgeTableTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 11),
    _BridgeTableTxOctets_Type()
)
bridgeTableTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableTxOctets.setStatus("current")
_BridgeTableFloodPackets_Type = Counter64
_BridgeTableFloodPackets_Object = MibTableColumn
bridgeTableFloodPackets = _BridgeTableFloodPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 12),
    _BridgeTableFloodPackets_Type()
)
bridgeTableFloodPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableFloodPackets.setStatus("current")
_BridgeTableFloodOctets_Type = Counter64
_BridgeTableFloodOctets_Object = MibTableColumn
bridgeTableFloodOctets = _BridgeTableFloodOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 13),
    _BridgeTableFloodOctets_Type()
)
bridgeTableFloodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableFloodOctets.setStatus("current")
_BridgeTableRxRoutedPackets_Type = Counter64
_BridgeTableRxRoutedPackets_Object = MibTableColumn
bridgeTableRxRoutedPackets = _BridgeTableRxRoutedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 14),
    _BridgeTableRxRoutedPackets_Type()
)
bridgeTableRxRoutedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableRxRoutedPackets.setStatus("current")
_BridgeTableTxRoutedPackets_Type = Counter64
_BridgeTableTxRoutedPackets_Object = MibTableColumn
bridgeTableTxRoutedPackets = _BridgeTableTxRoutedPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 15),
    _BridgeTableTxRoutedPackets_Type()
)
bridgeTableTxRoutedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableTxRoutedPackets.setStatus("current")
_BridgeTableLearn_Type = Unsigned32
_BridgeTableLearn_Object = MibTableColumn
bridgeTableLearn = _BridgeTableLearn_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 16),
    _BridgeTableLearn_Type()
)
bridgeTableLearn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableLearn.setStatus("current")
_BridgeTableAge_Type = Unsigned32
_BridgeTableAge_Object = MibTableColumn
bridgeTableAge = _BridgeTableAge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 17),
    _BridgeTableAge_Type()
)
bridgeTableAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableAge.setStatus("current")
_BridgeTableMove_Type = Unsigned32
_BridgeTableMove_Object = MibTableColumn
bridgeTableMove = _BridgeTableMove_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 4, 1, 18),
    _BridgeTableMove_Type()
)
bridgeTableMove.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeTableMove.setStatus("current")
_BridgeInterfaceTable_Object = MibTable
bridgeInterfaceTable = _BridgeInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5)
)
if mibBuilder.loadTexts:
    bridgeInterfaceTable.setStatus("current")
_BridgeInterfaceEntry_Object = MibTableRow
bridgeInterfaceEntry = _BridgeInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1)
)
bridgeInterfaceEntry.setIndexNames(
    (0, "VIPTELA-BRIDGE", "bridgeInterfaceBridgeId"),
    (1, "VIPTELA-BRIDGE", "bridgeInterfaceIfName"),
)
if mibBuilder.loadTexts:
    bridgeInterfaceEntry.setStatus("current")


class _BridgeInterfaceBridgeId_Type(Unsigned32):
    """Custom type bridgeInterfaceBridgeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_BridgeInterfaceBridgeId_Type.__name__ = "Unsigned32"
_BridgeInterfaceBridgeId_Object = MibTableColumn
bridgeInterfaceBridgeId = _BridgeInterfaceBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 1),
    _BridgeInterfaceBridgeId_Type()
)
bridgeInterfaceBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeInterfaceBridgeId.setStatus("current")


class _BridgeInterfaceIfName_Type(String):
    """Custom type bridgeInterfaceIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BridgeInterfaceIfName_Type.__name__ = "String"
_BridgeInterfaceIfName_Object = MibTableColumn
bridgeInterfaceIfName = _BridgeInterfaceIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 2),
    _BridgeInterfaceIfName_Type()
)
bridgeInterfaceIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeInterfaceIfName.setStatus("current")
_BridgeInterfaceVlan_Type = UnsignedShort
_BridgeInterfaceVlan_Object = MibTableColumn
bridgeInterfaceVlan = _BridgeInterfaceVlan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 3),
    _BridgeInterfaceVlan_Type()
)
bridgeInterfaceVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceVlan.setStatus("current")
_BridgeInterfaceNativeVlan_Type = String
_BridgeInterfaceNativeVlan_Object = MibTableColumn
bridgeInterfaceNativeVlan = _BridgeInterfaceNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 4),
    _BridgeInterfaceNativeVlan_Type()
)
bridgeInterfaceNativeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceNativeVlan.setStatus("current")


class _BridgeInterfaceAdminStatus_Type(String):
    """Custom type bridgeInterfaceAdminStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_BridgeInterfaceAdminStatus_Type.__name__ = "String"
_BridgeInterfaceAdminStatus_Object = MibTableColumn
bridgeInterfaceAdminStatus = _BridgeInterfaceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 5),
    _BridgeInterfaceAdminStatus_Type()
)
bridgeInterfaceAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceAdminStatus.setStatus("current")


class _BridgeInterfaceOperStatus_Type(String):
    """Custom type bridgeInterfaceOperStatus based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_BridgeInterfaceOperStatus_Type.__name__ = "String"
_BridgeInterfaceOperStatus_Object = MibTableColumn
bridgeInterfaceOperStatus = _BridgeInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 6),
    _BridgeInterfaceOperStatus_Type()
)
bridgeInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceOperStatus.setStatus("current")


class _BridgeInterfaceEncapType_Type(Integer32):
    """Custom type bridgeInterfaceEncapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("vlan", 1),
          ("ppp", 2))
    )


_BridgeInterfaceEncapType_Type.__name__ = "Integer32"
_BridgeInterfaceEncapType_Object = MibTableColumn
bridgeInterfaceEncapType = _BridgeInterfaceEncapType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 7),
    _BridgeInterfaceEncapType_Type()
)
bridgeInterfaceEncapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceEncapType.setStatus("current")
_BridgeInterfaceIfindex_Type = Unsigned32
_BridgeInterfaceIfindex_Object = MibTableColumn
bridgeInterfaceIfindex = _BridgeInterfaceIfindex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 8),
    _BridgeInterfaceIfindex_Type()
)
bridgeInterfaceIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceIfindex.setStatus("current")
_BridgeInterfaceMtu_Type = Unsigned32
_BridgeInterfaceMtu_Object = MibTableColumn
bridgeInterfaceMtu = _BridgeInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 9),
    _BridgeInterfaceMtu_Type()
)
bridgeInterfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceMtu.setStatus("current")
_BridgeInterfaceRxPackets_Type = Counter64
_BridgeInterfaceRxPackets_Object = MibTableColumn
bridgeInterfaceRxPackets = _BridgeInterfaceRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 10),
    _BridgeInterfaceRxPackets_Type()
)
bridgeInterfaceRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPackets.setStatus("current")
_BridgeInterfaceRxOctets_Type = Counter64
_BridgeInterfaceRxOctets_Object = MibTableColumn
bridgeInterfaceRxOctets = _BridgeInterfaceRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 11),
    _BridgeInterfaceRxOctets_Type()
)
bridgeInterfaceRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxOctets.setStatus("current")
_BridgeInterfaceTxPackets_Type = Counter64
_BridgeInterfaceTxPackets_Object = MibTableColumn
bridgeInterfaceTxPackets = _BridgeInterfaceTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 12),
    _BridgeInterfaceTxPackets_Type()
)
bridgeInterfaceTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPackets.setStatus("current")
_BridgeInterfaceTxOctets_Type = Counter64
_BridgeInterfaceTxOctets_Object = MibTableColumn
bridgeInterfaceTxOctets = _BridgeInterfaceTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 13),
    _BridgeInterfaceTxOctets_Type()
)
bridgeInterfaceTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxOctets.setStatus("current")
_BridgeInterfaceRxErrors_Type = Counter64
_BridgeInterfaceRxErrors_Object = MibTableColumn
bridgeInterfaceRxErrors = _BridgeInterfaceRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 14),
    _BridgeInterfaceRxErrors_Type()
)
bridgeInterfaceRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxErrors.setStatus("current")
_BridgeInterfaceRxDrops_Type = Counter64
_BridgeInterfaceRxDrops_Object = MibTableColumn
bridgeInterfaceRxDrops = _BridgeInterfaceRxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 15),
    _BridgeInterfaceRxDrops_Type()
)
bridgeInterfaceRxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxDrops.setStatus("current")
_BridgeInterfaceTxErrors_Type = Counter64
_BridgeInterfaceTxErrors_Object = MibTableColumn
bridgeInterfaceTxErrors = _BridgeInterfaceTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 16),
    _BridgeInterfaceTxErrors_Type()
)
bridgeInterfaceTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxErrors.setStatus("current")
_BridgeInterfaceTxDrops_Type = Counter64
_BridgeInterfaceTxDrops_Object = MibTableColumn
bridgeInterfaceTxDrops = _BridgeInterfaceTxDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 17),
    _BridgeInterfaceTxDrops_Type()
)
bridgeInterfaceTxDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxDrops.setStatus("current")
_BridgeInterfaceRxPps_Type = Counter64
_BridgeInterfaceRxPps_Object = MibTableColumn
bridgeInterfaceRxPps = _BridgeInterfaceRxPps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 18),
    _BridgeInterfaceRxPps_Type()
)
bridgeInterfaceRxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPps.setStatus("current")
_BridgeInterfaceRxKbps_Type = Counter64
_BridgeInterfaceRxKbps_Object = MibTableColumn
bridgeInterfaceRxKbps = _BridgeInterfaceRxKbps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 19),
    _BridgeInterfaceRxKbps_Type()
)
bridgeInterfaceRxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxKbps.setStatus("current")
_BridgeInterfaceTxPps_Type = Counter64
_BridgeInterfaceTxPps_Object = MibTableColumn
bridgeInterfaceTxPps = _BridgeInterfaceTxPps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 20),
    _BridgeInterfaceTxPps_Type()
)
bridgeInterfaceTxPps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPps.setStatus("current")
_BridgeInterfaceTxKbps_Type = Counter64
_BridgeInterfaceTxKbps_Object = MibTableColumn
bridgeInterfaceTxKbps = _BridgeInterfaceTxKbps_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 21),
    _BridgeInterfaceTxKbps_Type()
)
bridgeInterfaceTxKbps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxKbps.setStatus("current")
_BridgeInterfaceRxArpRequests_Type = Counter64
_BridgeInterfaceRxArpRequests_Object = MibTableColumn
bridgeInterfaceRxArpRequests = _BridgeInterfaceRxArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 22),
    _BridgeInterfaceRxArpRequests_Type()
)
bridgeInterfaceRxArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxArpRequests.setStatus("current")
_BridgeInterfaceTxArpReplies_Type = Counter64
_BridgeInterfaceTxArpReplies_Object = MibTableColumn
bridgeInterfaceTxArpReplies = _BridgeInterfaceTxArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 23),
    _BridgeInterfaceTxArpReplies_Type()
)
bridgeInterfaceTxArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxArpReplies.setStatus("current")
_BridgeInterfaceTxArpRequests_Type = Counter64
_BridgeInterfaceTxArpRequests_Object = MibTableColumn
bridgeInterfaceTxArpRequests = _BridgeInterfaceTxArpRequests_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 24),
    _BridgeInterfaceTxArpRequests_Type()
)
bridgeInterfaceTxArpRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxArpRequests.setStatus("current")
_BridgeInterfaceRxArpReplies_Type = Counter64
_BridgeInterfaceRxArpReplies_Object = MibTableColumn
bridgeInterfaceRxArpReplies = _BridgeInterfaceRxArpReplies_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 25),
    _BridgeInterfaceRxArpReplies_Type()
)
bridgeInterfaceRxArpReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxArpReplies.setStatus("current")
_BridgeInterfaceArpAddFails_Type = Counter64
_BridgeInterfaceArpAddFails_Object = MibTableColumn
bridgeInterfaceArpAddFails = _BridgeInterfaceArpAddFails_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 26),
    _BridgeInterfaceArpAddFails_Type()
)
bridgeInterfaceArpAddFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceArpAddFails.setStatus("current")
_BridgeInterfaceRxArpReplyDrops_Type = Counter64
_BridgeInterfaceRxArpReplyDrops_Object = MibTableColumn
bridgeInterfaceRxArpReplyDrops = _BridgeInterfaceRxArpReplyDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 27),
    _BridgeInterfaceRxArpReplyDrops_Type()
)
bridgeInterfaceRxArpReplyDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxArpReplyDrops.setStatus("current")
_BridgeInterfaceRxArpRateLimitDrops_Type = Counter64
_BridgeInterfaceRxArpRateLimitDrops_Object = MibTableColumn
bridgeInterfaceRxArpRateLimitDrops = _BridgeInterfaceRxArpRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 28),
    _BridgeInterfaceRxArpRateLimitDrops_Type()
)
bridgeInterfaceRxArpRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxArpRateLimitDrops.setStatus("current")
_BridgeInterfaceTxArpRateLimitDrops_Type = Counter64
_BridgeInterfaceTxArpRateLimitDrops_Object = MibTableColumn
bridgeInterfaceTxArpRateLimitDrops = _BridgeInterfaceTxArpRateLimitDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 29),
    _BridgeInterfaceTxArpRateLimitDrops_Type()
)
bridgeInterfaceTxArpRateLimitDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxArpRateLimitDrops.setStatus("current")
_BridgeInterfaceRxArpNonLocalDrops_Type = Counter64
_BridgeInterfaceRxArpNonLocalDrops_Object = MibTableColumn
bridgeInterfaceRxArpNonLocalDrops = _BridgeInterfaceRxArpNonLocalDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 30),
    _BridgeInterfaceRxArpNonLocalDrops_Type()
)
bridgeInterfaceRxArpNonLocalDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxArpNonLocalDrops.setStatus("current")
_BridgeInterfaceTxArpRequestFail_Type = Counter64
_BridgeInterfaceTxArpRequestFail_Object = MibTableColumn
bridgeInterfaceTxArpRequestFail = _BridgeInterfaceTxArpRequestFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 31),
    _BridgeInterfaceTxArpRequestFail_Type()
)
bridgeInterfaceTxArpRequestFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxArpRequestFail.setStatus("current")
_BridgeInterfaceTxNoArpDrops_Type = Counter64
_BridgeInterfaceTxNoArpDrops_Object = MibTableColumn
bridgeInterfaceTxNoArpDrops = _BridgeInterfaceTxNoArpDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 32),
    _BridgeInterfaceTxNoArpDrops_Type()
)
bridgeInterfaceTxNoArpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxNoArpDrops.setStatus("current")
_BridgeInterfaceRxIpTtlExpired_Type = Counter64
_BridgeInterfaceRxIpTtlExpired_Object = MibTableColumn
bridgeInterfaceRxIpTtlExpired = _BridgeInterfaceRxIpTtlExpired_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 33),
    _BridgeInterfaceRxIpTtlExpired_Type()
)
bridgeInterfaceRxIpTtlExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxIpTtlExpired.setStatus("current")
_BridgeInterfaceRxIpErrors_Type = Counter64
_BridgeInterfaceRxIpErrors_Object = MibTableColumn
bridgeInterfaceRxIpErrors = _BridgeInterfaceRxIpErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 34),
    _BridgeInterfaceRxIpErrors_Type()
)
bridgeInterfaceRxIpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxIpErrors.setStatus("current")
_BridgeInterfaceInterfaceDisabled_Type = Counter64
_BridgeInterfaceInterfaceDisabled_Object = MibTableColumn
bridgeInterfaceInterfaceDisabled = _BridgeInterfaceInterfaceDisabled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 35),
    _BridgeInterfaceInterfaceDisabled_Type()
)
bridgeInterfaceInterfaceDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceInterfaceDisabled.setStatus("current")
_BridgeInterfaceRxPolicerDrops_Type = Counter64
_BridgeInterfaceRxPolicerDrops_Object = MibTableColumn
bridgeInterfaceRxPolicerDrops = _BridgeInterfaceRxPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 36),
    _BridgeInterfaceRxPolicerDrops_Type()
)
bridgeInterfaceRxPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPolicerDrops.setStatus("current")
_BridgeInterfaceRxNonIpDrops_Type = Counter64
_BridgeInterfaceRxNonIpDrops_Object = MibTableColumn
bridgeInterfaceRxNonIpDrops = _BridgeInterfaceRxNonIpDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 37),
    _BridgeInterfaceRxNonIpDrops_Type()
)
bridgeInterfaceRxNonIpDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxNonIpDrops.setStatus("current")
_BridgeInterfaceFilterDrops_Type = Counter64
_BridgeInterfaceFilterDrops_Object = MibTableColumn
bridgeInterfaceFilterDrops = _BridgeInterfaceFilterDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 38),
    _BridgeInterfaceFilterDrops_Type()
)
bridgeInterfaceFilterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceFilterDrops.setStatus("current")
_BridgeInterfaceMirrorDrops_Type = Counter64
_BridgeInterfaceMirrorDrops_Object = MibTableColumn
bridgeInterfaceMirrorDrops = _BridgeInterfaceMirrorDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 39),
    _BridgeInterfaceMirrorDrops_Type()
)
bridgeInterfaceMirrorDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceMirrorDrops.setStatus("current")
_BridgeInterfaceCpuPolicerDrops_Type = Counter64
_BridgeInterfaceCpuPolicerDrops_Object = MibTableColumn
bridgeInterfaceCpuPolicerDrops = _BridgeInterfaceCpuPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 40),
    _BridgeInterfaceCpuPolicerDrops_Type()
)
bridgeInterfaceCpuPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceCpuPolicerDrops.setStatus("current")
_BridgeInterfaceTxIcmpPolicerDrops_Type = Counter64
_BridgeInterfaceTxIcmpPolicerDrops_Object = MibTableColumn
bridgeInterfaceTxIcmpPolicerDrops = _BridgeInterfaceTxIcmpPolicerDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 41),
    _BridgeInterfaceTxIcmpPolicerDrops_Type()
)
bridgeInterfaceTxIcmpPolicerDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxIcmpPolicerDrops.setStatus("current")
_BridgeInterfaceTxIcmpMirroredDrops_Type = Counter64
_BridgeInterfaceTxIcmpMirroredDrops_Object = MibTableColumn
bridgeInterfaceTxIcmpMirroredDrops = _BridgeInterfaceTxIcmpMirroredDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 42),
    _BridgeInterfaceTxIcmpMirroredDrops_Type()
)
bridgeInterfaceTxIcmpMirroredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxIcmpMirroredDrops.setStatus("current")
_BridgeInterfaceSplitHorizonDrops_Type = Counter64
_BridgeInterfaceSplitHorizonDrops_Object = MibTableColumn
bridgeInterfaceSplitHorizonDrops = _BridgeInterfaceSplitHorizonDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 43),
    _BridgeInterfaceSplitHorizonDrops_Type()
)
bridgeInterfaceSplitHorizonDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceSplitHorizonDrops.setStatus("current")
_BridgeInterfaceRouteLookupFail_Type = Counter64
_BridgeInterfaceRouteLookupFail_Object = MibTableColumn
bridgeInterfaceRouteLookupFail = _BridgeInterfaceRouteLookupFail_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 44),
    _BridgeInterfaceRouteLookupFail_Type()
)
bridgeInterfaceRouteLookupFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRouteLookupFail.setStatus("current")
_BridgeInterfaceBadLabel_Type = Counter64
_BridgeInterfaceBadLabel_Object = MibTableColumn
bridgeInterfaceBadLabel = _BridgeInterfaceBadLabel_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 45),
    _BridgeInterfaceBadLabel_Type()
)
bridgeInterfaceBadLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceBadLabel.setStatus("current")
_BridgeInterfaceTxInterfaceDisabled_Type = Counter64
_BridgeInterfaceTxInterfaceDisabled_Object = MibTableColumn
bridgeInterfaceTxInterfaceDisabled = _BridgeInterfaceTxInterfaceDisabled_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 46),
    _BridgeInterfaceTxInterfaceDisabled_Type()
)
bridgeInterfaceTxInterfaceDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxInterfaceDisabled.setStatus("current")
_BridgeInterfaceRxMulticastPkts_Type = Counter64
_BridgeInterfaceRxMulticastPkts_Object = MibTableColumn
bridgeInterfaceRxMulticastPkts = _BridgeInterfaceRxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 47),
    _BridgeInterfaceRxMulticastPkts_Type()
)
bridgeInterfaceRxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxMulticastPkts.setStatus("current")
_BridgeInterfaceRxBroadcastPkts_Type = Counter64
_BridgeInterfaceRxBroadcastPkts_Object = MibTableColumn
bridgeInterfaceRxBroadcastPkts = _BridgeInterfaceRxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 48),
    _BridgeInterfaceRxBroadcastPkts_Type()
)
bridgeInterfaceRxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxBroadcastPkts.setStatus("current")
_BridgeInterfaceTxMulticastPkts_Type = Counter64
_BridgeInterfaceTxMulticastPkts_Object = MibTableColumn
bridgeInterfaceTxMulticastPkts = _BridgeInterfaceTxMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 49),
    _BridgeInterfaceTxMulticastPkts_Type()
)
bridgeInterfaceTxMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxMulticastPkts.setStatus("current")
_BridgeInterfaceTxBroadcastPkts_Type = Counter64
_BridgeInterfaceTxBroadcastPkts_Object = MibTableColumn
bridgeInterfaceTxBroadcastPkts = _BridgeInterfaceTxBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 50),
    _BridgeInterfaceTxBroadcastPkts_Type()
)
bridgeInterfaceTxBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxBroadcastPkts.setStatus("current")
_BridgeInterfaceRxPausePkts_Type = Counter64
_BridgeInterfaceRxPausePkts_Object = MibTableColumn
bridgeInterfaceRxPausePkts = _BridgeInterfaceRxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 51),
    _BridgeInterfaceRxPausePkts_Type()
)
bridgeInterfaceRxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPausePkts.setStatus("current")
_BridgeInterfaceRxDmacFilterDrops_Type = Counter64
_BridgeInterfaceRxDmacFilterDrops_Object = MibTableColumn
bridgeInterfaceRxDmacFilterDrops = _BridgeInterfaceRxDmacFilterDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 52),
    _BridgeInterfaceRxDmacFilterDrops_Type()
)
bridgeInterfaceRxDmacFilterDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxDmacFilterDrops.setStatus("current")
_BridgeInterfaceRxWredDrops_Type = Counter64
_BridgeInterfaceRxWredDrops_Object = MibTableColumn
bridgeInterfaceRxWredDrops = _BridgeInterfaceRxWredDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 53),
    _BridgeInterfaceRxWredDrops_Type()
)
bridgeInterfaceRxWredDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxWredDrops.setStatus("current")
_BridgeInterfaceRxInterfaceNotFound_Type = Counter64
_BridgeInterfaceRxInterfaceNotFound_Object = MibTableColumn
bridgeInterfaceRxInterfaceNotFound = _BridgeInterfaceRxInterfaceNotFound_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 54),
    _BridgeInterfaceRxInterfaceNotFound_Type()
)
bridgeInterfaceRxInterfaceNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxInterfaceNotFound.setStatus("current")
_BridgeInterfaceRxInbErrors_Type = Counter64
_BridgeInterfaceRxInbErrors_Object = MibTableColumn
bridgeInterfaceRxInbErrors = _BridgeInterfaceRxInbErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 55),
    _BridgeInterfaceRxInbErrors_Type()
)
bridgeInterfaceRxInbErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxInbErrors.setStatus("current")
_BridgeInterfaceRxOversizeErrors_Type = Counter64
_BridgeInterfaceRxOversizeErrors_Object = MibTableColumn
bridgeInterfaceRxOversizeErrors = _BridgeInterfaceRxOversizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 56),
    _BridgeInterfaceRxOversizeErrors_Type()
)
bridgeInterfaceRxOversizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxOversizeErrors.setStatus("current")
_BridgeInterfaceRxFcsAlignErrors_Type = Counter64
_BridgeInterfaceRxFcsAlignErrors_Object = MibTableColumn
bridgeInterfaceRxFcsAlignErrors = _BridgeInterfaceRxFcsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 57),
    _BridgeInterfaceRxFcsAlignErrors_Type()
)
bridgeInterfaceRxFcsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxFcsAlignErrors.setStatus("current")
_BridgeInterfaceRxUndersizeErrors_Type = Counter64
_BridgeInterfaceRxUndersizeErrors_Object = MibTableColumn
bridgeInterfaceRxUndersizeErrors = _BridgeInterfaceRxUndersizeErrors_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 58),
    _BridgeInterfaceRxUndersizeErrors_Type()
)
bridgeInterfaceRxUndersizeErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxUndersizeErrors.setStatus("current")
_BridgeInterfaceTxUnderflowPkts_Type = Counter64
_BridgeInterfaceTxUnderflowPkts_Object = MibTableColumn
bridgeInterfaceTxUnderflowPkts = _BridgeInterfaceTxUnderflowPkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 59),
    _BridgeInterfaceTxUnderflowPkts_Type()
)
bridgeInterfaceTxUnderflowPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxUnderflowPkts.setStatus("current")
_BridgeInterfaceTxCollisionDrops_Type = Counter64
_BridgeInterfaceTxCollisionDrops_Object = MibTableColumn
bridgeInterfaceTxCollisionDrops = _BridgeInterfaceTxCollisionDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 60),
    _BridgeInterfaceTxCollisionDrops_Type()
)
bridgeInterfaceTxCollisionDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxCollisionDrops.setStatus("current")
_BridgeInterfaceTxPausePkts_Type = Counter64
_BridgeInterfaceTxPausePkts_Object = MibTableColumn
bridgeInterfaceTxPausePkts = _BridgeInterfaceTxPausePkts_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 61),
    _BridgeInterfaceTxPausePkts_Type()
)
bridgeInterfaceTxPausePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPausePkts.setStatus("current")
_BridgeInterfaceTxFragmentsNeeded_Type = Counter64
_BridgeInterfaceTxFragmentsNeeded_Object = MibTableColumn
bridgeInterfaceTxFragmentsNeeded = _BridgeInterfaceTxFragmentsNeeded_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 62),
    _BridgeInterfaceTxFragmentsNeeded_Type()
)
bridgeInterfaceTxFragmentsNeeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxFragmentsNeeded.setStatus("current")
_BridgeInterfaceTxFragments_Type = Counter64
_BridgeInterfaceTxFragments_Object = MibTableColumn
bridgeInterfaceTxFragments = _BridgeInterfaceTxFragments_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 63),
    _BridgeInterfaceTxFragments_Type()
)
bridgeInterfaceTxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxFragments.setStatus("current")
_BridgeInterfaceTxFragmentDrops_Type = Counter64
_BridgeInterfaceTxFragmentDrops_Object = MibTableColumn
bridgeInterfaceTxFragmentDrops = _BridgeInterfaceTxFragmentDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 64),
    _BridgeInterfaceTxFragmentDrops_Type()
)
bridgeInterfaceTxFragmentDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxFragmentDrops.setStatus("current")
_BridgeInterfaceTxTailRedDrops_Type = Counter64
_BridgeInterfaceTxTailRedDrops_Object = MibTableColumn
bridgeInterfaceTxTailRedDrops = _BridgeInterfaceTxTailRedDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 65),
    _BridgeInterfaceTxTailRedDrops_Type()
)
bridgeInterfaceTxTailRedDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxTailRedDrops.setStatus("current")
_BridgeInterfaceLlqDrops_Type = Counter64
_BridgeInterfaceLlqDrops_Object = MibTableColumn
bridgeInterfaceLlqDrops = _BridgeInterfaceLlqDrops_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 66),
    _BridgeInterfaceLlqDrops_Type()
)
bridgeInterfaceLlqDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceLlqDrops.setStatus("current")
_BridgeInterfaceRxPktSize64_Type = Counter64
_BridgeInterfaceRxPktSize64_Object = MibTableColumn
bridgeInterfaceRxPktSize64 = _BridgeInterfaceRxPktSize64_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 67),
    _BridgeInterfaceRxPktSize64_Type()
)
bridgeInterfaceRxPktSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPktSize64.setStatus("current")
_BridgeInterfaceRxPktSizeLt64_Type = Counter64
_BridgeInterfaceRxPktSizeLt64_Object = MibTableColumn
bridgeInterfaceRxPktSizeLt64 = _BridgeInterfaceRxPktSizeLt64_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 68),
    _BridgeInterfaceRxPktSizeLt64_Type()
)
bridgeInterfaceRxPktSizeLt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPktSizeLt64.setStatus("current")
_BridgeInterfaceRxPktSize65127_Type = Counter64
_BridgeInterfaceRxPktSize65127_Object = MibTableColumn
bridgeInterfaceRxPktSize65127 = _BridgeInterfaceRxPktSize65127_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 69),
    _BridgeInterfaceRxPktSize65127_Type()
)
bridgeInterfaceRxPktSize65127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPktSize65127.setStatus("current")
_BridgeInterfaceRxPktSize128255_Type = Counter64
_BridgeInterfaceRxPktSize128255_Object = MibTableColumn
bridgeInterfaceRxPktSize128255 = _BridgeInterfaceRxPktSize128255_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 70),
    _BridgeInterfaceRxPktSize128255_Type()
)
bridgeInterfaceRxPktSize128255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPktSize128255.setStatus("current")
_BridgeInterfaceRxPktSize256511_Type = Counter64
_BridgeInterfaceRxPktSize256511_Object = MibTableColumn
bridgeInterfaceRxPktSize256511 = _BridgeInterfaceRxPktSize256511_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 71),
    _BridgeInterfaceRxPktSize256511_Type()
)
bridgeInterfaceRxPktSize256511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPktSize256511.setStatus("current")
_BridgeInterfaceRxPktSize5121023_Type = Counter64
_BridgeInterfaceRxPktSize5121023_Object = MibTableColumn
bridgeInterfaceRxPktSize5121023 = _BridgeInterfaceRxPktSize5121023_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 72),
    _BridgeInterfaceRxPktSize5121023_Type()
)
bridgeInterfaceRxPktSize5121023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPktSize5121023.setStatus("current")
_BridgeInterfaceRxPktSize10241518_Type = Counter64
_BridgeInterfaceRxPktSize10241518_Object = MibTableColumn
bridgeInterfaceRxPktSize10241518 = _BridgeInterfaceRxPktSize10241518_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 73),
    _BridgeInterfaceRxPktSize10241518_Type()
)
bridgeInterfaceRxPktSize10241518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPktSize10241518.setStatus("current")
_BridgeInterfaceRxPktSizeGt1518_Type = Counter64
_BridgeInterfaceRxPktSizeGt1518_Object = MibTableColumn
bridgeInterfaceRxPktSizeGt1518 = _BridgeInterfaceRxPktSizeGt1518_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 74),
    _BridgeInterfaceRxPktSizeGt1518_Type()
)
bridgeInterfaceRxPktSizeGt1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPktSizeGt1518.setStatus("current")
_BridgeInterfaceTxPktSize64_Type = Counter64
_BridgeInterfaceTxPktSize64_Object = MibTableColumn
bridgeInterfaceTxPktSize64 = _BridgeInterfaceTxPktSize64_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 75),
    _BridgeInterfaceTxPktSize64_Type()
)
bridgeInterfaceTxPktSize64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPktSize64.setStatus("current")
_BridgeInterfaceTxPktSizeLt64_Type = Counter64
_BridgeInterfaceTxPktSizeLt64_Object = MibTableColumn
bridgeInterfaceTxPktSizeLt64 = _BridgeInterfaceTxPktSizeLt64_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 76),
    _BridgeInterfaceTxPktSizeLt64_Type()
)
bridgeInterfaceTxPktSizeLt64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPktSizeLt64.setStatus("current")
_BridgeInterfaceTxPktSize65127_Type = Counter64
_BridgeInterfaceTxPktSize65127_Object = MibTableColumn
bridgeInterfaceTxPktSize65127 = _BridgeInterfaceTxPktSize65127_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 77),
    _BridgeInterfaceTxPktSize65127_Type()
)
bridgeInterfaceTxPktSize65127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPktSize65127.setStatus("current")
_BridgeInterfaceTxPktSize128255_Type = Counter64
_BridgeInterfaceTxPktSize128255_Object = MibTableColumn
bridgeInterfaceTxPktSize128255 = _BridgeInterfaceTxPktSize128255_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 78),
    _BridgeInterfaceTxPktSize128255_Type()
)
bridgeInterfaceTxPktSize128255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPktSize128255.setStatus("current")
_BridgeInterfaceTxPktSize256511_Type = Counter64
_BridgeInterfaceTxPktSize256511_Object = MibTableColumn
bridgeInterfaceTxPktSize256511 = _BridgeInterfaceTxPktSize256511_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 79),
    _BridgeInterfaceTxPktSize256511_Type()
)
bridgeInterfaceTxPktSize256511.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPktSize256511.setStatus("current")
_BridgeInterfaceTxPktSize5121023_Type = Counter64
_BridgeInterfaceTxPktSize5121023_Object = MibTableColumn
bridgeInterfaceTxPktSize5121023 = _BridgeInterfaceTxPktSize5121023_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 80),
    _BridgeInterfaceTxPktSize5121023_Type()
)
bridgeInterfaceTxPktSize5121023.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPktSize5121023.setStatus("current")
_BridgeInterfaceTxPktSize10241518_Type = Counter64
_BridgeInterfaceTxPktSize10241518_Object = MibTableColumn
bridgeInterfaceTxPktSize10241518 = _BridgeInterfaceTxPktSize10241518_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 81),
    _BridgeInterfaceTxPktSize10241518_Type()
)
bridgeInterfaceTxPktSize10241518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPktSize10241518.setStatus("current")
_BridgeInterfaceTxPktSizeGt1518_Type = Counter64
_BridgeInterfaceTxPktSizeGt1518_Object = MibTableColumn
bridgeInterfaceTxPktSizeGt1518 = _BridgeInterfaceTxPktSizeGt1518_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 82),
    _BridgeInterfaceTxPktSizeGt1518_Type()
)
bridgeInterfaceTxPktSizeGt1518.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceTxPktSizeGt1518.setStatus("current")
_BridgeInterfaceRxPolicerRemark_Type = Counter64
_BridgeInterfaceRxPolicerRemark_Object = MibTableColumn
bridgeInterfaceRxPolicerRemark = _BridgeInterfaceRxPolicerRemark_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 5, 1, 83),
    _BridgeInterfaceRxPolicerRemark_Type()
)
bridgeInterfaceRxPolicerRemark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeInterfaceRxPolicerRemark.setStatus("current")
_BridgeMacTable_Object = MibTable
bridgeMacTable = _BridgeMacTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6)
)
if mibBuilder.loadTexts:
    bridgeMacTable.setStatus("current")
_BridgeMacEntry_Object = MibTableRow
bridgeMacEntry = _BridgeMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1)
)
bridgeMacEntry.setIndexNames(
    (0, "VIPTELA-BRIDGE", "bridgeMacBridgeId"),
    (0, "VIPTELA-BRIDGE", "bridgeMacInterface"),
    (0, "VIPTELA-BRIDGE", "bridgeMacMacAddress"),
)
if mibBuilder.loadTexts:
    bridgeMacEntry.setStatus("current")


class _BridgeMacBridgeId_Type(Unsigned32):
    """Custom type bridgeMacBridgeId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_BridgeMacBridgeId_Type.__name__ = "Unsigned32"
_BridgeMacBridgeId_Object = MibTableColumn
bridgeMacBridgeId = _BridgeMacBridgeId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 1),
    _BridgeMacBridgeId_Type()
)
bridgeMacBridgeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeMacBridgeId.setStatus("current")


class _BridgeMacInterface_Type(String):
    """Custom type bridgeMacInterface based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BridgeMacInterface_Type.__name__ = "String"
_BridgeMacInterface_Object = MibTableColumn
bridgeMacInterface = _BridgeMacInterface_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 2),
    _BridgeMacInterface_Type()
)
bridgeMacInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeMacInterface.setStatus("current")


class _BridgeMacMacAddress_Type(String):
    """Custom type bridgeMacMacAddress based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_BridgeMacMacAddress_Type.__name__ = "String"
_BridgeMacMacAddress_Object = MibTableColumn
bridgeMacMacAddress = _BridgeMacMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 3),
    _BridgeMacMacAddress_Type()
)
bridgeMacMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bridgeMacMacAddress.setStatus("current")
_BridgeMacType_Type = String
_BridgeMacType_Object = MibTableColumn
bridgeMacType = _BridgeMacType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 4),
    _BridgeMacType_Type()
)
bridgeMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeMacType.setStatus("current")
_BridgeMacExpiryTime_Type = String
_BridgeMacExpiryTime_Object = MibTableColumn
bridgeMacExpiryTime = _BridgeMacExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 5),
    _BridgeMacExpiryTime_Type()
)
bridgeMacExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeMacExpiryTime.setStatus("current")
_BridgeMacRxPackets_Type = Counter64
_BridgeMacRxPackets_Object = MibTableColumn
bridgeMacRxPackets = _BridgeMacRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 6),
    _BridgeMacRxPackets_Type()
)
bridgeMacRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeMacRxPackets.setStatus("current")
_BridgeMacRxOctets_Type = Counter64
_BridgeMacRxOctets_Object = MibTableColumn
bridgeMacRxOctets = _BridgeMacRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 7),
    _BridgeMacRxOctets_Type()
)
bridgeMacRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeMacRxOctets.setStatus("current")
_BridgeMacTxPackets_Type = Counter64
_BridgeMacTxPackets_Object = MibTableColumn
bridgeMacTxPackets = _BridgeMacTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 8),
    _BridgeMacTxPackets_Type()
)
bridgeMacTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeMacTxPackets.setStatus("current")
_BridgeMacTxOctets_Type = Counter64
_BridgeMacTxOctets_Object = MibTableColumn
bridgeMacTxOctets = _BridgeMacTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 41916, 10, 1, 6, 1, 9),
    _BridgeMacTxOctets_Type()
)
bridgeMacTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeMacTxOctets.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-BRIDGE",
    **{"UnsignedShort": UnsignedShort,
       "ConfdString": ConfdString,
       "String": String,
       "viptela-bridge": viptela_bridge,
       "bridge": bridge,
       "bridgeTableTable": bridgeTableTable,
       "bridgeTableEntry": bridgeTableEntry,
       "bridgeTableBridgeId": bridgeTableBridgeId,
       "bridgeTableName": bridgeTableName,
       "bridgeTableVlan": bridgeTableVlan,
       "bridgeTableRoutingInterface": bridgeTableRoutingInterface,
       "bridgeTableMaxMacs": bridgeTableMaxMacs,
       "bridgeTableNumMacs": bridgeTableNumMacs,
       "bridgeTableAgeTime": bridgeTableAgeTime,
       "bridgeTableRxPackets": bridgeTableRxPackets,
       "bridgeTableRxOctets": bridgeTableRxOctets,
       "bridgeTableTxPackets": bridgeTableTxPackets,
       "bridgeTableTxOctets": bridgeTableTxOctets,
       "bridgeTableFloodPackets": bridgeTableFloodPackets,
       "bridgeTableFloodOctets": bridgeTableFloodOctets,
       "bridgeTableRxRoutedPackets": bridgeTableRxRoutedPackets,
       "bridgeTableTxRoutedPackets": bridgeTableTxRoutedPackets,
       "bridgeTableLearn": bridgeTableLearn,
       "bridgeTableAge": bridgeTableAge,
       "bridgeTableMove": bridgeTableMove,
       "bridgeInterfaceTable": bridgeInterfaceTable,
       "bridgeInterfaceEntry": bridgeInterfaceEntry,
       "bridgeInterfaceBridgeId": bridgeInterfaceBridgeId,
       "bridgeInterfaceIfName": bridgeInterfaceIfName,
       "bridgeInterfaceVlan": bridgeInterfaceVlan,
       "bridgeInterfaceNativeVlan": bridgeInterfaceNativeVlan,
       "bridgeInterfaceAdminStatus": bridgeInterfaceAdminStatus,
       "bridgeInterfaceOperStatus": bridgeInterfaceOperStatus,
       "bridgeInterfaceEncapType": bridgeInterfaceEncapType,
       "bridgeInterfaceIfindex": bridgeInterfaceIfindex,
       "bridgeInterfaceMtu": bridgeInterfaceMtu,
       "bridgeInterfaceRxPackets": bridgeInterfaceRxPackets,
       "bridgeInterfaceRxOctets": bridgeInterfaceRxOctets,
       "bridgeInterfaceTxPackets": bridgeInterfaceTxPackets,
       "bridgeInterfaceTxOctets": bridgeInterfaceTxOctets,
       "bridgeInterfaceRxErrors": bridgeInterfaceRxErrors,
       "bridgeInterfaceRxDrops": bridgeInterfaceRxDrops,
       "bridgeInterfaceTxErrors": bridgeInterfaceTxErrors,
       "bridgeInterfaceTxDrops": bridgeInterfaceTxDrops,
       "bridgeInterfaceRxPps": bridgeInterfaceRxPps,
       "bridgeInterfaceRxKbps": bridgeInterfaceRxKbps,
       "bridgeInterfaceTxPps": bridgeInterfaceTxPps,
       "bridgeInterfaceTxKbps": bridgeInterfaceTxKbps,
       "bridgeInterfaceRxArpRequests": bridgeInterfaceRxArpRequests,
       "bridgeInterfaceTxArpReplies": bridgeInterfaceTxArpReplies,
       "bridgeInterfaceTxArpRequests": bridgeInterfaceTxArpRequests,
       "bridgeInterfaceRxArpReplies": bridgeInterfaceRxArpReplies,
       "bridgeInterfaceArpAddFails": bridgeInterfaceArpAddFails,
       "bridgeInterfaceRxArpReplyDrops": bridgeInterfaceRxArpReplyDrops,
       "bridgeInterfaceRxArpRateLimitDrops": bridgeInterfaceRxArpRateLimitDrops,
       "bridgeInterfaceTxArpRateLimitDrops": bridgeInterfaceTxArpRateLimitDrops,
       "bridgeInterfaceRxArpNonLocalDrops": bridgeInterfaceRxArpNonLocalDrops,
       "bridgeInterfaceTxArpRequestFail": bridgeInterfaceTxArpRequestFail,
       "bridgeInterfaceTxNoArpDrops": bridgeInterfaceTxNoArpDrops,
       "bridgeInterfaceRxIpTtlExpired": bridgeInterfaceRxIpTtlExpired,
       "bridgeInterfaceRxIpErrors": bridgeInterfaceRxIpErrors,
       "bridgeInterfaceInterfaceDisabled": bridgeInterfaceInterfaceDisabled,
       "bridgeInterfaceRxPolicerDrops": bridgeInterfaceRxPolicerDrops,
       "bridgeInterfaceRxNonIpDrops": bridgeInterfaceRxNonIpDrops,
       "bridgeInterfaceFilterDrops": bridgeInterfaceFilterDrops,
       "bridgeInterfaceMirrorDrops": bridgeInterfaceMirrorDrops,
       "bridgeInterfaceCpuPolicerDrops": bridgeInterfaceCpuPolicerDrops,
       "bridgeInterfaceTxIcmpPolicerDrops": bridgeInterfaceTxIcmpPolicerDrops,
       "bridgeInterfaceTxIcmpMirroredDrops": bridgeInterfaceTxIcmpMirroredDrops,
       "bridgeInterfaceSplitHorizonDrops": bridgeInterfaceSplitHorizonDrops,
       "bridgeInterfaceRouteLookupFail": bridgeInterfaceRouteLookupFail,
       "bridgeInterfaceBadLabel": bridgeInterfaceBadLabel,
       "bridgeInterfaceTxInterfaceDisabled": bridgeInterfaceTxInterfaceDisabled,
       "bridgeInterfaceRxMulticastPkts": bridgeInterfaceRxMulticastPkts,
       "bridgeInterfaceRxBroadcastPkts": bridgeInterfaceRxBroadcastPkts,
       "bridgeInterfaceTxMulticastPkts": bridgeInterfaceTxMulticastPkts,
       "bridgeInterfaceTxBroadcastPkts": bridgeInterfaceTxBroadcastPkts,
       "bridgeInterfaceRxPausePkts": bridgeInterfaceRxPausePkts,
       "bridgeInterfaceRxDmacFilterDrops": bridgeInterfaceRxDmacFilterDrops,
       "bridgeInterfaceRxWredDrops": bridgeInterfaceRxWredDrops,
       "bridgeInterfaceRxInterfaceNotFound": bridgeInterfaceRxInterfaceNotFound,
       "bridgeInterfaceRxInbErrors": bridgeInterfaceRxInbErrors,
       "bridgeInterfaceRxOversizeErrors": bridgeInterfaceRxOversizeErrors,
       "bridgeInterfaceRxFcsAlignErrors": bridgeInterfaceRxFcsAlignErrors,
       "bridgeInterfaceRxUndersizeErrors": bridgeInterfaceRxUndersizeErrors,
       "bridgeInterfaceTxUnderflowPkts": bridgeInterfaceTxUnderflowPkts,
       "bridgeInterfaceTxCollisionDrops": bridgeInterfaceTxCollisionDrops,
       "bridgeInterfaceTxPausePkts": bridgeInterfaceTxPausePkts,
       "bridgeInterfaceTxFragmentsNeeded": bridgeInterfaceTxFragmentsNeeded,
       "bridgeInterfaceTxFragments": bridgeInterfaceTxFragments,
       "bridgeInterfaceTxFragmentDrops": bridgeInterfaceTxFragmentDrops,
       "bridgeInterfaceTxTailRedDrops": bridgeInterfaceTxTailRedDrops,
       "bridgeInterfaceLlqDrops": bridgeInterfaceLlqDrops,
       "bridgeInterfaceRxPktSize64": bridgeInterfaceRxPktSize64,
       "bridgeInterfaceRxPktSizeLt64": bridgeInterfaceRxPktSizeLt64,
       "bridgeInterfaceRxPktSize65127": bridgeInterfaceRxPktSize65127,
       "bridgeInterfaceRxPktSize128255": bridgeInterfaceRxPktSize128255,
       "bridgeInterfaceRxPktSize256511": bridgeInterfaceRxPktSize256511,
       "bridgeInterfaceRxPktSize5121023": bridgeInterfaceRxPktSize5121023,
       "bridgeInterfaceRxPktSize10241518": bridgeInterfaceRxPktSize10241518,
       "bridgeInterfaceRxPktSizeGt1518": bridgeInterfaceRxPktSizeGt1518,
       "bridgeInterfaceTxPktSize64": bridgeInterfaceTxPktSize64,
       "bridgeInterfaceTxPktSizeLt64": bridgeInterfaceTxPktSizeLt64,
       "bridgeInterfaceTxPktSize65127": bridgeInterfaceTxPktSize65127,
       "bridgeInterfaceTxPktSize128255": bridgeInterfaceTxPktSize128255,
       "bridgeInterfaceTxPktSize256511": bridgeInterfaceTxPktSize256511,
       "bridgeInterfaceTxPktSize5121023": bridgeInterfaceTxPktSize5121023,
       "bridgeInterfaceTxPktSize10241518": bridgeInterfaceTxPktSize10241518,
       "bridgeInterfaceTxPktSizeGt1518": bridgeInterfaceTxPktSizeGt1518,
       "bridgeInterfaceRxPolicerRemark": bridgeInterfaceRxPolicerRemark,
       "bridgeMacTable": bridgeMacTable,
       "bridgeMacEntry": bridgeMacEntry,
       "bridgeMacBridgeId": bridgeMacBridgeId,
       "bridgeMacInterface": bridgeMacInterface,
       "bridgeMacMacAddress": bridgeMacMacAddress,
       "bridgeMacType": bridgeMacType,
       "bridgeMacExpiryTime": bridgeMacExpiryTime,
       "bridgeMacRxPackets": bridgeMacRxPackets,
       "bridgeMacRxOctets": bridgeMacRxOctets,
       "bridgeMacTxPackets": bridgeMacTxPackets,
       "bridgeMacTxOctets": bridgeMacTxOctets}
)
