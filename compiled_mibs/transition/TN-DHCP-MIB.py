# SNMP MIB module (TN-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DHCP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:15 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33)
)
if mibBuilder.loadTexts:
    tnDhcpMIB.setRevisions(
        ("2012-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnDhcpMIBObjects_ObjectIdentity = ObjectIdentity
tnDhcpMIBObjects = _TnDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1)
)
_TnDhcpSnoopingMgmt_ObjectIdentity = ObjectIdentity
tnDhcpSnoopingMgmt = _TnDhcpSnoopingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1)
)
_TnDhcpSnoopingTable_Object = MibTable
tnDhcpSnoopingTable = _TnDhcpSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingTable.setStatus("current")
_TnDhcpSnoopingEntry_Object = MibTableRow
tnDhcpSnoopingEntry = _TnDhcpSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 1, 1)
)
tnDhcpSnoopingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingEntry.setStatus("current")


class _TnDhcpSnoopingMode_Type(TruthValue):
    """Custom type tnDhcpSnoopingMode based on TruthValue"""
    defaultValue = 2


_TnDhcpSnoopingMode_Type.__name__ = "TruthValue"
_TnDhcpSnoopingMode_Object = MibTableColumn
tnDhcpSnoopingMode = _TnDhcpSnoopingMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 1, 1, 1),
    _TnDhcpSnoopingMode_Type()
)
tnDhcpSnoopingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpSnoopingMode.setStatus("current")
_TnDhcpSnoopingIfTable_Object = MibTable
tnDhcpSnoopingIfTable = _TnDhcpSnoopingIfTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingIfTable.setStatus("current")
_TnDhcpSnoopingIfEntry_Object = MibTableRow
tnDhcpSnoopingIfEntry = _TnDhcpSnoopingIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 2, 1)
)
tnDhcpSnoopingIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingIfEntry.setStatus("current")


class _TnDhcpSnoopingIfMode_Type(Integer32):
    """Custom type tnDhcpSnoopingIfMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_TnDhcpSnoopingIfMode_Type.__name__ = "Integer32"
_TnDhcpSnoopingIfMode_Object = MibTableColumn
tnDhcpSnoopingIfMode = _TnDhcpSnoopingIfMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 2, 1, 1),
    _TnDhcpSnoopingIfMode_Type()
)
tnDhcpSnoopingIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpSnoopingIfMode.setStatus("current")
_TnDhcpSnoopingStatisticsTable_Object = MibTable
tnDhcpSnoopingStatisticsTable = _TnDhcpSnoopingStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTable.setStatus("current")
_TnDhcpSnoopingStatisticsEntry_Object = MibTableRow
tnDhcpSnoopingStatisticsEntry = _TnDhcpSnoopingStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1)
)
tnDhcpSnoopingStatisticsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsEntry.setStatus("current")


class _TnDhcpSnoopingStatisticsClear_Type(TruthValue):
    """Custom type tnDhcpSnoopingStatisticsClear based on TruthValue"""
    defaultValue = 2


_TnDhcpSnoopingStatisticsClear_Type.__name__ = "TruthValue"
_TnDhcpSnoopingStatisticsClear_Object = MibTableColumn
tnDhcpSnoopingStatisticsClear = _TnDhcpSnoopingStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 1),
    _TnDhcpSnoopingStatisticsClear_Type()
)
tnDhcpSnoopingStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsClear.setStatus("current")
_TnDhcpSnoopingStatisticsRxDiscover_Type = Integer32
_TnDhcpSnoopingStatisticsRxDiscover_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxDiscover = _TnDhcpSnoopingStatisticsRxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 2),
    _TnDhcpSnoopingStatisticsRxDiscover_Type()
)
tnDhcpSnoopingStatisticsRxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxDiscover.setStatus("current")
_TnDhcpSnoopingStatisticsTxDiscover_Type = Integer32
_TnDhcpSnoopingStatisticsTxDiscover_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxDiscover = _TnDhcpSnoopingStatisticsTxDiscover_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 3),
    _TnDhcpSnoopingStatisticsTxDiscover_Type()
)
tnDhcpSnoopingStatisticsTxDiscover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxDiscover.setStatus("current")
_TnDhcpSnoopingStatisticsRxOffer_Type = Integer32
_TnDhcpSnoopingStatisticsRxOffer_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxOffer = _TnDhcpSnoopingStatisticsRxOffer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 4),
    _TnDhcpSnoopingStatisticsRxOffer_Type()
)
tnDhcpSnoopingStatisticsRxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxOffer.setStatus("current")
_TnDhcpSnoopingStatisticsTxOffer_Type = Integer32
_TnDhcpSnoopingStatisticsTxOffer_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxOffer = _TnDhcpSnoopingStatisticsTxOffer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 5),
    _TnDhcpSnoopingStatisticsTxOffer_Type()
)
tnDhcpSnoopingStatisticsTxOffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxOffer.setStatus("current")
_TnDhcpSnoopingStatisticsRxRequest_Type = Integer32
_TnDhcpSnoopingStatisticsRxRequest_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxRequest = _TnDhcpSnoopingStatisticsRxRequest_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 6),
    _TnDhcpSnoopingStatisticsRxRequest_Type()
)
tnDhcpSnoopingStatisticsRxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxRequest.setStatus("current")
_TnDhcpSnoopingStatisticsTxRequest_Type = Integer32
_TnDhcpSnoopingStatisticsTxRequest_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxRequest = _TnDhcpSnoopingStatisticsTxRequest_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 7),
    _TnDhcpSnoopingStatisticsTxRequest_Type()
)
tnDhcpSnoopingStatisticsTxRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxRequest.setStatus("current")
_TnDhcpSnoopingStatisticsRxDecline_Type = Integer32
_TnDhcpSnoopingStatisticsRxDecline_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxDecline = _TnDhcpSnoopingStatisticsRxDecline_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 8),
    _TnDhcpSnoopingStatisticsRxDecline_Type()
)
tnDhcpSnoopingStatisticsRxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxDecline.setStatus("current")
_TnDhcpSnoopingStatisticsTxDecline_Type = Integer32
_TnDhcpSnoopingStatisticsTxDecline_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxDecline = _TnDhcpSnoopingStatisticsTxDecline_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 9),
    _TnDhcpSnoopingStatisticsTxDecline_Type()
)
tnDhcpSnoopingStatisticsTxDecline.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxDecline.setStatus("current")
_TnDhcpSnoopingStatisticsRxACK_Type = Integer32
_TnDhcpSnoopingStatisticsRxACK_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxACK = _TnDhcpSnoopingStatisticsRxACK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 10),
    _TnDhcpSnoopingStatisticsRxACK_Type()
)
tnDhcpSnoopingStatisticsRxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxACK.setStatus("current")
_TnDhcpSnoopingStatisticsTxACK_Type = Integer32
_TnDhcpSnoopingStatisticsTxACK_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxACK = _TnDhcpSnoopingStatisticsTxACK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 11),
    _TnDhcpSnoopingStatisticsTxACK_Type()
)
tnDhcpSnoopingStatisticsTxACK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxACK.setStatus("current")
_TnDhcpSnoopingStatisticsRxNAK_Type = Integer32
_TnDhcpSnoopingStatisticsRxNAK_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxNAK = _TnDhcpSnoopingStatisticsRxNAK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 12),
    _TnDhcpSnoopingStatisticsRxNAK_Type()
)
tnDhcpSnoopingStatisticsRxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxNAK.setStatus("current")
_TnDhcpSnoopingStatisticsTxNAK_Type = Integer32
_TnDhcpSnoopingStatisticsTxNAK_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxNAK = _TnDhcpSnoopingStatisticsTxNAK_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 13),
    _TnDhcpSnoopingStatisticsTxNAK_Type()
)
tnDhcpSnoopingStatisticsTxNAK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxNAK.setStatus("current")
_TnDhcpSnoopingStatisticsRxRelease_Type = Integer32
_TnDhcpSnoopingStatisticsRxRelease_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxRelease = _TnDhcpSnoopingStatisticsRxRelease_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 14),
    _TnDhcpSnoopingStatisticsRxRelease_Type()
)
tnDhcpSnoopingStatisticsRxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxRelease.setStatus("current")
_TnDhcpSnoopingStatisticsTxRelease_Type = Integer32
_TnDhcpSnoopingStatisticsTxRelease_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxRelease = _TnDhcpSnoopingStatisticsTxRelease_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 15),
    _TnDhcpSnoopingStatisticsTxRelease_Type()
)
tnDhcpSnoopingStatisticsTxRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxRelease.setStatus("current")
_TnDhcpSnoopingStatisticsRxInform_Type = Integer32
_TnDhcpSnoopingStatisticsRxInform_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxInform = _TnDhcpSnoopingStatisticsRxInform_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 16),
    _TnDhcpSnoopingStatisticsRxInform_Type()
)
tnDhcpSnoopingStatisticsRxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxInform.setStatus("current")
_TnDhcpSnoopingStatisticsTxInform_Type = Integer32
_TnDhcpSnoopingStatisticsTxInform_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxInform = _TnDhcpSnoopingStatisticsTxInform_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 17),
    _TnDhcpSnoopingStatisticsTxInform_Type()
)
tnDhcpSnoopingStatisticsTxInform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxInform.setStatus("current")
_TnDhcpSnoopingStatisticsRxLeaseQuery_Type = Integer32
_TnDhcpSnoopingStatisticsRxLeaseQuery_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxLeaseQuery = _TnDhcpSnoopingStatisticsRxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 18),
    _TnDhcpSnoopingStatisticsRxLeaseQuery_Type()
)
tnDhcpSnoopingStatisticsRxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxLeaseQuery.setStatus("current")
_TnDhcpSnoopingStatisticsTxLeaseQuery_Type = Integer32
_TnDhcpSnoopingStatisticsTxLeaseQuery_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxLeaseQuery = _TnDhcpSnoopingStatisticsTxLeaseQuery_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 19),
    _TnDhcpSnoopingStatisticsTxLeaseQuery_Type()
)
tnDhcpSnoopingStatisticsTxLeaseQuery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxLeaseQuery.setStatus("current")
_TnDhcpSnoopingStatisticsRxLeaseUnassigned_Type = Integer32
_TnDhcpSnoopingStatisticsRxLeaseUnassigned_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxLeaseUnassigned = _TnDhcpSnoopingStatisticsRxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 20),
    _TnDhcpSnoopingStatisticsRxLeaseUnassigned_Type()
)
tnDhcpSnoopingStatisticsRxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxLeaseUnassigned.setStatus("current")
_TnDhcpSnoopingStatisticsTxLeaseUnassigned_Type = Integer32
_TnDhcpSnoopingStatisticsTxLeaseUnassigned_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxLeaseUnassigned = _TnDhcpSnoopingStatisticsTxLeaseUnassigned_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 21),
    _TnDhcpSnoopingStatisticsTxLeaseUnassigned_Type()
)
tnDhcpSnoopingStatisticsTxLeaseUnassigned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxLeaseUnassigned.setStatus("current")
_TnDhcpSnoopingStatisticsRxLeaseUnknown_Type = Integer32
_TnDhcpSnoopingStatisticsRxLeaseUnknown_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxLeaseUnknown = _TnDhcpSnoopingStatisticsRxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 22),
    _TnDhcpSnoopingStatisticsRxLeaseUnknown_Type()
)
tnDhcpSnoopingStatisticsRxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxLeaseUnknown.setStatus("current")
_TnDhcpSnoopingStatisticsTxLeaseUnknown_Type = Integer32
_TnDhcpSnoopingStatisticsTxLeaseUnknown_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxLeaseUnknown = _TnDhcpSnoopingStatisticsTxLeaseUnknown_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 23),
    _TnDhcpSnoopingStatisticsTxLeaseUnknown_Type()
)
tnDhcpSnoopingStatisticsTxLeaseUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxLeaseUnknown.setStatus("current")
_TnDhcpSnoopingStatisticsRxLeaseActive_Type = Integer32
_TnDhcpSnoopingStatisticsRxLeaseActive_Object = MibTableColumn
tnDhcpSnoopingStatisticsRxLeaseActive = _TnDhcpSnoopingStatisticsRxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 24),
    _TnDhcpSnoopingStatisticsRxLeaseActive_Type()
)
tnDhcpSnoopingStatisticsRxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsRxLeaseActive.setStatus("current")
_TnDhcpSnoopingStatisticsTxLeaseActive_Type = Integer32
_TnDhcpSnoopingStatisticsTxLeaseActive_Object = MibTableColumn
tnDhcpSnoopingStatisticsTxLeaseActive = _TnDhcpSnoopingStatisticsTxLeaseActive_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 1, 3, 1, 25),
    _TnDhcpSnoopingStatisticsTxLeaseActive_Type()
)
tnDhcpSnoopingStatisticsTxLeaseActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpSnoopingStatisticsTxLeaseActive.setStatus("current")
_TnDhcpRelayMgmt_ObjectIdentity = ObjectIdentity
tnDhcpRelayMgmt = _TnDhcpRelayMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2)
)
_TnDhcpRelayTable_Object = MibTable
tnDhcpRelayTable = _TnDhcpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tnDhcpRelayTable.setStatus("current")
_TnDhcpRelayEntry_Object = MibTableRow
tnDhcpRelayEntry = _TnDhcpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 1, 1)
)
tnDhcpRelayEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpRelayEntry.setStatus("current")


class _TnDhcpRelayMode_Type(TruthValue):
    """Custom type tnDhcpRelayMode based on TruthValue"""
    defaultValue = 2


_TnDhcpRelayMode_Type.__name__ = "TruthValue"
_TnDhcpRelayMode_Object = MibTableColumn
tnDhcpRelayMode = _TnDhcpRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 1, 1, 1),
    _TnDhcpRelayMode_Type()
)
tnDhcpRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayMode.setStatus("current")
_TnDhcpRelayServerAddrType_Type = InetAddressType
_TnDhcpRelayServerAddrType_Object = MibTableColumn
tnDhcpRelayServerAddrType = _TnDhcpRelayServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 1, 1, 2),
    _TnDhcpRelayServerAddrType_Type()
)
tnDhcpRelayServerAddrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayServerAddrType.setStatus("current")
_TnDhcpRelayServerAddr_Type = InetAddress
_TnDhcpRelayServerAddr_Object = MibTableColumn
tnDhcpRelayServerAddr = _TnDhcpRelayServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 1, 1, 3),
    _TnDhcpRelayServerAddr_Type()
)
tnDhcpRelayServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayServerAddr.setStatus("current")


class _TnDhcpRelayInfoMode_Type(TruthValue):
    """Custom type tnDhcpRelayInfoMode based on TruthValue"""
    defaultValue = 2


_TnDhcpRelayInfoMode_Type.__name__ = "TruthValue"
_TnDhcpRelayInfoMode_Object = MibTableColumn
tnDhcpRelayInfoMode = _TnDhcpRelayInfoMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 1, 1, 4),
    _TnDhcpRelayInfoMode_Type()
)
tnDhcpRelayInfoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayInfoMode.setStatus("current")


class _TnDhcpRelayInfoPolicy_Type(Integer32):
    """Custom type tnDhcpRelayInfoPolicy based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replace", 0),
          ("keep", 1),
          ("drop", 2))
    )


_TnDhcpRelayInfoPolicy_Type.__name__ = "Integer32"
_TnDhcpRelayInfoPolicy_Object = MibTableColumn
tnDhcpRelayInfoPolicy = _TnDhcpRelayInfoPolicy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 1, 1, 5),
    _TnDhcpRelayInfoPolicy_Type()
)
tnDhcpRelayInfoPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayInfoPolicy.setStatus("current")
_TnDhcpRelayStatisticsTable_Object = MibTable
tnDhcpRelayStatisticsTable = _TnDhcpRelayStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsTable.setStatus("current")
_TnDhcpRelayStatisticsEntry_Object = MibTableRow
tnDhcpRelayStatisticsEntry = _TnDhcpRelayStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1)
)
tnDhcpRelayStatisticsEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsEntry.setStatus("current")


class _TnDhcpRelayStatisticsClear_Type(TruthValue):
    """Custom type tnDhcpRelayStatisticsClear based on TruthValue"""
    defaultValue = 2


_TnDhcpRelayStatisticsClear_Type.__name__ = "TruthValue"
_TnDhcpRelayStatisticsClear_Object = MibTableColumn
tnDhcpRelayStatisticsClear = _TnDhcpRelayStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 1),
    _TnDhcpRelayStatisticsClear_Type()
)
tnDhcpRelayStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsClear.setStatus("current")
_TnDhcpRelayStatisticsServerTransmitToServer_Type = Integer32
_TnDhcpRelayStatisticsServerTransmitToServer_Object = MibTableColumn
tnDhcpRelayStatisticsServerTransmitToServer = _TnDhcpRelayStatisticsServerTransmitToServer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 2),
    _TnDhcpRelayStatisticsServerTransmitToServer_Type()
)
tnDhcpRelayStatisticsServerTransmitToServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsServerTransmitToServer.setStatus("current")
_TnDhcpRelayStatisticsServerTransmitError_Type = Integer32
_TnDhcpRelayStatisticsServerTransmitError_Object = MibTableColumn
tnDhcpRelayStatisticsServerTransmitError = _TnDhcpRelayStatisticsServerTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 3),
    _TnDhcpRelayStatisticsServerTransmitError_Type()
)
tnDhcpRelayStatisticsServerTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsServerTransmitError.setStatus("current")
_TnDhcpRelayStatisticsServerReceiveFromServer_Type = Integer32
_TnDhcpRelayStatisticsServerReceiveFromServer_Object = MibTableColumn
tnDhcpRelayStatisticsServerReceiveFromServer = _TnDhcpRelayStatisticsServerReceiveFromServer_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 4),
    _TnDhcpRelayStatisticsServerReceiveFromServer_Type()
)
tnDhcpRelayStatisticsServerReceiveFromServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsServerReceiveFromServer.setStatus("current")
_TnDhcpRelayStatisticsServerReceiveMissingAgentOption_Type = Integer32
_TnDhcpRelayStatisticsServerReceiveMissingAgentOption_Object = MibTableColumn
tnDhcpRelayStatisticsServerReceiveMissingAgentOption = _TnDhcpRelayStatisticsServerReceiveMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 5),
    _TnDhcpRelayStatisticsServerReceiveMissingAgentOption_Type()
)
tnDhcpRelayStatisticsServerReceiveMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsServerReceiveMissingAgentOption.setStatus("current")
_TnDhcpRelayStatisticsServerReceiveMissingCircuitID_Type = Integer32
_TnDhcpRelayStatisticsServerReceiveMissingCircuitID_Object = MibTableColumn
tnDhcpRelayStatisticsServerReceiveMissingCircuitID = _TnDhcpRelayStatisticsServerReceiveMissingCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 6),
    _TnDhcpRelayStatisticsServerReceiveMissingCircuitID_Type()
)
tnDhcpRelayStatisticsServerReceiveMissingCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsServerReceiveMissingCircuitID.setStatus("current")
_TnDhcpRelayStatisticsServerReceiveMissingRemoteID_Type = Integer32
_TnDhcpRelayStatisticsServerReceiveMissingRemoteID_Object = MibTableColumn
tnDhcpRelayStatisticsServerReceiveMissingRemoteID = _TnDhcpRelayStatisticsServerReceiveMissingRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 7),
    _TnDhcpRelayStatisticsServerReceiveMissingRemoteID_Type()
)
tnDhcpRelayStatisticsServerReceiveMissingRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsServerReceiveMissingRemoteID.setStatus("current")
_TnDhcpRelayStatisticsServerReceiveBadCircuitID_Type = Integer32
_TnDhcpRelayStatisticsServerReceiveBadCircuitID_Object = MibTableColumn
tnDhcpRelayStatisticsServerReceiveBadCircuitID = _TnDhcpRelayStatisticsServerReceiveBadCircuitID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 8),
    _TnDhcpRelayStatisticsServerReceiveBadCircuitID_Type()
)
tnDhcpRelayStatisticsServerReceiveBadCircuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsServerReceiveBadCircuitID.setStatus("current")
_TnDhcpRelayStatisticsServerReceiveBadRemoteID_Type = Integer32
_TnDhcpRelayStatisticsServerReceiveBadRemoteID_Object = MibTableColumn
tnDhcpRelayStatisticsServerReceiveBadRemoteID = _TnDhcpRelayStatisticsServerReceiveBadRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 9),
    _TnDhcpRelayStatisticsServerReceiveBadRemoteID_Type()
)
tnDhcpRelayStatisticsServerReceiveBadRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsServerReceiveBadRemoteID.setStatus("current")
_TnDhcpRelayStatisticsClientTransmitToClient_Type = Integer32
_TnDhcpRelayStatisticsClientTransmitToClient_Object = MibTableColumn
tnDhcpRelayStatisticsClientTransmitToClient = _TnDhcpRelayStatisticsClientTransmitToClient_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 10),
    _TnDhcpRelayStatisticsClientTransmitToClient_Type()
)
tnDhcpRelayStatisticsClientTransmitToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsClientTransmitToClient.setStatus("current")
_TnDhcpRelayStatisticsClientTransmitError_Type = Integer32
_TnDhcpRelayStatisticsClientTransmitError_Object = MibTableColumn
tnDhcpRelayStatisticsClientTransmitError = _TnDhcpRelayStatisticsClientTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 11),
    _TnDhcpRelayStatisticsClientTransmitError_Type()
)
tnDhcpRelayStatisticsClientTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsClientTransmitError.setStatus("current")
_TnDhcpRelayStatisticsClientReceiveFromClient_Type = Integer32
_TnDhcpRelayStatisticsClientReceiveFromClient_Object = MibTableColumn
tnDhcpRelayStatisticsClientReceiveFromClient = _TnDhcpRelayStatisticsClientReceiveFromClient_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 12),
    _TnDhcpRelayStatisticsClientReceiveFromClient_Type()
)
tnDhcpRelayStatisticsClientReceiveFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsClientReceiveFromClient.setStatus("current")
_TnDhcpRelayStatisticsClientReceiveAgentOption_Type = Integer32
_TnDhcpRelayStatisticsClientReceiveAgentOption_Object = MibTableColumn
tnDhcpRelayStatisticsClientReceiveAgentOption = _TnDhcpRelayStatisticsClientReceiveAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 13),
    _TnDhcpRelayStatisticsClientReceiveAgentOption_Type()
)
tnDhcpRelayStatisticsClientReceiveAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsClientReceiveAgentOption.setStatus("current")
_TnDhcpRelayStatisticsClientReplaceAgentOption_Type = Integer32
_TnDhcpRelayStatisticsClientReplaceAgentOption_Object = MibTableColumn
tnDhcpRelayStatisticsClientReplaceAgentOption = _TnDhcpRelayStatisticsClientReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 14),
    _TnDhcpRelayStatisticsClientReplaceAgentOption_Type()
)
tnDhcpRelayStatisticsClientReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsClientReplaceAgentOption.setStatus("current")
_TnDhcpRelayStatisticsClientKeepAgentOption_Type = Integer32
_TnDhcpRelayStatisticsClientKeepAgentOption_Object = MibTableColumn
tnDhcpRelayStatisticsClientKeepAgentOption = _TnDhcpRelayStatisticsClientKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 15),
    _TnDhcpRelayStatisticsClientKeepAgentOption_Type()
)
tnDhcpRelayStatisticsClientKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsClientKeepAgentOption.setStatus("current")
_TnDhcpRelayStatisticsClientDropAgentOption_Type = Integer32
_TnDhcpRelayStatisticsClientDropAgentOption_Object = MibTableColumn
tnDhcpRelayStatisticsClientDropAgentOption = _TnDhcpRelayStatisticsClientDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 1, 2, 2, 1, 16),
    _TnDhcpRelayStatisticsClientDropAgentOption_Type()
)
tnDhcpRelayStatisticsClientDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatisticsClientDropAgentOption.setStatus("current")
_TnDhcpMIBNotifications_ObjectIdentity = ObjectIdentity
tnDhcpMIBNotifications = _TnDhcpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 33, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DHCP-MIB",
    **{"tnDhcpMIB": tnDhcpMIB,
       "tnDhcpMIBObjects": tnDhcpMIBObjects,
       "tnDhcpSnoopingMgmt": tnDhcpSnoopingMgmt,
       "tnDhcpSnoopingTable": tnDhcpSnoopingTable,
       "tnDhcpSnoopingEntry": tnDhcpSnoopingEntry,
       "tnDhcpSnoopingMode": tnDhcpSnoopingMode,
       "tnDhcpSnoopingIfTable": tnDhcpSnoopingIfTable,
       "tnDhcpSnoopingIfEntry": tnDhcpSnoopingIfEntry,
       "tnDhcpSnoopingIfMode": tnDhcpSnoopingIfMode,
       "tnDhcpSnoopingStatisticsTable": tnDhcpSnoopingStatisticsTable,
       "tnDhcpSnoopingStatisticsEntry": tnDhcpSnoopingStatisticsEntry,
       "tnDhcpSnoopingStatisticsClear": tnDhcpSnoopingStatisticsClear,
       "tnDhcpSnoopingStatisticsRxDiscover": tnDhcpSnoopingStatisticsRxDiscover,
       "tnDhcpSnoopingStatisticsTxDiscover": tnDhcpSnoopingStatisticsTxDiscover,
       "tnDhcpSnoopingStatisticsRxOffer": tnDhcpSnoopingStatisticsRxOffer,
       "tnDhcpSnoopingStatisticsTxOffer": tnDhcpSnoopingStatisticsTxOffer,
       "tnDhcpSnoopingStatisticsRxRequest": tnDhcpSnoopingStatisticsRxRequest,
       "tnDhcpSnoopingStatisticsTxRequest": tnDhcpSnoopingStatisticsTxRequest,
       "tnDhcpSnoopingStatisticsRxDecline": tnDhcpSnoopingStatisticsRxDecline,
       "tnDhcpSnoopingStatisticsTxDecline": tnDhcpSnoopingStatisticsTxDecline,
       "tnDhcpSnoopingStatisticsRxACK": tnDhcpSnoopingStatisticsRxACK,
       "tnDhcpSnoopingStatisticsTxACK": tnDhcpSnoopingStatisticsTxACK,
       "tnDhcpSnoopingStatisticsRxNAK": tnDhcpSnoopingStatisticsRxNAK,
       "tnDhcpSnoopingStatisticsTxNAK": tnDhcpSnoopingStatisticsTxNAK,
       "tnDhcpSnoopingStatisticsRxRelease": tnDhcpSnoopingStatisticsRxRelease,
       "tnDhcpSnoopingStatisticsTxRelease": tnDhcpSnoopingStatisticsTxRelease,
       "tnDhcpSnoopingStatisticsRxInform": tnDhcpSnoopingStatisticsRxInform,
       "tnDhcpSnoopingStatisticsTxInform": tnDhcpSnoopingStatisticsTxInform,
       "tnDhcpSnoopingStatisticsRxLeaseQuery": tnDhcpSnoopingStatisticsRxLeaseQuery,
       "tnDhcpSnoopingStatisticsTxLeaseQuery": tnDhcpSnoopingStatisticsTxLeaseQuery,
       "tnDhcpSnoopingStatisticsRxLeaseUnassigned": tnDhcpSnoopingStatisticsRxLeaseUnassigned,
       "tnDhcpSnoopingStatisticsTxLeaseUnassigned": tnDhcpSnoopingStatisticsTxLeaseUnassigned,
       "tnDhcpSnoopingStatisticsRxLeaseUnknown": tnDhcpSnoopingStatisticsRxLeaseUnknown,
       "tnDhcpSnoopingStatisticsTxLeaseUnknown": tnDhcpSnoopingStatisticsTxLeaseUnknown,
       "tnDhcpSnoopingStatisticsRxLeaseActive": tnDhcpSnoopingStatisticsRxLeaseActive,
       "tnDhcpSnoopingStatisticsTxLeaseActive": tnDhcpSnoopingStatisticsTxLeaseActive,
       "tnDhcpRelayMgmt": tnDhcpRelayMgmt,
       "tnDhcpRelayTable": tnDhcpRelayTable,
       "tnDhcpRelayEntry": tnDhcpRelayEntry,
       "tnDhcpRelayMode": tnDhcpRelayMode,
       "tnDhcpRelayServerAddrType": tnDhcpRelayServerAddrType,
       "tnDhcpRelayServerAddr": tnDhcpRelayServerAddr,
       "tnDhcpRelayInfoMode": tnDhcpRelayInfoMode,
       "tnDhcpRelayInfoPolicy": tnDhcpRelayInfoPolicy,
       "tnDhcpRelayStatisticsTable": tnDhcpRelayStatisticsTable,
       "tnDhcpRelayStatisticsEntry": tnDhcpRelayStatisticsEntry,
       "tnDhcpRelayStatisticsClear": tnDhcpRelayStatisticsClear,
       "tnDhcpRelayStatisticsServerTransmitToServer": tnDhcpRelayStatisticsServerTransmitToServer,
       "tnDhcpRelayStatisticsServerTransmitError": tnDhcpRelayStatisticsServerTransmitError,
       "tnDhcpRelayStatisticsServerReceiveFromServer": tnDhcpRelayStatisticsServerReceiveFromServer,
       "tnDhcpRelayStatisticsServerReceiveMissingAgentOption": tnDhcpRelayStatisticsServerReceiveMissingAgentOption,
       "tnDhcpRelayStatisticsServerReceiveMissingCircuitID": tnDhcpRelayStatisticsServerReceiveMissingCircuitID,
       "tnDhcpRelayStatisticsServerReceiveMissingRemoteID": tnDhcpRelayStatisticsServerReceiveMissingRemoteID,
       "tnDhcpRelayStatisticsServerReceiveBadCircuitID": tnDhcpRelayStatisticsServerReceiveBadCircuitID,
       "tnDhcpRelayStatisticsServerReceiveBadRemoteID": tnDhcpRelayStatisticsServerReceiveBadRemoteID,
       "tnDhcpRelayStatisticsClientTransmitToClient": tnDhcpRelayStatisticsClientTransmitToClient,
       "tnDhcpRelayStatisticsClientTransmitError": tnDhcpRelayStatisticsClientTransmitError,
       "tnDhcpRelayStatisticsClientReceiveFromClient": tnDhcpRelayStatisticsClientReceiveFromClient,
       "tnDhcpRelayStatisticsClientReceiveAgentOption": tnDhcpRelayStatisticsClientReceiveAgentOption,
       "tnDhcpRelayStatisticsClientReplaceAgentOption": tnDhcpRelayStatisticsClientReplaceAgentOption,
       "tnDhcpRelayStatisticsClientKeepAgentOption": tnDhcpRelayStatisticsClientKeepAgentOption,
       "tnDhcpRelayStatisticsClientDropAgentOption": tnDhcpRelayStatisticsClientDropAgentOption,
       "tnDhcpMIBNotifications": tnDhcpMIBNotifications}
)
